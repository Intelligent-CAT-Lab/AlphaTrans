import argparse
import os
import subprocess
import json
import keyword
import xml.etree.ElementTree as ET
 
from src.compositional_glue_tests.utils import default_type_value, write_to_file, type_handling, pre_order_traversal
from src.compositional_glue_tests.constants import *


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
                f"{self.glue_dir}/src/{paths[self.name]['main']}IntegrationUtils.java",
                f.read().format(
                    project = f"org.apache.{self.formatted_name}"
                )
            )
            
        # copy java_handler.py to the translated project
        subprocess.run([
            "cp", 
            f"{self.script_dir}/misc/java_handler.py", 
            f"{self.root_dir}/{TRANSLATION_DIR}/{self.name}/src/{paths[self.name]['main'].replace('/java/', '/')}/"
        ], check=True)
        
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
                python_file_contents.extend(schema_data['python_imports'])
                python_file_contents.append("import java") # import the java module (from Polyglot)
                
                # add classes
                for _class in schema_data['classes']:
                    # add declaration
                    python_file_contents.append(schema_data['classes'][_class]['python_class_declaration'])
                    
                    # ----------------------------------------------------------------------------------------------------------------
                    # add fields
                    # for _field in schema_data['classes'][_class]['fields']:
                    #     if schema_data['classes'][_class]['fields'][_field]['translation_status'] == "success":
                    #         python_file_contents.append("\n".join(schema_data['classes'][_class]['fields'][_field]['translation']))
                    #     else:
                    #         pass # TODO: What do we do when the field was not translated successfully?
                    # ----------------------------------------------------------------------------------------------------------------
                    # On second thought, we will not add fields to the python file!
                    # This should be taken care of by the sync() and revsync() methods.
                    
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
                    if schema_data['classes'][_class]['nested_inside']:
                        class_name = f"{schema_data['classes'][_class]['nested_inside']}.{_class}"
                    else:
                        class_name = _class
                    
                    python_file_contents.append(f"    javaClz = java.type(\"org.apache.{self.formatted_name}{subpackage}.{class_name}\")")
                    
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
        
        # build the method body            
        casted_parameters = [param for param in method_schema_data['parameters']] # TODO: Add type casting
        
        args_buildup = ", ".join(casted_parameters)
        
        if "static" in method_schema_data['modifiers'] or is_constructor:
            caller = f"{class_name}.javaClz"
        else:
            caller = "self.obj"
            
        if is_constructor:
            java_call = f"{caller}.pythonFactory()"
        else:
            java_call = f"{caller}.{original_method_name}({args_buildup})"
            
        method_content = []
        if is_constructor:
            # TODO: Fix stuff for constructors
            method_content.append(f"        self.javaObj = {java_call}")
        elif 'void' in method_schema_data['modifiers']:
            method_content.append(f"        {java_call}")
        else:
            method_content.append(f"        return {java_call}")
            
        # TODO: revsync and sync?
        # TODO: Add error handling
        
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
        If no schemas are provided, all schemas in the project will be processed.
        
        For a given schema, if an empty dictionary is provided, all classes will be processed.
        If None is provided, no classes will be processed.
        
        For a given class, if an empty list is provided, all methods will be processed.
        If None is provided, no methods will be processed.
        """
        return CompositionalTest(self, components, debug)

        
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
        
        for schema in self.schemas_to_process:
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                schema_data = json.load(f)
                
            schema_object = Schema(schema, self.project, schema_data)
            schema_name_full = schema.split('.')[-2]
            schema_name = schema_name_full.split('_python_partial')[0]
            
            # get the classes to process
            if schema_name not in components or components[schema_name] == {}:
                # Process all classes if no classes are provided
                # or no schema was provided to begin with
                classes_to_process = list(schema_data['classes'].keys())
            elif components[schema_name] is None:
                classes_to_process = []            
            else:
                classes_to_process = []
                for _class in components[schema_name]:
                    if _class not in schema_data['classes']:
                        raise ValueError(f"Class {_class} not found in schema {schema}!")
                    classes_to_process.append(_class)
                    
                    # check if this class extends another class
                    if schema_data['classes'][_class]['extends']:
                        parent_class = schema_data['classes'][_class]['extends'][0]
                                                
                        # check if this class is being processed
                        if parent_class not in [
                            c for s in components for c in components[s] if components[s][c] is not None
                        ]:
                            # find the schema for the parent class
                            # (assuming the parent class has its own schema)
                            for file_name in os.listdir(f'{self.project.schema_dir}/{self.project.name}'):
                                if file_name.endswith(f'.{parent_class}_python_partial.json'):
                                    # add the parent class to the components
                                    _schema = file_name[:file_name.rfind('.')].split('.')[-1]
                                    if _schema in components:
                                        components[_schema][parent_class] = None
                                    else:
                                        self.schemas_to_process.append(file_name)
                                        components[_schema] = {parent_class: None}
                    
            class_list = self.__resolve_class_order(schema_data)
            
            for _class in class_list:
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
                elif components[schema_name][_class] is None:
                    methods_to_process = []
                else:
                    methods_to_process = []
                    
                    _available_methods = []
                    for _method in schema_data['classes'][_class]['methods']:
                        _is_constructor = schema_data['classes'][_class]['methods'][_method]['is_constructor']
                        _method_name = _method.split(':', 1)[1].strip() if not _is_constructor else "__init__"
                        
                        _available_methods.append((_method, _method_name))
                    
                    for _method in components[schema_name][_class]:
                        for m in _available_methods:
                            if m[1] == _method:
                                methods_to_process.append(m[0])
                                break
                        else:
                            raise ValueError(f"Method {_method} not found in class {_class} of schema {schema}!")
                    
                schema_object.add_class(_class, schema_data['classes'][_class], methods_to_process)
                
            # write back into the java file (with glue-instrumentation)
            local_path = schema_data['path'].split('/src/')[-1]
            self.__log_write(
                f"{self.project.glue_dir}/src/{local_path}",
                schema_object.get_body()
            )
        
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
    
    def __log_write(self, file_name: str, content: str):
        """
        Log the write operation for the given file.
        """
        if file_name not in self.scheduled_writes:
            self.scheduled_writes[file_name] = {
                "original_content": None,
                "new_content": content
            }
        else:
            self.scheduled_writes[file_name]["new_content"] = content
            
    def __execute_writes(self):
        """
        Execute the write operations.
        """
        for file_name in self.scheduled_writes:
            if os.path.exists(file_name):
                with open(file_name) as f:
                    self.scheduled_writes[file_name]["original_content"] = f.read()
            
            # make the directories if they don't exist
            os.makedirs(os.path.dirname(file_name), exist_ok=True)        
            with open(file_name, "w") as f:
                f.write(self.scheduled_writes[file_name]["new_content"])
                
            # run the formatter
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
        project_schemas = [file_name for file_name in os.listdir(f'{self.project.schema_dir}/{self.project.name}') if (
            'src.test' not in file_name # ignore test schemas
            # and not file_name.endswith('_python_partial.json') # ignore partial schemas
        )]
        
        if not schemas_to_process:
            self.schemas_to_process = project_schemas
        else:
            self.schemas_to_process = []
            for schema in schemas_to_process:
                mathing_schemas = [s for s in project_schemas if s.endswith(f'.{schema}_python_partial.json')]
                if not mathing_schemas:
                    raise ValueError(f"Schema for {schema} not found!")
                self.schemas_to_process.extend(mathing_schemas)
                
        self.__add_schema_dependent_files()

    def __add_schema_dependent_files(self):
        # Add ContextInitializer.java
        ctx_mappings, ctx_imports = self.__make_ctx_mappings()
        with open(f"{self.project.script_dir}/misc/ContextInitializer.java") as f:
            self.__log_write(
                f"{self.project.glue_dir}/src/{paths[self.project.name]['main']}ContextInitializer.java",
                f.read().format(
                    project = f"org.apache.{self.project.formatted_name}",
                    imports = ctx_imports,
                    code_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.project.name}/src/{paths[self.project.name]['main'].replace('/java/', '/')}",
                    package_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.project.name}/",
                    mappings = ctx_mappings                
                )
            )
            
        # Add ExceptionHandler.java
        exp_mappings, exp_imports = self.__make_exp_mappings()
        with open(f"{self.project.script_dir}/misc/ExceptionHandler.java") as f:
            self.__log_write(
                f"{self.project.glue_dir}/src/{paths[self.project.name]['main']}ExceptionHandler.java",
                f.read().format(
                    project = f"org.apache.{self.project.formatted_name}",
                    imports = exp_imports,
                    mappings = exp_mappings
                )
            )
    
    def __make_ctx_mappings(self):
        classes_to_map = []
        imports = []
        
        for schema in self.schemas_to_process:
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                data = json.load(f)

            for _class in data['classes']:
                if (
                        not data['classes'][_class]['is_interface'] 
                        and not '/test/' in data['path'] 
                        and not _class.endswith('Exception')
                ):
                    class_to_map, import_to_add = self.__process_class_for_mapping(_class, data)
                    classes_to_map.append(class_to_map)
                    if import_to_add:
                        imports.append(import_to_add)
                        
        # code for the mappings
        mapping_code = "".join([
            f".targetTypeMapping(Value.class, {_class}.class, null, (v) -> new {_class}(v))\n" 
            for _class in classes_to_map
        ]) + "// TODO: Add other mappings"
        
        # code for the imports
        imports_code = "".join([
            f"import org.apache.{self.project.formatted_name}{_import};"
            for _import in imports
        ])
        
        return mapping_code, imports_code
    
    def __make_exp_mappings(self):
        classes_to_map = []
        imports = []
        
        for schema in self.schemas_to_process:
            with open(f'{self.project.schema_dir}/{self.project.name}/{schema}') as f:
                data = json.load(f)

            for _class in data['classes']:
                if _class.endswith('Exception'): # Assuming all exceptions have the suffix 'Exception'
                    class_to_map, import_to_add = self.__process_class_for_mapping(_class, data)
                    classes_to_map.append(class_to_map)
                    if import_to_add:
                        imports.append(import_to_add)
                        
        # code for the mappings
        mapping_code = "".join([
            f"if(exceptionType.equals(\"{_class}\")){{ return new {_class}(exceptionObj);}}\n" 
            for _class in classes_to_map
        ]) + "// TODO: Add other mappings"
        
        # code for the imports
        imports_code = "".join([
            f"import org.apache.{self.project.formatted_name}{_import};"
            for _import in imports
        ])
        
        return mapping_code, imports_code
                  
    def __process_class_for_mapping(self, class_name: str, schema_data: dict):
        """
        Process the given class for mapping and return the class
        identifier and the import to add.
        """
        if schema_data['classes'][class_name]["nested_inside"]:
            class_to_map =  f"{schema_data['classes'][class_name]['nested_inside']}.{class_name}"
        else:
            class_to_map = class_name
        
        # link subpackages (no need to import otherwise)
        import_to_make = None
        if paths[self.project.name]['main'] in schema_data['path']:
            path_tail = schema_data['path'].split(paths[self.project.name]['main'])[-1]
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
            
        if self.debug:
            # create a snapshot of the project in logs/glue/
            os.makedirs(f"{self.project.root_dir}/logs/glue/{self.project.name}/", exist_ok=True)
            subprocess.run(['cp', '-r', f"{self.project.glue_dir}/.", f"{self.project.root_dir}/logs/glue/{self.project.name}/"], check=True)
        
        self.__revert_writes()
        
        # collect the results
        failed_tests = self.__get_failed_tests_from_surefire()
        
        if failure_flag and not failed_tests:
            # raise Exception("An error occurred while running the tests!")
            
            # for now, we will just return False (a potential false negative)
            # so that the pipeline doesn't stop
            return {
                "status": False,
                "failed_tests": []
            }
        
        return {
            "status": True if not failed_tests else False,
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

class SyncMethod:
    """
    A class to manage the sync and revsync methods.
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
        field_type = field_schema_data['types'][0][0]
        
        # compose name of field in Python
        if 'private' in field_schema_data['modifiers']:
            python_field_name = f"_{self.class_name}__{field_name}"
        else:
            python_field_name = field_name
        
        field_from_python = type_handling[field_type].format("this.obj.getMember(\"" + python_field_name + "\")")
        
        if not self.reverse:
            self.fields.append(f"{field_name} = ({field_type}) {field_from_python};")
        else:
            self.fields.append(f"this.obj.putMember(\"{python_field_name}\", IntegrationUtils.mapToPython({field_name}));")
    
    def get_body(self):
        if not self.reverse:
            method_name = "sync"
        else:
            method_name = "revsync"
        
        body = "\n".join(self.fields)
            
        return f"""
            public void {method_name}() {{
                {body}
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
        
    def add_class(self, class_name: str, class_schema_data: dict, methods_to_process: list[str] = None, dont_process: bool = False):
        if not methods_to_process:
            methods_to_process = []
        
        # create the class declaration
        with open(self.schema_data['path'], 'r') as f:
            lst = f.readlines()
        class_declaration = "".join(lst[class_schema_data['start']-1:class_schema_data['end']])
        
        # if the class is not public, make it public
        if 'public' not in class_declaration:
            # check if the class is marked as private
            if 'private' in class_declaration:
                class_declaration = class_declaration.replace('private', 'public', 1)
            else:
                class_declaration = "public " + class_declaration
        
        class_obj = {
            "name": class_name,
            "declaration": class_declaration,
            "fields": [],
            "unitialized_fields": [],
            "methods": [],
            "sync": SyncMethod(class_name) if not dont_process else None,
            "revsync": SyncMethod(class_name, reverse=True) if not dont_process else None,
            "nests": []
        }
        
        for _field in class_schema_data['fields']:
            self.__add_field_to_class(class_obj, _field, class_schema_data['fields'][_field], dont_process=dont_process)
            
        for _method in class_schema_data['methods']:
            if dont_process:
                self.__add_method_to_unprocessed_class(class_obj, _method, class_schema_data['methods'][_method])
            else:
                if _method in methods_to_process:
                    self.__add_method_to_class(class_obj, _method, class_schema_data['methods'][_method])
                else:
                    self.__add_method_to_class(class_obj, _method, class_schema_data['methods'][_method], dont_process=True)
        
        # add graal-related members and a default constructor
        python_file_dir = self.subpackage.replace('.', '/')
        python_file_dir = python_file_dir[:-1] if not python_file_dir else python_file_dir
        current_file_name = self.schema_data["path"].split('/')[-1].split('.')[0]
        python_file = f'{python_file_dir}/{current_file_name}.py'
        
        class_obj["fields"].extend([
            f"private static Value clz = ContextInitializer.getPythonClass(\"{python_file}\", \"{class_name}\");",
            "private Value obj;"
        ])
        unititialized_fields_body = "".join(class_obj["unitialized_fields"])
        
        # add Value constructor
        class_obj["methods"].append(f"""
            public {class_name}(Value obj) {{
                {unititialized_fields_body}
                this.obj = obj;
            }}                            
        """)

        # add getPythonObject()
        class_obj["methods"].append(f"""
            public Value getPythonObject() {{
                return obj;
            }}
        """)

        # add a Default constructor
        class_obj["methods"].append(f"""
            public {class_name}() {{
                {unititialized_fields_body}
                this.obj = clz.newInstance();
            }}
        """)
        
        # check if this class is nested inside another class
        if class_schema_data['nested_inside']:
            parent_class = class_schema_data['nested_inside']
            for _class in self.__classes:
                if _class['name'] == parent_class:
                    _class["nests"].append(class_obj)
                    break
        else:
            self.__classes.append(class_obj)
        
    def __add_field_to_class(self, class_obj: dict, field_name: str, field_schema_data: dict, dont_process: bool = False):
        field_name = field_name.split(':')[1].strip()
        field_type = field_schema_data['types'][0][0]
        field_body = "".join(field_schema_data['body'])

        if not dont_process:
            # if field is 'final', remove the 'final' keyword
            if 'final' in field_schema_data['modifiers']:
                field_body = field_body.replace(' final', '', 1)
            
            # add field to sync() and revsync() methods
            class_obj["sync"].add_field(field_name, field_schema_data)
            class_obj["revsync"].add_field(field_name, field_schema_data)      
        
        class_obj["fields"].append(field_body)
        
        # check if this field was not initialized
        if '=' not in field_body:
            class_obj["unitialized_fields"].append(f"{field_name} = {default_type_value[field_type]};")
        
    def __add_method_to_unprocessed_class(self, class_obj: dict, method_name: str, method_schema_data: dict):
        method_body = "".join(method_schema_data['body'])
        method_signature = method_body[:method_body.find('{')+1]
        method_content = method_body[method_body.find('{')+1:method_body.rfind('}')]
        
        # if the method is not public, make it so
        if 'public' not in method_signature:
            # check if the method is marked as private
            if 'private' in method_signature:
                method_signature = method_signature.replace('private', 'public', 1)
            else:
                method_signature = "public " + method_signature
                
        class_obj["methods"].append(f"{method_signature}\n{method_content}\n}}")
    
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
        
        # if the method is not public, make it so
        if 'public' not in method_signature:
            # check if the method is marked as private
            if 'private' in method_signature:
                method_signature = method_signature.replace('private', 'public', 1)
            else:
                method_signature = "public " + method_signature
        
        # if method is not to be processed, add it directly
        if dont_process:
            class_obj["methods"].append(f"{method_signature}\n{method_content}\n}}")
            return
        
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
        
        # comment out the original method contents if method is not a constructor, else leave it as it is
        if is_constructor:
            final_method_content = method_content
        else:
            final_method_content = "".join([f"// {line.strip()}\n" for line in method_content.split('\n')])
            
        # construct call to Python
        if "static" in method_schema_data['modifiers'] or is_constructor:
            caller = "clz"
        else:
            caller = "this.obj"
            
        casted_parameters = [f"IntegrationUtils.mapToPython({param})" for param in method_schema_data['parameters']]
            
        args_buildup = ", ".join(casted_parameters)
        
        if is_constructor:
            python_call = f"clz.newInstance({args_buildup})"
        else:
            python_call = f"{caller}.invokeMember(\"{method_name}\"{', ' + args_buildup if args_buildup else ''})"
            
        if is_constructor:
            final_method_content += f"this.obj = {python_call};sync();"
        elif 'void' in method_signature:
            if 'static' in method_schema_data['modifiers']:
                final_method_content += f"{python_call};" # no need to sync for static methods
            else:
                final_method_content += f"revsync();{python_call};sync();"
        else:
            return_type = method_schema_data['return_types'][0][0]
            return_type_casted = type_handling[return_type].format(python_call)
            
            final_method_content += "".join([
                f"revsync();" if 'static' not in method_schema_data['modifiers'] else '', # no need to sync for static methods
                f"{return_type} val = ({return_type}) {return_type_casted};",
                "sync();" if 'static' not in method_schema_data['modifiers'] else '', # no need to sync for static methods
                f"return val;"
            ])
        
        # handle the presence of exceptions
        if 'throws' in method_body:
            exception_name = method_body[method_body.find('throws')+6:method_body.find('{')].strip()
            final_method_content = f"""
            try {{
                {final_method_content}
            }} catch (PolyglotException e) {{
                throw ({exception_name}) ExceptionHandler.handle(e, "{class_obj['name']}.{method_name}");
            }}
            """
            
        class_obj["methods"].append(f"{method_signature}\n{final_method_content}\n}}")
        
    def __resolve_subpackage(self):
        """find subpackage name (if exists)"""
        self.subpackage = ""
        if paths[self.project.name]['main'] in self.schema_data['path']:
            path_tail = self.schema_data['path'].split(paths[self.project.name]['main'])[-1]
            if "/" in path_tail:
                # remove the last segment
                path_tail = path_tail[:path_tail.rfind('/')]
                self.subpackage = "." + path_tail.replace('/', '.')
    
    def __resolve_imports(self):
        """resolve imports for the schema"""
        self.imports = [
            "import org.graalvm.polyglot.Value;",
            "import org.graalvm.polyglot.PolyglotException;",
            f"import org.apache.{self.project.formatted_name}.ContextInitializer;",
            f"import org.apache.{self.project.formatted_name}.ExceptionHandler;",
            f"import org.apache.{self.project.formatted_name}.IntegrationUtils;"
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
            "".join(_class['fields']),
            "".join(_class['methods']),
            _class['sync'].get_body() if _class['sync'] else "",
            _class['revsync'].get_body() if _class['revsync'] else "",
            "".join([
                self.__get_class_body(nested_class) for nested_class in _class['nests']
            ]),
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
