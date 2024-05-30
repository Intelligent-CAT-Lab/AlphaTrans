import argparse
import os
import subprocess
import json
import keyword
import xml.etree.ElementTree as ET
 
from utils import default_type_value, write_to_file, get_destination_path, type_handling
from constants import *


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

        self.__initialize_project()
                
    def __initialize_project(self):
        """       
        Copy original project to glue_code directory
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

        # if pom.xml existed, write it back
        if pom_contents:
            with open(f"{self.glue_dir}/pom.xml", "w") as f:
                f.write(pom_contents)
        
        # IntegrationUtils.java
        with open(f"{self.script_dir}/misc/IntegrationUtils.java") as f:
            write_to_file(
                get_destination_path(
                    self.name, 
                    "IntegrationUtils", 
                    self.glue_dir, 
                    path_to_main=paths[self.name]['main']
                ), 
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
        
    def derive_compositional_tests(self, components: dict[str, dict[str, list[str]]]):
        """
        Derive compositional tests for the given components.
        components is a dictionary with the following structure:
        {
            "schema_name": {
                "class_name": ["method_name"]
            }
        }
        """
        return CompositionalTest(self, components)
            
        
class CompositionalTest:
    """
    A compositional test for a given project
    on the given components.
    """
    
    def __init__(self, project: Project, components: dict[str, dict[str, list[str]]]):
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
        
        # log of files to be written
        # { file_name: { original_content: str, new_content: str }}
        self.scheduled_writes = dict()
        
        # set the schemas to process
        self.__set_schemas_to_process(list(components.keys()))
        
        for schema in self.schemas_to_process:
            with open(f'{self.schema_dir}/{self.name}/{schema}') as f:
                schema_data = json.load(f)
                
            schema_object = Schema(schema, self.project, schema_data)
            
            # get the classes to process
            if schema not in components or not components[schema]:
                # Process all classes if no classes are provided
                # or no schema was provided to begin with
                classes_to_process = list(schema_data['classes'].keys())
            else:
                classes_to_process = []
                for _class in components[schema]:
                    if _class not in schema_data['classes']:
                        raise ValueError(f"Class {_class} not found in schema {schema}!")
                    classes_to_process.append(_class)
                    
            for _class in schema_data['classes']:
                if _class not in classes_to_process or schema_data['classes'][_class]['is_interface']:
                    # don't process this class if it's not in the list
                    # or if it's an interface
                    schema_object.add_class_body("".join(schema_data['classes'][_class]['body']))
                
                # get the methods to process
                if schema not in components or _class not in components[schema] or not components[schema][_class]:
                    # Process all methods if no methods are provided
                    # or no class or schema was provided to begin with
                    methods_to_process = list(schema_data['classes'][_class]['methods'].keys())
                else:
                    methods_to_process = []
                    
                    _available_methods = []
                    for _method in schema_data['classes'][_class]['methods']:
                        _is_constructor = schema_data['classes'][_class]['methods'][_method]['is_constructor']
                        _method_name = _method.split(':', 1)[1].strip() if not _is_constructor else "__init__"
                        
                        _available_methods.append((_method, _method_name))
                    
                    for _method in components[schema][_class]:
                        for m in _available_methods:
                            if m[1] == _method:
                                methods_to_process.append(m[0])
                                break
                        else:
                            raise ValueError(f"Method {_method} not found in class {_class} of schema {schema}!")
                    
                schema_object.add_class(_class, schema_data['classes'][_class], methods_to_process)
                
                # write the schema back
                self.__log_write(
                    get_destination_path(
                        schema_data['path'],
                        schema.split('.')[-2],
                        self.project.glue_dir,
                        is_full_path=True
                    ),
                    schema_object.get_body()
                )
        
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
            if not self.scheduled_writes[file_name]["original_content"]:
                with open(file_name) as f:
                    self.scheduled_writes[file_name]["original_content"] = f.read()
                    
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
        
    def __set_schemas_to_process(self, schemas_to_process: list[str] = None):
        """
        Set up the schemas to process for the project.
        If no schemas are provided, all schemas in the project will be processed.
        """   
        project_schemas = [file_name for file_name in os.listdir(f'{self.project.schema_dir}/{self.project.name}') if (
            'src.test' not in file_name and # ignore test schemas
            not file_name.endswith('_python_partial.json') # ignore partial schemas
        )]
        
        if not schemas_to_process:
            self.schemas_to_process = project_schemas
        else:
            self.schemas_to_process = []
            for schema in schemas_to_process:
                mathing_schemas = [s for s in project_schemas if s.endswith(f'.{schema}.json')]
                if not mathing_schemas:
                    raise ValueError(f"Schema for {schema} not found!")
                self.schemas_to_process.extend(mathing_schemas)
                
        self.__add_schema_dependent_files()

    def __add_schema_dependent_files(self):
        # Add ContextInitializer.java
        ctx_mappings, ctx_imports = self.__make_ctx_mappings()
        with open(f"{self.script_dir}/misc/ContextInitializer.java") as f:
            self.__log_write(
                get_destination_path(
                    self.name, 
                    "ContextInitializer", 
                    self.glue_dir,
                    path_to_main=paths[self.name]['main']
                ), 
                f.read().format(
                    project = f"org.apache.{self.formatted_name}",
                    imports = ctx_imports,
                    code_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.name}/src/{paths[self.name]['main'].replace('/java/', '/')}",
                    package_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{self.name}/",
                    mappings = ctx_mappings                
                )
            )
            
        # Add ExceptionHandler.java
        exp_mappings, exp_imports = self.__make_exp_mappings()
        with open(f"{self.script_dir}/misc/ExceptionHandler.java") as f:
            self.__log_write(
                get_destination_path(
                    self.name, 
                    "ExceptionHandler", 
                    self.glue_dir, 
                    path_to_main=paths[self.name]['main']
                ), 
                f.read().format(
                    project = f"org.apache.{self.formatted_name}",
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
        if paths[self.name]['main'] in schema_data['path']:
            path_tail = schema_data['path'].split(paths[self.name]['main'])[-1]
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
        try:
            subprocess.run(
                ['mvn', 'clean', 'test', '-Drat.skip', '-q'],
                cwd=self.project.glue_dir,
                # stderr=subprocess.DEVNULL,
                # stdout=subprocess.DEVNULL,
                check=True
            )
        except Exception:
            raise RuntimeError(f"Error running compositional test.")

class SyncMethod:
    """
    A class to manage the sync and revsync methods.
    """
    
    def __init__(self, class_name: str, reverse: bool = False):
        self.class_name = class_name
        self.reverse = reverse
        self.fields = []
        
    def add_field(self, field_name: str, field_schema_data: dict):
        field_name = field_name.split(':')[1].strip()
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
            private void {method_name}() {{
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
        
        # count of unclosed brackets due to class definitions
        self.__unclosed_brackets = 0
        
    def add_class(self, class_name: str, class_schema_data: dict, methods_to_process: list[str]):
        # create the class declaration
        with open(self.schema_data['path'], 'r') as f:
            lst = f.readlines()
        class_declaration = lst[class_schema_data['start']-1:class_schema_data['end']]
        
        class_obj = {
            "name": class_name,
            "declaration": class_declaration,
            "fields": [],
            "unitialized_fields": [],
            "methods": [],
            "sync": SyncMethod(class_name),
            "revsync": SyncMethod(class_name, reverse=True)
        }
        
        for _field in class_schema_data['fields']:
            self.__add_field_to_class(class_obj, _field, class_schema_data['fields'][_field])
            
        for _method in class_schema_data['methods']:
            if _method in methods_to_process:
                self.__add_method_to_class(class_obj, _method, class_schema_data['methods'][_method])
            else:
                self.__add_method_to_class(class_obj, _method, class_schema_data['methods'][_method], dont_process=True)     
        
        # add graal attributes
        python_file_dir = self.subpackage.replace('.', '/')
        python_file_dir = python_file_dir[:-1] if not python_file_dir else python_file_dir
        current_file_name = self.schema_data["path"].split('/')[-1].split('.')[0]
        python_file = f'{python_file_dir}/{current_file_name}.py'
        
        class_obj["fields"].extend([
            f"private static Value clz = ContextInitializer.getPythonClass(\"{python_file}\", \"{class_name}\");",
            "private Value obj;"
        ])

        # add Value constructor
        class_obj["methods"].append(f"""
            public {class_name}(Value obj) {{
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
        class_obj["methods"].append(f"public {class_name}() {{this.obj = clz.newInstance();}}")
        
    def add_class_body(self, class_name: str, class_schema_data: dict):
        """
        Directly add the body of a class to the schema
        without any processing.
        """
        class_body = []
        
        # create the class declaration
        with open(self.schema_data['path'], 'r') as f:
            lst = f.readlines()
        class_declaration = lst[class_schema_data['start']-1:class_schema_data['end']]
        class_body.append(class_declaration)
    
        for _field in class_schema_data['fields']:
            field_body = "".join(class_schema_data['fields'][_field]['body'])
            class_body.append(field_body)            
            
        for _method in class_schema_data['methods']:
            method_body = "".join(class_schema_data['methods'][_method]['body'])
            class_body.append(method_body)
            
        self.__classes.append("".join(class_body))
        
    def __add_field_to_class(self, class_obj: dict, field_name: str, field_schema_data: dict):
        field_name = field_name.split(':')[1].strip()
        field_type = field_schema_data['types'][0][0]
        field_body = "".join(field_schema_data['body'])
        
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
        
    def __add_method_to_class(self, class_obj: dict, method_name: str, method_schema_data: dict, dont_process: bool = False):
        method_body = "".join(method_schema_data['body'])
        # check if the method is not implemented
        if method_body.strip()[-1] != '}':
            # add a semi-colon if not present
            if method_body.strip()[-1] != ';':
                method_body += ';'
            
            class_obj["methods"].append(method_body)
            return
        
        # if method is not to be processed, add it directly
        if dont_process:
            class_obj["methods"].append(method_body)
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
            
        method_signature = method_body[:method_body.find('{')+1]
        method_content = method_body[method_body.find('{')+1:method_body.rfind('}')]
        
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
            
        args_buildup = ", ".join(method_schema_data['parameters'])
        
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
            _class['sync'].get_body(),
            _class['revsync'].get_body()    
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

# def main(args):
   
#     for schema in schemas:
#         with open(f'data/schemas/{args.project_name}/{schema}') as f:
#             data = json.load(f)
        
#         # dict with the mapping { class: <method>}
#         methods_under_test = {}
        
#         for _class in data['classes']:
#             if _class in data['classes'][_class]['extends']:
#                 # This will take care of the super class constructor when
#                 # the super class is defined in the same file
                
#                 # add empty constructor for super class
#                 final_glue_code += f"    public {_class}() {{\n"
                
#                 # initialize all uninitialized fields inside the constructor
#                 for _field in unitialized_fields:
#                     field_name = _field.split(':')[1].strip()
#                     field_type = data['classes'][_class]['fields'][_field]['types'][0][0]
                    
#                     final_glue_code += f"        {field_name} = {default_type_value[field_type]};\n"
                    
#                 final_glue_code += "    }\n"                
            


#             for _method in data['classes'][_class]['methods']:
#                 ...
                    
#             # add nested classes
#             if not data['classes'][_class]["nests"]:
#                 final_glue_code += "}\n"
#             else:
#                 unclosed_brace_count += 1
                    
#             final_glue_code += "}\n" * unclosed_brace_count
            
#             # If the super class is not defined in the same file, we handle it separately
#             # note that a class can only extend at most one class
            
#             # We have assumed (for now) that the parent class will have a file of its own
#             if data['classes'][_class]['extends']:
#                 super_class = data['classes'][_class]['extends'][0]
#                 if super_class not in data['classes']:
#                     # find the schema where the super class is defined
#                     super_schema = [s for s in schemas if s.endswith(f'.{super_class}.json')][0]
                    
#                     # get the path to the super class
#                     with open(f'data/schemas/{args.project_name}/{super_schema}') as f:
#                         super_data = json.load(f)
                        
#                     super_file_path = get_destination_path(super_data["path"], super_class, OUTPUT_DIR, is_full_path=True)
                    
#                     # read the super class file
#                     with open(super_file_path) as f:
#                         super_class_file = f.read()
                        
#                     # add the empty constructor for the super class
#                     unitialized_fields = []
#                     for _field in super_data['classes'][super_class]['fields']:
#                         line = "".join(super_data['classes'][super_class]['fields'][_field]['body'])
                        
#                         if '=' not in line:
#                             unitialized_fields.append(_field)
                            
#                     new_constructor_code = f"    public {super_class}() {{\n"
                    
#                     # initialize all uninitialized fields inside the constructor
#                     for _field in unitialized_fields:
#                         field_name = _field.split(':')[1].strip()
#                         field_type = super_data['classes'][super_class]['fields'][_field]['types'][0][0]
                        
#                         new_constructor_code += f"        {field_name} = {default_type_value[field_type]};\n"
                        
#                     new_constructor_code += "    }\n"
                    
#                     # note: parent class has a file of its own
                    
#                     # add the new constructor to the super class file
#                     super_class_file = super_class_file[:super_class_file.rfind('}')]
#                     super_class_file += new_constructor_code
#                     super_class_file += "}\n"
                    
#                     # write the super class file back
#                     write_to_file(super_file_path, super_class_file)

#             class_name = schema.split('.')[-2] # get the class name preceding '.json'
#             output_file = get_destination_path(data["path"], class_name, OUTPUT_DIR, is_full_path=True)
#             write_to_file(output_file, final_glue_code)
            
#             # run the test
#             for mut in methods_under_test[_class]:
#                 class_name = schema.split('.')[-2]
#                 print("Method currently under test:", f"{class_name}#{mut}")
#                 try:
#                     subprocess.run(['mvn', 'clean', 'test', '-Drat.skip', '-q'], cwd=f"{OUTPUT_DIR}/{args.project_name}/", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)
#                 except Exception as e:
#                     print(f"Error running test for {args.project_name}.")
#                     continue

#                 # get the test results
#                 failed_tests = []
                
#                 # first get all XML files in the target/surefire-reports directory
#                 for report_file in [f for f in os.listdir(f"{OUTPUT_DIR}/{args.project_name}/target/surefire-reports/") if f.endswith('.xml')]:
#                     test_class_name = report_file.split('.')[0]
#                     root = ET.parse(f"{OUTPUT_DIR}/{args.project_name}/target/surefire-reports/{report_file}").getroot()
                    
#                     # get the <testsuite> element
#                     if not  root.find('testsuite'):
#                         continue

#                     testsuite = root.find('testsuite')
                    
#                     # iterate over all testcase elements
#                     for testcase in testsuite.findall('testcase'):
#                         # does the testcase have an error element?
#                         error = testcase.find('error')
                        
#                         if error is not None:
#                             failed_tests.append(f"{test_class_name}#{testcase.get('name')}")
                            
#                 if failed_tests:
#                     print("Test failures were found.")
#                     print(*failed_tests, sep='\n')
#                 else:
#                     print("All tests passed!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Compositional Testing.')
    parser.add_argument('--project', type=str, dest='project_name', help='<Required> name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', nargs="+", help='list of class name(s)', required=False)
    parser.add_argument('--method', type=str, dest='method_name', help='name of the method', required=False)
    args = parser.parse_args()
    
    project = Project(args.project_name)
    test = project.derive_compositional_tests({
        args.class_name[0]: {
            args.class_name[0]: [args.method_name]
        }
    })
    test.run()
