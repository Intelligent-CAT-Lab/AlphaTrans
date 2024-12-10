import json
import os
from src.icl.icl_ranking import rank_icl


class PromptGenerator:
        
    def __init__(self, is_feedback, args, fragment_details, feedback='', use_icl_pool=False):
        self.is_feedback = is_feedback
        self.args = args
        self.prompt = ''
        self.feedback = feedback
        self.prompt_status = 'success'
        self.use_icl_pool = use_icl_pool
        self.fragment_details = fragment_details

        self.meta_data = {
                            'deepseek-coder-33b-instruct-persona': 'You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.',
                            'gpt-4o-2024-11-20-persona': '',
                            'llama-3-1-405b-instruct-fp8-persona': '',
                            'Qwen2.5-Coder-32B-Instruct-persona': '',
                            'icl': {
                                'field': 'Java code:\n```\npublic class Calculator {\n    public int x;\n}\n```\n\nPartial Python translation:\n```\nclass Calculator:\n    x: int = \n```\n\nPython field translation:\n```\n    x: int = 0\n```',
                                'method': 'Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```',
                                'static_initializer': 'Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```',
                                'feedback': "Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```" + "\n\nIncorrect Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        return a + c\n```\n\nExecution feedback:\n```\n  File \"script.py\", line 5, in add\n    return a + c\nNameError: name 'c' is not defined\n```\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```",
                            }
                        }

        self.assert_map = json.load(open('data/type_resolution/assert_map.json', 'r'))
        
        self.load_fragment(fragment_details)
        self.construct_adaptive_icl()
        self.build_base_prompt()
    
    def build_base_prompt(self):
        # add persona
        self.prompt += self.meta_data[f'{self.args.model_name}-persona']
        
        self.double_line_break()

        # add in-context learning example
        self.prompt += self.adaptive_icl

        self.double_line_break()

        # add instruction
        self.add_instruction()

        self.double_line_break()

        # add source code
        self.add_source_code()

        self.double_line_break()

        if self.is_feedback:
            self.add_incorrect_translation()
            self.double_line_break()
            self.add_feedback()
            self.double_line_break()

        # add partial translation
        self.add_partial_translation()

        self.double_line_break()

        # add target translation
        self.add_target_translation()

    def construct_adaptive_icl(self):
        used_assertions = []
        for source_assert in self.assert_map:
            if source_assert in self.source_fragment_body:
                used_assertions.append(source_assert)

        source_statements = ''
        target_statements = ''
        for source_assert in self.assert_map:
            if source_assert not in used_assertions:
                continue
            for i in range(2):
                source_statements += self.assert_map[source_assert][i]['java'] + ';\n        '
                target_statements += 'self.' + self.assert_map[source_assert][i]['python'] + '\n        '

        if self.is_feedback:
            test_icl = "Java code:\n```\npublic class TestClass {\n    @Test\n    public void testMethod(self) {\n        List<String> inputList = Arrays.asList(\"apple\", \"banana\", \"cherry\");\n        assertEquals(\"inputList size does not match expected size = 3\", 3, inputList.size());\n    " + "}\n}\n```\n\nIncorrect Python translation:\n```\nclass TestClass(unittest.TestCase):\n    def testMethod(self) -> None:\n        inputList = [\"apple\", \"banana\", \"cherry\"]\n        self.assertEqual(\"inputList size does not match expected size = 3\", 3, len(inputList))\n```\n\nExecution feedback:\n```\n  File \"TestClass.py\", line 4, in testMethod\n    self.assertEqual(\"inputList size does not match expected size = 3\", 3, len(inputList))\nAssertionError: 'inputList size does not match expected size = 3' != 3 : 2\n```\n\nPartial Python translation:\n```\nclass TestClass(unittest.TestCase):\n    def testMethod(self) -> None:\n        pass\n```\n\nPython method translation:\n```\n    def testMethod(self) -> None:\n        inputList = [\"apple\", \"banana\", \"cherry\"]\n        self.assertEqual(3, len(inputList), \"inputList size does not match expected size = 3\")\n```"
            test_icl = test_icl.replace('self.pytest.', 'pytest.')
        else:
            test_icl = 'Java code:\n```\npublic class TestClass {\n    @Test\n    public void testMethod(self) {\n        ' + source_statements.rstrip() + '\n    ' + '}\n}\n```\n\nPartial Python translation:\n```\nclass TestClass(unittest.TestCase):\n    def testMethod(self) -> None:\n        pass\n```\n\nPython method translation:\n```\n    def testMethod(self) -> None:\n        ' + target_statements.rstrip() + '\n```\n'
            test_icl = test_icl.replace('self.pytest.', 'pytest.')

        if self.is_feedback:
            if used_assertions:
                self.adaptive_icl = test_icl
            else:
                self.adaptive_icl = self.meta_data['icl']['feedback']
        else:
            # if not self.use_icl_pool or self.fragment_details['fragment_type'] != 'method':
            if used_assertions:
                self.adaptive_icl = test_icl
            else:
                self.adaptive_icl = self.meta_data['icl'][self.fragment_type]
            # else:
            #     matched_icl = rank_icl(self.args.project_name, 1, 'library_api', self.args.suffix, f"{self.fragment_details['schema_name']}|{self.fragment_details['class_name']}|{self.fragment_details['fragment_name']}")
            #     if len(matched_icl) == 0:
            #         if used_assertions:
            #             self.adaptive_icl = test_icl
            #         else:
            #             self.adaptive_icl = self.meta_data['icl'][self.fragment_type]
                    
            #         return
                
            #     source_code = '\n'.join(matched_icl[0]['source_code'])
            #     translation_signature = matched_icl[0]['target_signature']
            #     correct_translation = '\n'.join(matched_icl[0]['correct_translation'])
            #     self.adaptive_icl = f"Java code:\n```\n{source_code}\n```" + f"\n\nPartial Python translation:\n```\n{translation_signature}\n        pass\n```\n\nPython method translation:\n```\n{correct_translation}\n```"


    def load_fragment(self, fragment_details):
        self.schema_name = fragment_details['schema_name']
        self.class_name = fragment_details['class_name']
        self.fragment_name = fragment_details['fragment_name']
        self.fragment_actual_name = self.fragment_name.split(':')[1]
        self.fragment_type = fragment_details['fragment_type']
        self.is_test_method = fragment_details['is_test_method']

        self.schema_data = {}
        with open(f'{self.args.translation_dir}/{self.schema_name}_python_partial.json', 'r') as f:
            self.schema_data = json.load(f)
        
        self.fragment_dict = self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]

        # add source fragment body
        self.source_fragment_body = '\n'.join([f"    @{x}" for x in self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['annotations'] if x.startswith('Test')]) + '\n' if self.fragment_type == 'method' else ''
        self.source_fragment_body += ''.join(self.fragment_dict['body'])

        # add source class fields for reference
        self.source_class_dependent_fields = ''
        for field in self.schema_data['classes'][self.class_name]['fields']:
            if field == self.fragment_name:
                continue
            if field.split(':')[1] in self.source_fragment_body:
                self.source_class_dependent_fields += ''.join(self.schema_data['classes'][self.class_name]['fields'][field]['body'])
                self.source_class_dependent_fields += '\n'

        self.source_fragment_code = f'class {self.class_name} {{\n{self.source_class_dependent_fields}\n{self.source_fragment_body}\n}}'

    def add_instruction(self):
        if self.is_feedback:
            self.prompt += f'### Instruction:\nBased on the feedback provided, identify the error in the following Python translation of the {self.fragment_type} and correct it. You only need to correct the \"{self.fragment_actual_name}\" {self.fragment_type}. All necessary dependencies are available in partial {self.args.to_lang} translation. Only complete the given \"{self.fragment_actual_name}\" method like the example above and do not add anything else in your response.'
        else:
            self.prompt += f'### Instruction:\nTranslate the following {self.args.from_lang} {self.fragment_type} to {self.args.to_lang} 3.10 like the example above. You only need to translate the \"{self.fragment_actual_name}\" {self.fragment_type}. All necessary dependencies are available in partial {self.args.to_lang} translation.'

    def add_source_code(self):
        self.prompt += f'{self.args.from_lang} code:\n```\n{self.source_fragment_code}\n```'

    def add_incorrect_translation(self):
        translation = '\n'.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['translation'])
        self.prompt += f'Incorrect {self.args.to_lang} translation:\n```\nclass {self.class_name}:\n{translation}\n```'

    def add_feedback(self):
        self.prompt += 'Execution feedback:\n```\n'
        self.prompt += self.feedback
        self.prompt += '\n```'

    def add_partial_translation(self):
        self.build_partial_translation()
        self.prompt += f'Partial {self.args.to_lang} translation:\n```\n{self.partial_translation}\n```'

    def build_partial_translation(self):
        self.partial_translation = '\n'.join(self.schema_data['python_imports'])
        self.partial_translation += '\n\n'

        # add inner and outer classes
        inner_outer_classes = self.schema_data['classes'][self.class_name]['nests'] + [self.schema_data['classes'][self.class_name]['nested_inside']]
        for inner_outer_class in inner_outer_classes:
            if 'new' in inner_outer_class or '{' in inner_outer_class or inner_outer_class == []:
                continue
            
            inner_outer_classes_py = [f"{self.schema_data['classes'][inner_outer_class]['python_class_declaration']}"]
            for field in self.schema_data['classes'][inner_outer_class]['fields']:
                if field.split(':')[1] in ''.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['body']):
                    field_translation = self.schema_data['classes'][inner_outer_class]['fields'][field]['translation']
                    inner_outer_classes_py.append('\n'.join(field_translation) if field_translation else ''.join(self.schema_data['classes'][inner_outer_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None'))
                    inner_outer_classes_py.append('\n')
            
            if len(inner_outer_classes_py) > 1:
                self.partial_translation += '\n'.join(inner_outer_classes_py) + '\n\n'

        # add necessary dependencies from imported classes
        dependencies = {}
        dependencies_path = f'data/dependencies/{self.args.project_name}/dependencies.json'
        if self.args.translate_evosuite:
            dependencies_path = f'data/dependencies_evosuite/{self.args.project_name}/dependencies.json'

        with open(dependencies_path, 'r') as f:
            dependencies = json.load(f)

        imported_classes = []
        if self.class_name in dependencies:
            imported_classes = dependencies[self.class_name]

        for (dependenct_class_name, dependent_class_path) in imported_classes:
            
            has_exceptional_import = False
            for exceptional_import in ['commons.io', 'commons.logging', 'opentest4j', 'com.google', 'org.evosuite', 'scaffolding']:
                if exceptional_import in dependent_class_path:
                    has_exceptional_import = True
                    break

                if 'joda.convert' in dependent_class_path and self.args.project_name == 'joda-money': # resolving these dependencies later
                    has_exceptional_import = True
                    break
            
            if has_exceptional_import:
                continue

            imported_class_path = self.get_dependency_path(dependent_class_path, self.args.project_name)
            
            imported_class_data = {}
            with open(f'{self.args.translation_dir}/{self.args.project_name}.{imported_class_path}_python_partial.json', 'r') as f:
                imported_class_data = json.load(f)

            imported_classes = [f'{imported_class_data["classes"][dependenct_class_name]["python_class_declaration"]}']

            for field in imported_class_data['classes'][dependenct_class_name]['fields']:
                if field.split(':')[1] in ''.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['body']):
                    field_translation = imported_class_data['classes'][dependenct_class_name]['fields'][field]['translation']
                    if field_translation:
                        imported_classes += ['\n'.join(field_translation)]
                    else:
                        imported_classes += ['\n'.join(imported_class_data['classes'][dependenct_class_name]['fields'][field]['partial_translation']).replace('<placeholder>', 'None')]
            
            if len(imported_classes) > 1:
                self.partial_translation += '\n'.join(imported_classes) + '\n'

        # include fields of superclass
        for super_class in self.schema_data['classes'][self.class_name]['extends']:            
            super_class_schema = ''
            for schema_file in os.listdir(self.args.translation_dir):
                if f'.{super_class}_python_partial.json' in schema_file:
                    super_class_schema = schema_file
                    break
            
            if super_class_schema == '':
                continue

            super_class_data = {}
            with open(f'{self.args.translation_dir}/{super_class_schema}', 'r') as f:
                super_class_data = json.load(f)

            if f'class {super_class}:' in self.partial_translation or f'class {super_class}(' in self.partial_translation:
                continue

            super_class_declaration = [super_class_data['classes'][super_class]['python_class_declaration']]
            for field in super_class_data['classes'][super_class]['fields']:
                if field.split(':')[1] in ''.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['body']):
                    field_translation = super_class_data['classes'][super_class]['fields'][field]['translation']
                    super_class_declaration.append('\n'.join(field_translation) if field_translation else ''.join(super_class_data['classes'][super_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None'))
                    super_class_declaration.append('\n')
            
            if len(super_class_declaration) > 1:
                self.partial_translation += '\n'.join(super_class_declaration) + '\n\n'

        # add the fragment partial translation
        main_class_partial_translation = self.schema_data['classes'][self.class_name]['python_class_declaration']

        if '<placeholder>' not in ''.join(self.fragment_dict['partial_translation']):
            self.prompt_status = 'translated'
        
        # add related fields of the main class 
        for field in self.schema_data['classes'][self.class_name]['fields']:
            if field.split(':')[1] == self.fragment_actual_name and self.fragment_type == 'field':
                continue
            if field.split(':')[1] in ''.join(''.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['body'])):
                field_translation = self.schema_data['classes'][self.class_name]['fields'][field]['translation']
                main_class_partial_translation += '\n'.join(field_translation) if field_translation else ''.join(self.schema_data['classes'][self.class_name]['fields'][field]['partial_translation']).replace('<placeholder>', 'None')
                main_class_partial_translation += '\n\n'

        # add related methods of the main class
        if self.fragment_type == 'method':

            if len(self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['calls']) != 0 and self.args.include_call_graph:

                out_of_file_dependencies = []
                out_of_class_dependencies = []
                for callee_schema, callee_class, callee_method in self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['calls']:

                    if callee_schema == 'library':
                        continue

                    callee_schema_data = {}
                    with open(f'{self.args.translation_dir}/{callee_schema}_python_partial.json', 'r') as f:
                        callee_schema_data = json.load(f)
                    
                    if ':' not in callee_method:
                        continue

                    if callee_schema != self.schema_name.replace('_python_partial.json', ''):
                        out_of_file_dependencies.append((callee_schema, callee_class, callee_method))
                        continue

                    if callee_class != self.class_name:
                        out_of_class_dependencies.append((callee_schema, callee_class, callee_method))
                        continue

                    if self.args.include_implementation:
                        method_translation = callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']
                        callee_partial_translation = '\n'.join(method_translation).rstrip() if method_translation else ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()
                    else:
                        callee_partial_translation = ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()

                    main_class_partial_translation += f"{callee_partial_translation}\n\n"

                main_class_partial_translation += ''.join(self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['partial_translation']).rstrip()

                if len(out_of_file_dependencies) != 0:
                    ordered_out_of_file_dependencies = {}
                    for callee_schema, callee_class, callee_method in out_of_file_dependencies:
                        ordered_out_of_file_dependencies.setdefault(callee_schema, [])
                        ordered_out_of_file_dependencies[callee_schema].append((callee_class, callee_method))

                    for callee_schema in ordered_out_of_file_dependencies:
                        for callee_class, callee_method in ordered_out_of_file_dependencies[callee_schema]:

                            callee_schema_data = {}
                            with open(f'{self.args.translation_dir}/{callee_schema}_python_partial.json', 'r') as f:
                                callee_schema_data = json.load(f)
                            
                            if callee_schema_data['classes'][callee_class]['python_class_declaration'] not in self.partial_translation:
                                self.partial_translation += f"{callee_schema_data['classes'][callee_class]['python_class_declaration']}"
                                for field in callee_schema_data['classes'][callee_class]['fields']:
                                    field_translation = callee_schema_data['classes'][callee_class]['fields'][field]['translation']
                                    self.partial_translation += '\n'.join(field_translation) if field_translation else ''.join(callee_schema_data['classes'][callee_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None')
                                    self.partial_translation += '\n'
                            
                            self.partial_translation += '\n'

                            if self.args.include_implementation:
                                callee_method_translation = callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']
                                self.partial_translation += '\n'.join(callee_method_translation).rstrip() if callee_method_translation else ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()
                            else:
                                self.partial_translation += ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()
                            
                            self.partial_translation += '\n\n'

                if len(out_of_class_dependencies) != 0:
                    ordered_out_of_file_dependencies = {}
                    for callee_schema, callee_class, callee_method in out_of_class_dependencies:
                        ordered_out_of_file_dependencies.setdefault(callee_schema, [])
                        ordered_out_of_file_dependencies[callee_schema].append((callee_class, callee_method))

                    for callee_schema in ordered_out_of_file_dependencies:
                        for callee_class, callee_method in ordered_out_of_file_dependencies[callee_schema]:
                            callee_schema_data = {}
                            with open(f'{self.args.translation_dir}/{callee_schema}_python_partial.json', 'r') as f:
                                callee_schema_data = json.load(f)
                            
                            self.partial_translation += f"{callee_schema_data['classes'][callee_class]['python_class_declaration']}"
                            for field in callee_schema_data['classes'][callee_class]['fields']:
                                field_translation = callee_schema_data['classes'][callee_class]['fields'][field]['translation']
                                self.partial_translation += '\n'.join(field_translation) + '\n' if field_translation else ''.join(callee_schema_data['classes'][callee_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'
                            
                            if self.args.include_implementation:
                                callee_method_translation = callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']
                                self.partial_translation += '\n'.join(callee_method_translation) if callee_method_translation else ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                            else:
                                self.partial_translation += ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                            
                            self.partial_translation += '\n\n'
                        
                main_class_partial_translation += '\n'
                
            else:
                main_class_partial_translation += ''.join(self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['partial_translation']).rstrip()
                main_class_partial_translation += '\n'
            
        else:
            for method in self.schema_data['classes'][self.class_name]['methods']:
                if method.split(':')[1] in ''.join(''.join(self.schema_data['classes'][self.class_name][f'{self.fragment_type}s'][self.fragment_name]['body'])):
                    method_translation = self.schema_data['classes'][self.class_name]['methods'][method]['translation']
                    if self.args.include_implementation:
                        main_class_partial_translation += '\n'.join(method_translation) if method_translation else ''.join(self.schema_data['classes'][self.class_name]['methods'][method]['partial_translation']).replace('<placeholder>', 'None')
                    else:
                        main_class_partial_translation += ''.join(self.schema_data['classes'][self.class_name]['methods'][method]['partial_translation']).replace('<placeholder>', 'None')
                    main_class_partial_translation += '\n\n'
        
        if self.fragment_type == 'field':
            main_class_partial_translation += ''.join(self.fragment_dict['partial_translation']).replace('<placeholder>', '') + '\n'
        elif self.fragment_type == 'static_initializer':
            main_class_partial_translation += '    @staticmethod\n    def run_static_init():\n        pass'
        
        self.partial_translation += main_class_partial_translation

    def add_target_translation(self):
        self.prompt += '### Response:\n'
        if self.fragment_type == 'field':
            self.prompt += f'Python field translation:\n```\n'
        
        elif self.fragment_type == 'method':
            self.prompt += f'Python method translation:\n```\n'
            self.prompt += ''.join(self.schema_data['classes'][self.class_name]['methods'][self.fragment_name]['partial_translation']).rstrip().replace('    pass', '    ')
        
        elif self.fragment_type == 'static_initializer':
            self.prompt += f'Python method translation:\n```\n'
            self.prompt += '    @staticmethod\n    def run_static_init():\n        '        

    def single_line_break(self):
        self.prompt += '\n'
    
    def double_line_break(self):
        self.prompt += '\n\n'

    def get_dependency_path(self, dependent_class, project_name):
        if os.path.exists(f'java_projects/cleaned_final_projects{self.args.suffix}/{project_name}/src/main/java/' + dependent_class.replace('.', '/') + '.java'):
            return f'src.main.{dependent_class}'
        elif os.path.exists(f'java_projects/cleaned_final_projects{self.args.suffix}/{project_name}/src/test/java/' + dependent_class.replace('.', '/') + '.java'):
            return f'src.test.{dependent_class}'
        else:
            return f'src.main.{dependent_class}'

    def generate_prompt(self):
        self.prompt = self.prompt.replace('\u0000', '')
        return self.prompt

