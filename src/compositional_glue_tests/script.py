import argparse
import os
import subprocess
import json
import keyword
import xml.etree.ElementTree as ET

from src.compositional_glue_tests.utils import IMMUTABLES, default_type_value, get_method_parameter_types, write_to_file, pre_order_traversal, exception_handling, type_mapping, get_java_class_declaration
from src.compositional_glue_tests.constants import *

ERROR = "error"
SUCCESS = "success"
FAILURE = "failure"


class Project:
    """
    Represents a project under testing.
    """

    def __init__(self, name: str):
        """
        Initialize the project with the given name.
        """
        if name not in paths:
            raise ValueError(f"Project {name} not found!")

        self.name = name
        self.formatted_name = name.replace('-', '.')
        self.main_path = paths[name]['main']
        self.package = package_names[name]

        # meta information for the file
        self.script_dir = os.path.dirname(__file__)
        self.schema_dir = os.path.join(self.script_dir, SCRIPT_DIR_DEPTH, SCHEMAS_DIR)
        self.root_dir = os.path.join(self.script_dir, SCRIPT_DIR_DEPTH)
        self.project_dir = os.path.join(self.root_dir, ORIGINAL_DIR, self.name)
        self.glue_dir = os.path.join(self.root_dir, OUTPUT_DIR, self.name)

        self.__initialize_java_project()

    def __initialize_java_project(self):
        """       
        Copy original java project to glue_code directory
        but first check if pom.xml exists in the output directory and
        and if it does, store its contents      
        """        
        pom_contents = None
        if os.path.exists(f"{self.glue_dir}/pom.xml"):
            with open(f"{self.glue_dir}/pom.xml") as f:
                pom_contents = f.read()

        if not os.path.exists(f"{self.glue_dir}/"):
            os.makedirs(f"{self.glue_dir}/") # make all directories in the path
            
        # copy the project
        subprocess.run(['cp', '-r', f"{self.project_dir}/.", f"{self.glue_dir}/"], check=True)
        
        # if the 'target' directory has also been copied, remove it
        if os.path.exists(f"{self.glue_dir}/target"):
            subprocess.run(['rm', '-r', f"{self.glue_dir}/target"], check=True)

        # if pom.xml existed, write it back
        if pom_contents:
            with open(f"{self.glue_dir}/pom.xml", "w") as f:
                f.write(pom_contents)
        
        # IntegrationUtils.java
        with open(f"{self.script_dir}/misc/IntegrationUtils.java") as f:
            write_to_file(
                f"{self.glue_dir}/src/{self.main_path}IntegrationUtils.java",
                f.read().format(
                    project = self.package
                )
            )
            
        # copy java_handler.py to the translated project
        java_handler_path = f"{self.root_dir}/{TRANSLATION_DIR}/{self.name}/src/{self.main_path.replace('/java/', '/')}/java_handler.py"
        os.makedirs(os.path.dirname(java_handler_path), exist_ok=True)
        with open(f"{self.script_dir}/misc/java_handler.py") as f:
            write_to_file(
                java_handler_path,
                f.read().format(
                    project = self.package,
                    exception_map = json.dumps(exception_handling)
                )
            )

    def recompose_python_project(self, injected_translations: dict[tuple[str, str, str], str]):
        """
        (Re)compose the python project with the injected translations.
        injected_translations is a dict with the following structure:
        {
            (schema_file_name, class_name, method_name): translation,
            ...
        }
        """
        # ensure that the python project directory exists
        os.makedirs(f"{self.root_dir}/{TRANSLATION_DIR}/{self.name}/", exist_ok=True)
            
        # process all the schemas to create instrumented python files
        for schema_file_name in os.listdir(f"{self.schema_dir}/{self.name}"):
            if (schema_file_name.endswith('_python_partial.json')
                and '.test.' not in schema_file_name): # leave the test schemas alone
                          
                schema_file_name_without_ext = ".".join(schema_file_name.split('.')[:-1])
                
                with open(f"{self.schema_dir}/{self.name}/{schema_file_name}") as f:
                    schema_data = json.load(f)
                    
                schema_object = Schema(schema_file_name, self, schema_data)
                    
                # create the python file's contents
                python_file_contents = []
                
                # add imports
                # filter out unnecessary imports
                imports_from_schema = filter(
                    lambda imp: not any(x in imp for x in ['commons.io', 'commons.logging', 'opentest4j', 'com.google']),
                    schema_data['python_imports']
                )
                python_file_contents.extend(imports_from_schema)
                python_file_contents.append("import java") # import the java module (from Polyglot)
                python_file_contents.append(f"from src.{self.main_path.replace('/java/', '/').replace('/', '.')}java_handler import *")
                
                class_order = schema_object.get_class_order()

                for _class in class_order:
                    if 'new' in _class or '{' in _class: # skip "anonymous" classes
                        continue
            
                    # add declaration
                    class_declaration = schema_data['classes'][_class]['python_class_declaration']
                    
                    # get java class declaration
                    java_class_declaration = get_java_class_declaration(schema_data, _class)
                    is_static_class = 'static' in java_class_declaration
                    is_nested_class = bool(schema_data['classes'][_class]['nested_inside'])
                    
                    # the class should inherit from StaticFieldRedirector
                    class_declaration_prefix_pos = class_declaration.find(_class) + len(_class)
                    class_declaration_prefix = class_declaration[:class_declaration_prefix_pos]
                    class_declaration_suffix = class_declaration[class_declaration_prefix_pos:].strip()
                    if class_declaration_suffix == ":":
                        class_declaration_suffix = "(metaclass=StaticFieldRedirector):"
                    else:
                        bracket_left = class_declaration_suffix.find("(")
                        bracket_right = class_declaration_suffix.rfind(")")
                        if class_declaration_suffix[bracket_left+1:bracket_right].strip() == "":
                            class_declaration_suffix = "(metaclass=StaticFieldRedirector):"
                        else:
                            class_declaration_suffix = class_declaration_suffix[:bracket_right] + ", metaclass=StaticFieldRedirector" + class_declaration_suffix[bracket_right:]
                            
                    class_declaration = class_declaration_prefix + class_declaration_suffix
                    python_file_contents.append(class_declaration)
                    
                    # we do not need to add "fields" because they are taken from the Java object
                    # due to jToPy()
                    
                    # add methods
                    for _method in schema_data['classes'][_class]['methods']:
                        if (schema_file_name_without_ext, _class, _method) in injected_translations:
                            # this is the translated method
                            method_body = injected_translations[(schema_file_name_without_ext, _class, _method)]
                        else:
                            method_body = self.__get_instrumented_python_method_body(_method, schema_data['classes'][_class]['methods'][_method], _class)
                                                   
                        python_file_contents.append(method_body)
                    
                    # add other graal stuff
                    # load up the Java class            
                    subpackage = schema_object.subpackage
                    # if the class is nested inside another class, add the parent class to the class name
                    class_name_for_import = _class
                    outer_class_name = schema_data['classes'][_class]['nested_inside']
                    while outer_class_name:
                        class_name_for_import = f"{outer_class_name}${class_name_for_import}"
                        outer_class_name = schema_data['classes'][outer_class_name]['nested_inside']
                        
                    python_file_contents.append(f"    javaClz = java.type(\"{self.package}{subpackage}.{class_name_for_import}\")")
           
                    # add default constructor
                    python_file_contents.append("\n".join([
                        f"    @staticmethod",
                        f"    def getDefaultInstance():",
                        f"        return {_class}.__new__({_class})"
                    ]))
                    
                    # modify __getattr__ method to handle cases like 
                    # static field access from 'self'
                    python_file_contents.append("\n".join([
                        f"    def __getattr__(self, name):",
                        f"        try:",
                        f"            return object.__getattribute__(self, name)",
                        f"        except AttributeError:",
                        f"            pass",
                        f"        return getattr(self.javaClz, name)"
                    ]))
                    
                # write the new contents to the python file
                python_file_path = "".join([
                    f"{self.root_dir}/{TRANSLATION_DIR}/{self.name}/src/",
                    schema_data['path'].split('/src/')[1].replace('.java', '.py').replace('/java/', '/')
                ])

                os.makedirs(os.path.dirname(python_file_path), exist_ok=True)
                with open(python_file_path, "w") as f:
                    f.write("\n".join(python_file_contents))
            
    def __get_instrumented_python_method_body(self, method_name: str, method_schema_data: dict, class_name: str):
        original_method_name = method_name.split(':', 1)[1].strip() # remove the line-numbers from the method name        
        is_constructor = method_schema_data['is_constructor']
        is_static = 'static' in method_schema_data['modifiers']
        java_method_body = "".join(method_schema_data['body'])
        
        # if the method was not implemented in Java, just return the partial translation
        if java_method_body.strip()[-1] != '}':
            return "".join(method_schema_data['partial_translation'])
        
        # get the method declaration from the partial translation
        method_declaration_lines = []
        for line in method_schema_data['partial_translation']:
            if line.strip() == "pass":
                break
            method_declaration_lines.append(line)
        method_declaration = "\n".join(method_declaration_lines)
        
        parameter_types = get_method_parameter_types(method_schema_data)
        
        # build the method body            
        casted_parameters = [
            type_mapping(param, parameter_types[i], calling_from_python=True, include_idMap=True, idMap_name="idMapPyToJ")
            for i, param in enumerate(method_schema_data['parameters'])
        ]
        
        translated_args = [f"translatedArg{i} = {param}" for i, param in enumerate(casted_parameters)]
        retranslated_args = [f"JavaHandler.mapping(translatedArg{i}, idMapJToPy, {param})" for i, param in enumerate(method_schema_data['parameters'])]
        
        args_buildup = ", ".join([f"translatedArg{i}" for i in range(len(casted_parameters))])
        
        if "static" in method_schema_data['modifiers'] or is_constructor:
            caller = f"{class_name}.javaClz"
        else:
            caller = "self.javaObj"
            
        if is_constructor:
            java_call = f"{caller}({args_buildup})"
        else:
            java_call = f"{caller}.{original_method_name}({args_buildup})"
            
        method_content = []
        if is_constructor:
            method_content.append("\n".join([
                f"        idMapPyToJ = JavaHandler.valueToObject(dict(), \"Map\")",
                f"        " + "        \n".join(translated_args),
                f"        try:",
                f"            self.javaObj = {java_call}",
                f"        except:",
                f"            raise JavaHandler.mapping(java.type(\"{self.package}.ExceptionHandler\").ERR)",
                f"        finally:",
                f"            self.javaObj.setPythonObject(self)",
                f"            idMapJToPy = self.javaObj.jToPy()",
                "            " + "            \n".join(retranslated_args)
            ]))
        elif 'void' in method_schema_data['return_types'][0]:
            method_content.append("\n".join([
                f"        idMapPyToJ = self.javaObj.pyToJ()" if not is_static else "",
                f"        " + "        \n".join(translated_args),
                f"        try:",
                f"            {java_call}",
                f"        except:",
                f"            raise JavaHandler.mapping(java.type(\"{self.package}.ExceptionHandler\").ERR)",
                f"        finally:",
                f"            idMapJToPy = self.javaObj.jToPy()" if not is_static else "",
                f"            " + "            \n".join(retranslated_args)
            ]))
        else:
            method_content.append("\n".join([
                f"        idMapPyToJ = self.javaObj.pyToJ()" if not is_static else "",
                f"        " + "        \n".join(translated_args),
                f"        try:",
                f"            val = JavaHandler.mapping({java_call})",
                f"            idMapJToPy = self.javaObj.jToPy()" if not is_static else "",
                f"            " + "            \n".join(retranslated_args),
                f"            return val",
                f"        except:",
                f"            raise JavaHandler.mapping(java.type(\"{self.package}.ExceptionHandler\").ERR)",
                f"        finally:",
                f"            idMapJToPy = self.javaObj.jToPy()" if not is_static else "",
                f"            " + "            \n".join(retranslated_args)
            ]))

        method_body = method_declaration + "\n" + "\n".join(method_content)
        return method_body        
    
    def derive_compositional_tests(self, components: dict[str, dict[str, list[str]]], debug: bool = False):
        """
        Derive compositional tests for the given components.
        components is a dictionary with the following structure:
        {
            "schema_name": {
                "class_name": ["method_name"]
            }
        }
        """
        try:
            return CompositionalTest(self, components, debug)
        except NotImplementedError as e:
            return None

        
class CompositionalTest:
    """
    A compositional test for a given project
    on the given components.
    """
    
    def __init__(self, project: Project, components: dict[str, dict[str, list[str]]], debug: bool = False):
        """
        Derive compositional tests for the given components.
        components is a dictionary with the following structure:
        {
            "schema_name": {
                "class_name": ["method_name"]
            }
        }
        """
        self.project = project
        self.debug = debug
        
        # log of files to be written
        # { file_name: { original_content: str, new_content: str }}
        self.scheduled_writes = dict()
        
        # set the schemas to process
        self.__set_schemas_to_process(list(components.keys()))
        
        # list of exception-method pairs to map (from all schemas)
        self.__exceptions = []
        
        for schema in self.project_schemas:            
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                schema_data = json.load(f)
                
            schema_object = Schema(schema, self.project, schema_data)
            schema_name_full = schema.split('.')[-2]
            schema_name = schema_name_full.split('_python_partial')[0]
            
            # get the classes to process
            if schema not in self.schemas_to_process:
                # all classes remain unprocessed but have some modifications made to them
                classes_to_process = []
            else:
                classes_to_process = []
                for _class in components[schema_name]:
                    if _class not in schema_data['classes']:
                        raise ValueError(f"Class {_class} not found in schema {schema}!")
                    classes_to_process.append(_class)
                    
            class_list = self.__resolve_class_order(schema_data)
            
            for _class in class_list:
                # check if the class is enclosed within a method
                # and skip such classes
                if Schema.is_class_enclosed_in_method(_class, schema_data):
                    continue 
                
                if _class not in classes_to_process or schema_data['classes'][_class]['is_interface']:
                    # don't process this class if it's not in the list
                    # or if it's an interface
                    schema_object.add_class(_class, schema_data['classes'][_class], dont_process=True)
                    continue

                # get the methods to process
                if schema_name not in components or _class not in components[schema_name] or components[schema_name][_class] == []:
                    # Process all methods if no methods are provided
                    # or no class or schema was provided to begin with
                    methods_to_process = list(schema_data['classes'][_class]['methods'].keys())
                else:
                    # first check if the class is supported for testing
                    self.__check_if_supported_class(schema_data, _class)
                    
                    methods_to_process = []
                    
                    _available_methods = []
                    for _method in schema_data['classes'][_class]['methods']:
                        _is_constructor = schema_data['classes'][_class]['methods'][_method]['is_constructor']
                        _method_name = _method.split(':', 1)[1].strip() if not _is_constructor else "__init__"
                        
                        _available_methods.append((_method, _method_name))
                    
                    for _method in components[schema_name][_class]:
                        for m in _available_methods:
                            if m[1] == _method:
                                # check if the method is supported for testing
                                self.__check_if_supported_method(schema_data['classes'][_class]['methods'][m[0]])
                                
                                methods_to_process.append(m[0])
                                break
                        else:
                            raise ValueError(f"Method {_method} not found in class {_class} of schema {schema}!")
  
                schema_object.add_class(_class, schema_data['classes'][_class], methods_to_process)
                
                self.__exceptions.extend(schema_object.get_exceptions())
                
            # write back into the java file (with glue-instrumentation)
            local_path = schema_data['path'].split('/src/')[-1]
            self.__log_write(
                f"{self.project.glue_dir}/src/{local_path}",
                schema_object.get_body()
            )
                
        self.__add_schema_dependent_files()
        
    def __resolve_class_order(self, schema_data: dict):
        """
        Resolve the order in which classes should be processed.
        This is a pre-order traversal of the class hierarchy (in terms of nesting).
        """
        nested_inside_relations = []
        for _class in schema_data['classes']:
            if schema_data['classes'][_class]['nested_inside']:
                nested_inside_relations.append((_class, schema_data['classes'][_class]['nested_inside']))
            else:
                nested_inside_relations.append((_class, None))
                
        # sort the classes based on the nesting
        return pre_order_traversal(nested_inside_relations)
    
    def __log_write(self, file_name: str, content: str, priority: int = 0):
        """
        Log the write operation for the given file.
        Higher priority values will be written first.
        """
        if file_name not in self.scheduled_writes:
            self.scheduled_writes[file_name] = {
                "original_content": None,
                "new_content": content,
                "priority": priority
            }
        else:
            self.scheduled_writes[file_name]["new_content"] = content
            
    def __execute_writes(self):
        """
        Execute the write operations.
        """
        for file_name in sorted(self.scheduled_writes.keys(), key=lambda x: -self.scheduled_writes[x]["priority"]):
            if os.path.exists(file_name):
                with open(file_name) as f:
                    self.scheduled_writes[file_name]["original_content"] = f.read()
            
            # make the directories if they don't exist
            os.makedirs(os.path.dirname(file_name), exist_ok=True)        
            with open(file_name, "w") as f:
                f.write(self.scheduled_writes[file_name]["new_content"])
                
            # run the formatter
            if file_name.endswith('.java'):
                try:
                    subprocess.run([
                        'java', '-jar', 
                        self.project.script_dir + '/google-java-format-1.20.0-all-deps.jar', '--skip-removing-unused-imports', '-r', 
                        file_name
                    ], check=True)
                except Exception:
                    print(f"Error formatting {file_name}! This may be due to a syntax error.")
                
    def __revert_writes(self):
        """
        Revert the write operations.
        """
        for file_name in self.scheduled_writes:
            if self.scheduled_writes[file_name]["original_content"]:
                with open(file_name, "w") as f:
                    f.write(self.scheduled_writes[file_name]["original_content"])
            else:
                os.remove(file_name)
        
    def __set_schemas_to_process(self, schemas_to_process: list[str] = None):
        """
        Set up the schemas to process for the project.
        If no schemas are provided, all schemas in the project will be processed.
        """   
        self.project_schemas = [file_name for file_name in os.listdir(f'{self.project.schema_dir}/{self.project.name}') if (
            'src.test' not in file_name # ignore test schemas
            and file_name.endswith('_python_partial.json') # only consider partial schemas
        )]
        
        if not schemas_to_process:
            self.schemas_to_process = self.project_schemas
        else:
            self.schemas_to_process = []
            for schema in schemas_to_process:
                mathing_schemas = [s for s in self.project_schemas if s.endswith(f'.{schema}_python_partial.json')]
                if not mathing_schemas:
                    raise ValueError(f"Schema for {schema} not found!")
                self.schemas_to_process.extend(mathing_schemas)

    def __add_schema_dependent_files(self):
        # Add ContextInitializer.java
        ctx_mappings, ctx_imports = self.__make_ctx_mappings()
        with open(f"{self.project.script_dir}/misc/ContextInitializer.java") as f:
            self.__log_write(
                f"{self.project.glue_dir}/src/{self.project.main_path}ContextInitializer.java",
                f.read().format(
                    project = self.project.package,
                    imports = ctx_imports,
                    code_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.project.name}/src/{self.project.main_path.replace('/java/', '/')}",
                    package_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.project.name}/",
                    # ----------------------------------------------------------------------------------------------
                    # mappings = ""               
                    # ----------------------------------------------------------------------------------------------
                    mappings = ctx_mappings # We shouldn't need these anymore due to IntegrationUtils.valueToObject
                                            # but sometimes we need this for implicitly handling null values
                                            # We also need this for handling Arrays (Type[])
                                            # TODO: FIXME
                    # ----------------------------------------------------------------------------------------------
                ),
                priority = 1
            )
            
        # Add ExceptionHandler.java
        exp_mappings, exp_imports = self.__make_exp_mappings()
        with open(f"{self.project.script_dir}/misc/ExceptionHandler.java") as f:
            self.__log_write(
                f"{self.project.glue_dir}/src/{self.project.main_path}ExceptionHandler.java",
                f.read().format(
                    project = self.project.package,
                    imports = exp_imports,
                    mappings = exp_mappings
                ),
                priority = 1
            )
    
    def __make_ctx_mappings(self):
        classes_to_map = []
        imports = []
        
        for schema in self.project_schemas:
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                data = json.load(f)

            for _class in data['classes']:
                # create the class declaration
                java_class_declaration = get_java_class_declaration(data, _class)
                
                # check if the class is an enum
                is_enum = 'enum' in java_class_declaration 
                
                if (
                        not data['classes'][_class]['is_interface']
                        and not data['classes'][_class]['is_abstract']
                        and not is_enum
                        and not '/test/' in data['path']
                        and not ('new' in _class or '{' in _class) # skip "anonymous" classes
                        and not Schema.is_class_enclosed_in_method(_class, data) # skip classes enclosed in methods
                ):
                    class_to_map = self.__process_class_for_ctx_mapping(_class, data)
                    classes_to_map.append(class_to_map)
                        
        # code for the mappings
        mapping_code = "\n".join([
            "\n".join([
                f".targetTypeMapping(Value.class, {_class}.class, null, (v) -> {{",
                f"    if(v.isNull()){{ return null; }}",
                f"    {_class} obj = v.getMember(\"javaObj\").asHostObject();",
                f"    obj.pyToJ();",
                f"    return obj;",
                "})"
            ])
            for _class in classes_to_map
        ]) + "// TODO: Add other mappings"

        imports_code = ""
        
        return mapping_code, imports_code
    
    def __make_exp_mappings(self):
        classes_to_map = []
        imports = []
        std_imports = [] # imports for standard exceptions
        
        for schema in self.schemas_to_process:
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                data = json.load(f)

            for _class in data['classes']:
                if _class.endswith('Exception'): # Assuming all exceptions have the suffix 'Exception'
                    class_to_map, import_to_add = self.__process_class_for_exp_mapping(_class, data)
                    classes_to_map.append(class_to_map)
                    if import_to_add:
                        imports.append(import_to_add)
                        
        # code for the mappings
        mapping_code = "".join([
            f"if(exceptionType.equals(\"{_class}\")){{ return new {_class}(exceptionObj);}}\n" 
            for _class in classes_to_map
        ])
        
        for exception, method in self.__exceptions:
            if exception in exception_handling:
                target, call = exception_handling[exception]["target"], exception_handling[exception]["call"]
                mapping_code += f"if(exceptionType.equals(\"{target}\") && thrower.equals(\"{method}\")){{ return new {call};}}\n"
                
                # no need to make any imports here (that is handled in the next block)
        
        # now just dump all exceptions from exception_handling.json
        for exception in exception_handling:
            target, call = exception_handling[exception]["target"], exception_handling[exception]["call"]
            mapping_code += f"if(exceptionType.equals(\"{target}\")){{ return new {call};}}\n"
            
            # add the import if required
            if "import" in exception_handling[exception]:
                std_imports.append(exception_handling[exception]["import"])
              
        # code for the imports
        imports_code = "".join([
            f"import {self.project.package}{_import};"
            for _import in imports
        ]) + "".join([
            f"import {_import};"
            for _import in std_imports
        ])
        
        return mapping_code, imports_code

    def __process_class_for_ctx_mapping(self, class_name: str, schema_data: dict):
        """
        Process the given class for mapping and return the class
        identifier and the import to add.
        
        Uses full class names for classes in subpackages to avoid conflicts
        that may arise while importing from subpackages.
        """
        class_to_map = class_name
        parent_class = schema_data['classes'][class_name]['nested_inside']
        while parent_class:
            class_to_map = f"{parent_class}.{class_to_map}"
            parent_class = schema_data['classes'][parent_class]['nested_inside']
        
        # if class is from a subpackage, use the full class name
        if self.project.main_path in schema_data['path']:
            path_tail = schema_data['path'].split(self.project.main_path)[-1]
            if "/" in path_tail:
                # remove the last segment
                path_tail = path_tail[:path_tail.rfind('/')]
                subproj_name = "." + path_tail.replace('/', '.')
                class_to_map = f"{self.project.package}{subproj_name}.{class_to_map}"
                
        return class_to_map
                  
    def __process_class_for_exp_mapping(self, class_name: str, schema_data: dict):
        """
        Process the given class for mapping and return the class
        identifier and the import to add.
        """
        class_to_map = class_name
        parent_class = schema_data['classes'][class_name]['nested_inside']
        while parent_class:
            class_to_map = f"{parent_class}.{class_to_map}"
            parent_class = schema_data['classes'][parent_class]['nested_inside']
        
        # link subpackages (no need to import otherwise)
        import_to_make = None
        if self.project.main_path in schema_data['path']:
            path_tail = schema_data['path'].split(self.project.main_path)[-1]
            if "/" in path_tail:
                # remove the last segment
                path_tail = path_tail[:path_tail.rfind('/')]
                subproj_name = "." + path_tail.replace('/', '.')
                import_to_make = f"{subproj_name}.{class_name}"
                
        return class_to_map, import_to_make
    
    def run(self):
        """
        Run the compositional tests.
        """
        self.__execute_writes()

        if self.debug:
            # create a snapshot of the project in logs/glue/
            os.makedirs(f"{self.project.root_dir}/logs/glue/{self.project.name}/", exist_ok=True)
            subprocess.run(['cp', '-r', f"{self.project.glue_dir}/.", f"{self.project.root_dir}/logs/glue/{self.project.name}/"], check=True)

        failure_flag = False
        try:
            subprocess.run(
                ['mvn', 'clean', 'test', '-Drat.skip', '-q'],
                cwd=self.project.glue_dir,
                stderr=open(f"{self.project.root_dir}/glue_err.log", "w") if self.debug else subprocess.DEVNULL,
                stdout=open(f"{self.project.root_dir}/glue.log", "w") if self.debug else subprocess.DEVNULL,
                check=True
            )
        except Exception:
            failure_flag = True # check if the failure is due to the tests or something else

        self.__revert_writes()
        
        # collect the results
        failed_tests = self.__get_failed_tests_from_surefire()
        
        if failure_flag and not failed_tests:
            return {
                "status": ERROR, # error in running the tests
                "failed_tests": []
            }
        
        return {
            "status": SUCCESS if not failed_tests else FAILURE,
            "failed_tests": failed_tests
        }
    
    def __get_failed_tests_from_surefire(self):
        """
        Get the failed tests from the surefire reports.
        """
        surefire_dir = f"{self.project.glue_dir}/target/surefire-reports"
        if not os.path.exists(surefire_dir):
            return []
        
        failed_tests = []
        for file_name in os.listdir(surefire_dir):
            if file_name.startswith('TEST-') and file_name.endswith('.xml'):
                tree = ET.parse(f"{surefire_dir}/{file_name}")
                root = tree.getroot()
                for test_case in root.findall('testcase'):
                    if test_case.find('error') is not None or test_case.find('failure') is not None:
                        failed_tests.append(test_case.attrib['classname'] + '.' + test_case.attrib['name'])
                        
        return failed_tests

    @staticmethod
    def  __check_if_supported_class(schema_data: dict, class_name: str):
        """
        Check if the class can be processed.
        """
        class_data = schema_data['classes'][class_name]
        # get the class declaration
        class_declaration = get_java_class_declaration(schema_data, class_name)
        
        # no support for non-static nested classes
        if 'static' not in class_declaration and class_data['nested_inside']:
            raise NotImplementedError("Static nested classes are not supported.")

    @staticmethod
    def __check_if_supported_method(method_data: dict):
        """
        Check if the method can be processed.
        """
        method_body = "".join(method_data['body'])


class SyncMethod:
    """
    A class to manage the pyToJ and jToPy (reverse=True) methods.
    """
    
    def __init__(self, class_name: str, reverse: bool = False):
        self.class_name = class_name
        self.reverse = reverse
        self.fields = []
        
        # put the 'javaObj' field into the python object
        if not self.reverse:
            pass
        else:
            self.fields.append("this.obj.putMember(\"javaObj\", this);")
        
    def add_field(self, field_name: str, field_schema_data: dict):
        field_type = field_schema_data['types'][0][0].strip()
        
        # if field_type has any '<>', don't keep it in the formatted_field_type
        formatted_field_type = field_type.replace('<>', '')
        
        # compose name of field in Python
        if 'private' in field_schema_data['modifiers']:
            python_field_name = f"_{self.class_name}__{field_name}"
        else:
            python_field_name = field_name
        
        if not self.reverse:
            field_from_python = type_mapping(f"this.obj.getMember(\"{python_field_name}\")", formatted_field_type, include_idMap=True, target_object=field_name)
            self.fields.append(f"{field_name} = ({formatted_field_type}) {field_from_python};")
        else:
            self.fields.append(f"this.obj.putMember(\"{python_field_name}\", IntegrationUtils.mapToPython({field_name}, idMap, this.obj.getMember(\"{python_field_name}\")));")
    
    def get_body(self):
        fields_body = "\n".join(self.fields)
        
        if not self.reverse:
            return f"""
            public java.util.Map pyToJ() {{
                java.util.Map idMap = new java.util.HashMap();
                {fields_body}
                return idMap;
            }}
        """
        else:
            return f"""
            public Value jToPy() {{
                Value idMap = IntegrationUtils.mapToPython(new java.util.HashMap());
                return jToPy(idMap);
            }}
            public Value jToPy(Value idMap) {{
                {fields_body}
                return idMap;
            }}
        """
                

class Schema:
    """
    A class to manage the contents of a schema.
    """
    
    def __init__(self, name: str, project: Project, schema_data: dict):
        self.name = name
        self.project = project
        self.schema_data = schema_data
        
        self.__resolve_subpackage()
        self.__resolve_imports()
        
        # list of classes to be added to the schema
        # where each class is a string of the class body
        # or a dictionary with different parts of the class
        self.__classes = []
        
        # list of exception-method pairs to map
        self.__exceptions = []
        
    def add_class(self, class_name: str, class_schema_data: dict, methods_to_process: list[str] = None, dont_process: bool = False):
        if 'new' in class_name or '{' in class_name:
            return # skip "anonymous" classes
        
        if not methods_to_process:
            methods_to_process = []
        
        # create the class declaration
        class_declaration = get_java_class_declaration(self.schema_data, class_name)
        
        is_interface = class_schema_data['is_interface']
        is_enum = 'enum' in class_declaration
        is_static = 'static' in class_declaration
        is_nested = bool(class_schema_data['nested_inside'])
        is_abstract = class_schema_data['is_abstract']
        
        # if the class is not public, make it public
        if 'public' not in class_declaration:
            # check if the class is marked as private or protected
            if 'private' in class_declaration:
                class_declaration = class_declaration.replace('private', 'public', 1)
            elif 'protected' in class_declaration:
                class_declaration = class_declaration.replace('protected', 'public', 1)
            else:
                class_declaration = "public " + class_declaration

        class_obj = {
            "name": class_name,
            "declaration": class_declaration,
            "fields": [],
            "unitialized_fields": [],
            "methods": [],
            "pyToJ": SyncMethod(class_name) if not (is_interface) else None,
            "jToPy": SyncMethod(class_name, reverse=True) if not (is_interface) else None,
            "nests": [],
            "is_interface": is_interface,
            "is_enum": is_enum
        }
        
        value_fields = [] # fields that are related to graal
        
        # add graal-related members (unless it is an interface)
        if not (is_interface):
            python_file_dir = self.subpackage.replace('.', '/')
            python_file_dir = python_file_dir[:-1] if not python_file_dir else python_file_dir
            current_file_name = self.schema_data["path"].split('/')[-1].split('.')[0]
            python_file = f'{python_file_dir}/{current_file_name}.py'
            
            value_fields += [
                (
                    f"private static final Value clz = ContextInitializer.getPythonClass(\"{python_file}\", \"{class_name}\");"
                    if not (not is_static and is_nested) and not is_enum
                    else
                    # compromise for non-static nested classes (which we do not support)
                    # and also for enums
                    f"private final Value clz = ContextInitializer.getPythonClass(\"{python_file}\", \"{class_name}\");"
                 ),
                
                # 'transient' so that it is not part of serialization
                f"private transient Value obj = clz.invokeMember(\"getDefaultInstance\");"
            ]
            unititialized_fields_body = "".join(class_obj["unitialized_fields"])

            # add getPythonObject() and setPythonObject() methods
            class_obj["methods"].append(f"""
                public Value getPythonObject() {{
                    return obj;
                }}
            """)
            class_obj["methods"].append(f"""
                public void setPythonObject(Value obj) {{
                    this.obj = obj;
                }}
            """)        
    
        # we sort the fields to ensure that they are in the correct order
        # since key-names are prefixed by line numbers
        line_numbers_already_added = set()
        for _field in sorted(list(class_schema_data['fields'].keys()), key=lambda x: int(x.split('-')[0])):
            _field_line_numbers = _field.split(':')[0]            
            self.__add_field_to_class(
                class_obj, 
                _field, 
                class_schema_data['fields'][_field], 
                dont_process=dont_process, 
                field_of_enum=is_enum,
                skip_body=_field_line_numbers in line_numbers_already_added # skip the body if it has already been added
            )
            line_numbers_already_added.add(_field_line_numbers)
            
        # value fields should come first
        # except for enums for which they should come later
        if not is_enum:
            class_obj["fields"] = value_fields + class_obj["fields"]
        else:
            # TODO: FIXME!!
            # add an ";" to the last field
            class_obj["fields"][-1] += ';'
            
            class_obj["fields"] = class_obj["fields"] + value_fields
            
        for _method in class_schema_data['methods']:
            self.__add_method_to_class(
                class_obj, 
                _method, 
                class_schema_data['methods'][_method], 
                dont_process = dont_process or _method not in methods_to_process
            )

        # check if this class is nested inside another class
        if class_schema_data['nested_inside']:
            parent_class = class_schema_data['nested_inside']
            parent_class_obj = self.__search_for_class(parent_class)
            parent_class_obj["nests"].append(class_obj)
        else:
            self.__classes.append(class_obj)

    def __search_for_class(self, class_name: str) -> dict:
        """
        Searches for a class in the schema and returns the class object.
        """
        for _class in self.__classes:
            res = self.__search_for_class_recursively(_class, class_name)
            if res:
                return res
            
        return None            
        
    def __search_for_class_recursively(self, class_obj: dict, class_name: str) -> dict:
        if class_obj["name"] == class_name:
            return class_obj
        
        for _class in class_obj["nests"]:
            res =  self.__search_for_class_recursively(_class, class_name)
            if res:
                return res
        
        return None
    
    def __add_field_to_class(self, class_obj: dict, field_name: str, field_schema_data: dict, dont_process: bool = False, field_of_enum=False, skip_body=False):
        field_name = field_name.split(':')[1].strip()
        field_type = field_schema_data['types'][0][0]
        field_body = "".join(field_schema_data['body'])
        
        is_final = 'final' in field_schema_data['modifiers']
        is_public = 'public' in field_schema_data['modifiers']
        
        # make the field public if it is not
        if not is_public:
            # check if the field is marked as private or protected
            if 'private' in field_body:
                field_body = field_body.replace('private', 'public', 1)
            elif 'protected' in field_body:
                field_body = field_body.replace('protected', 'public', 1)
            else:
                field_body = "public " + field_body
            
        # if the field is from an enum, check that it is followed by a comma
        # unless it is followed by a semi-colon
        if field_of_enum:
            if (field_body.strip()[-1] != ','
                and field_body.strip()[-1] != ';'):
                field_body += ','

        # processing for creating pyToJ and jToPy methods (if the field is not static)
        if 'static' not in field_schema_data['modifiers']:
            # add field to pyToJ() and jToPy() methods if those methods exist
            if class_obj["pyToJ"] and class_obj["jToPy"]:
                # deal with pyToJ
                if (
                    not is_final  # don't add final fields to pyToJ...
                    or field_type not in IMMUTABLES # ...unless they are immutable
                ):                
                    if is_final: # if field is 'final', remove the 'final' keyword
                        field_body = field_body.replace('final', '', 1)

                    class_obj["pyToJ"].add_field(field_name, field_schema_data)

                # deal with jToPy
                class_obj["jToPy"].add_field(field_name, field_schema_data)

        if not skip_body:
            class_obj["fields"].append(field_body)

        # check if this field was not initialized (except for fields of enums)
        if not field_of_enum:
            if '=' not in field_body:
                class_obj["unitialized_fields"].append(f"{field_name} = {default_type_value[field_type]};")

    def __add_method_to_class(self, class_obj: dict, method_name: str, method_schema_data: dict, dont_process: bool = False):
        method_body = "".join(method_schema_data['body'])
        # check if the method is not implemented
        if method_body.strip()[-1] != '}':
            # add a semi-colon if not present
            if method_body.strip()[-1] != ';':
                method_body += ';'
            
            class_obj["methods"].append(method_body)
            return
        
        method_signature = method_body[:method_body.find('{')+1]
        method_content = method_body[method_body.find('{')+1:method_body.rfind('}')]
        is_constructor = method_schema_data['is_constructor']
        method_name = method_name.split(':', 1)[1].strip() if not is_constructor else "__init__"

        # if method is private, take mangling into account
        # except for constructors
        if 'private' in method_schema_data['modifiers'] and not is_constructor:
            method_name = f"_{class_obj['name']}__{method_name}"
        
        # take into account the naming scheme for protected methods
        elif 'protected' in method_schema_data['modifiers'] and not is_constructor:
            method_name = f"_{method_name}"
            
        # if method name is a keyword, add an underscore at the end
        if keyword.iskeyword(method_name):
            method_name += "_"
        
        # handle the presence of exceptions
        exception_name = None # We only handle one exception for now! TODO: Fix this later
        if 'throws' in method_body: # if specificied with the "throws" keyword
            exception_name = method_body[method_body.find('throws')+6:method_body.find('{')].strip()
            exception_name = exception_name.split(',')[0].strip() # take the first exception for now if there are multiple
        elif 'throw new' in method_body: # if specified with the "throw new" keyword but not in the method signature
            throw_new_pos = method_body.find('throw new')
            exception_name = method_body[throw_new_pos+9:method_body.find('(', throw_new_pos)].strip()
        
        # check if the method signature should have @Override
        if 'Override' in method_schema_data['annotations'] and '@Override' not in method_signature:
            method_signature = '@Override\n' + method_signature
        
        # if the method is not public, make it so
        # unless it is the constructor of an enum (cannot be public)
        if (
            'public' not in method_signature
            and not (class_obj["is_enum"] and is_constructor)
        ):
            # check if the method is marked as private or protected
            if 'private' in method_signature:
                method_signature = method_signature.replace('private', 'public', 1)
            elif 'protected' in method_signature:
                method_signature = method_signature.replace('protected', 'public', 1)
            else:
                method_signature = "public " + method_signature
        
        # if method is not to be processed, add it directly
        if dont_process:
            # intercept exceptions to save them in the ExceptionHandler
            # before rethrowing them
            if exception_name:
                method_content = f"""
                    try {{
                        {method_content}
                    }} catch (Exception e) {{
                        ExceptionHandler.ERR = e;
                        throw e;
                    }}
                """
            class_obj["methods"].append(f"{method_signature}\n{method_content}\n}}")
            return
        
        # comment out the original method contents
        final_method_content = "".join([f"// {line.strip()}\n" for line in method_content.split('\n')])
            
        # construct call to Python
        if "static" in method_schema_data['modifiers']:
            caller = "clz"
        else:
            caller = "this.obj"

        parameter_types = get_method_parameter_types(method_schema_data)
        casted_parameters = [f"IntegrationUtils.mapToPython({param}, idMapJToPy)" for param in method_schema_data['parameters']]
        translated_args = "\n".join([
            f"Value translatedArg{i} = {param};" for i, param in enumerate(casted_parameters)
        ])
        retranslated_args = "\n".join([
            type_mapping(f"translatedArg{i}", param_type, target_object=param_name, include_idMap=True, idMap_name="idMapPyToJ") + ";"
            for i, (param_type, param_name) in enumerate(zip(parameter_types, method_schema_data['parameters']))
        ])

        args_buildup = ", ".join([f"translatedArg{i}" for i in range(len(casted_parameters))])
        
        if is_constructor:
            python_call = f"{caller}.invokeMember(\"__init__\"{', ' + args_buildup if args_buildup else ''})"
        else:
            python_call = f"{caller}.invokeMember(\"{method_name}\"{', ' + args_buildup if args_buildup else ''})"

        if is_constructor:
            final_method_content += f"Value idMapJToPy = jToPy();{translated_args}{python_call};java.util.Map idMapPyToJ = pyToJ();{retranslated_args}"
        elif 'void' in method_signature:
            if 'static' in method_schema_data['modifiers']:
                final_method_content += f"{translated_args}{python_call};{retranslated_args}" # no need to sync for static methods
            else:
                final_method_content += f"Value idMapJToPy = jToPy();{translated_args}{python_call};java.util.Map idMapPyToJ = pyToJ();{retranslated_args}"
        else:
            return_type = method_schema_data['return_types'][0][0]
            
            # remove any <> in the return type
            return_type = return_type.replace('<>', '').strip()
            
            return_type_casted = type_mapping(python_call, return_type)
            
            final_method_content += "".join([
                f"Value idMapJToPy = " + (
                    "jToPy()" if 'static' not in method_schema_data['modifiers'] else 'IntegrationUtils.mapToPython(new java.util.HashMap())'
                ) + ";",
                translated_args,
                f"{return_type} val = ({return_type}) {return_type_casted};",
                "java.util.Map idMapPyToJ = " + (
                    "pyToJ()" if 'static' not in method_schema_data['modifiers'] else 'new java.util.HashMap()'
                ) + ";",
                retranslated_args,
                f"return val;"
            ])
        
        # exception handling        
        if exception_name:            
            final_method_content = f"""
            try {{
                {final_method_content}
            }} catch (PolyglotException e) {{
                throw ({exception_name}) ExceptionHandler.handle(e, "{class_obj['name']}.{method_name}");
            }} finally {{
                pyToJ();
                {retranslated_args}
            }}
            """
            self.__exceptions.append((exception_name, f"{class_obj['name']}.{method_name}"))
            
        class_obj["methods"].append(f"{method_signature}\n{final_method_content}\n}}")
        
    def __resolve_subpackage(self):
        """find subpackage name (if exists)"""
        self.subpackage = ""
        if self.project.main_path in self.schema_data['path']:
            path_tail = self.schema_data['path'].split(self.project.main_path)[-1]
            if "/" in path_tail:
                # remove the last segment
                path_tail = path_tail[:path_tail.rfind('/')]
                self.subpackage = "." + path_tail.replace('/', '.')
    
    def __resolve_imports(self):
        """resolve imports for the schema"""
        self.imports = [
            "import org.graalvm.polyglot.Value;",
            "import org.graalvm.polyglot.PolyglotException;",
            f"import {self.project.package}.ContextInitializer;",
            f"import {self.project.package}.ExceptionHandler;",
            f"import {self.project.package}.IntegrationUtils;"
        ]
        self.imports.extend([
            "".join(self.schema_data['imports'][_import]["body"])
            for _import in self.schema_data['imports']
        ])
        
    def __get_class_body(self, _class: dict | str):
        """
        Get the body of the class.
        """
        if isinstance(_class, str):
            return _class
        
        # class is provided as a dictionary
        return "".join([
            _class['declaration'],
            "".join([
                self.__get_class_body(nested_class) for nested_class in _class['nests']
            ]),
            "".join(_class['fields']),
            "".join(_class['methods']),
            _class['pyToJ'].get_body() if _class['pyToJ'] else "",
            _class['jToPy'].get_body() if _class['jToPy'] else "",
            "}"
        ])
        
    def get_body(self):
        """
        Get the body of the schema.
        """
        class_bodies = "".join([
            self.__get_class_body(_class) for _class in self.__classes
        ])
        
        return f"""
        package {package_names[self.project.name]}{self.subpackage};
        {"".join(self.imports)}
        {class_bodies}
        """
        
    def get_exceptions(self):
        return self.__exceptions
    
    def get_class_order(self):
        """
        Get the order of classes in the schema based on inheritance.
        """
        class_order = []
        while len(class_order) != len(self.schema_data['classes']):
            for class_ in self.schema_data['classes']:
                if class_ in class_order:
                    continue

                if not set(self.schema_data['classes'][class_]['extends']).issubset(set(class_order)) and all([x in self.schema_data['classes'].keys() for x in self.schema_data['classes'][class_]['extends']]):
                    continue
                
                if not set(self.schema_data['classes'][class_]['implements']).issubset(set(class_order)) and all([x in self.schema_data['classes'].keys() for x in self.schema_data['classes'][class_]['implements']]):
                    continue                                                                                                                       
                
                if self.schema_data['classes'][class_]['nests'] == []:
                    class_order.append(class_)
                    continue

                if all([x in class_order for x in self.schema_data['classes'][class_]['nests']]):
                    class_order.append(class_)
        
        return class_order
    
    @staticmethod
    def is_class_enclosed_in_method(class_name: str, schema_data: dict):
        """
        Check if the class is enclosed in a method.
        """
        class_declaration_line = schema_data['classes'][class_name]['start']
        outer_class = schema_data['classes'][class_name]['nested_inside']
        
        # if there is no outer class, then the class can't be enclosed in a method
        if not outer_class:
            return False
        
        # loop over all methods in the outer class
        for method in schema_data['classes'][outer_class]['methods']:
            method_start_line = schema_data['classes'][outer_class]['methods'][method]['start']
            method_end_line = schema_data['classes'][outer_class]['methods'][method]['end']
            
            if method_start_line <= class_declaration_line <= method_end_line:
                return True
            
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Compositional Testing.')
    parser.add_argument('--project', type=str, dest='project_name', help='<Required> name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', help='list of class name(s)', required=False)
    parser.add_argument('--method', type=str, dest='method_name', help='name of the method', required=False)
    args = parser.parse_args()
    
    project = Project(args.project_name)
    test = project.derive_compositional_tests({
        args.class_name: {
            args.class_name: [args.method_name]
        }
    })
    print(test.run())
