import os
import re
import sys

source_code_path = '.'

standard_java_packages = ['java.util', 'java.text', 'java.lang','java.io','java.nio','java.net','java.time', 'java.math', 'org.junit.', 'org.opentest4j', 'junit.', 'org.slf4j.Logger']

method_regex = (
    r'\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(<[\w\s,?<>]+>\s*)?'
    r'[\w<>\[\],\s?]+[\w\s,<>.\[\]?]*\s+'
    r'(\w+)\s*'
    r'\(\s*([\w\s,<>\[\].?]*?)\s*\)\s*'
    r'(throws\s+[\w.<>,\s]+)?\s*'
    r'\{'
)
abstract_method_regex = (
    r'\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(public|private|protected|static|synchronized|final|abstract|native|transient|volatile|strictfp)?\s*'
    r'(<[\w\s,?<>]+>\s*)?'
    r'[\w<>\[\],\s?]+[\w\s,<>.\[\]?]*\s+'
    r'(\w+)\s*'
    r'\(\s*([\w\s,<>\[\].?]*?)\s*\)\s*'
    r'(throws\s+[\w.<>,\s]+)?\s*'
    r';'
)
class_regex = (
    r'\s*'
    r'(public|private|protected|static|final|abstract)?\s*'
    r'(public|private|protected|static|final|abstract)?\s*'
    r'(public|private|protected|static|final|abstract)?\s*'
    r'class\s+'
    r'(\w+(\s*<[\w\s,<>]+>)?)\s*'
    r'(\s+extends\s+[\w\s,<>]+)?'
    r'(\s+implements\s+[\w\s,<>]+)?'
    r'\s*\{'
)
max_multiline = 10

def identify_current_project_packages(source_code_path):
    packages = set()
    file_count = 0
    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_count += 1
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for line in lines:
                    package_match = re.match(r'package\s+([\w.]+);', line.strip())
                    if package_match:
                        packages.add(package_match.group(1))
    package_count = len(packages)
    print("Found", file_count, "Java files across", package_count, "package(s).")
    return packages


def identify_override_methods(source_code_path):
    override_methods = set()
    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                if "/java/" not in file_path:
                    continue
                class_path = file_path.split("/java/")[1].split(".")[0].replace("/", ".")
                class_base_path = class_path.split("$")[0]


                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    outer_class_brace_level = 0
                    inner_class_brace_level = 0
                    inside_outer_class = False
                    inside_inner_class = False
                    skip_lines = 0
                    match_some_header = False

                    for i, line in enumerate(lines):
                        multiline = line
                        match_some_header = False
                        if skip_lines > 0:
                            skip_lines -= 1
                            continue
                        for j in range(max_multiline):
                            if j > 0 and (i + j) < len(lines):
                                multiline += lines[i + j]
                            if re.match(class_regex, multiline.strip()) and inside_outer_class:
                                inner_class_match = re.match(class_regex, multiline.strip())
                                if inner_class_match:
                                    inside_inner_class = True
                                    skip_lines += j
                                    match_some_header = True
                                    inner_class_name = inner_class_match.group(4)
                                    class_path += ('$' + inner_class_name.split("<")[0])         
                            if re.match(class_regex, multiline.strip()) and (not inside_outer_class):
                                inside_outer_class = True
                                skip_lines += j
                                match_some_header = True
                            if match_some_header:
                                break
                        
                        if line.strip() == "@Override":
                            next_lines = ''
                            next_line_num = i + 1
                            for k in range(max_multiline - 1):
                                next_lines += lines[next_line_num]
                                if (next_line_num + 1) >= len(lines):
                                    break
                                next_line_num += 1

                                method_match = re.match(
                                    method_regex,
                                    next_lines.strip()
                                )
                                if method_match:
                                    method_signature = method_match.group(5)
                                    full_method_name = class_base_path +\
                                        (("$" + class_path.split('$')[1]) if ('$' in class_path) else '') +\
                                        ":" + method_signature
                                    override_methods.add(full_method_name)
                                    break
                        
                        if not match_some_header:
                            multiline = line
                        
                        if inside_outer_class:
                            outer_class_brace_level += multiline.count('{')
                            outer_class_brace_level -= multiline.count('}')
                            if outer_class_brace_level == 0:
                                inside_outer_class = False
                        
                        if inside_inner_class:
                            inner_class_brace_level += multiline.count('{')
                            inner_class_brace_level -= multiline.count('}')
                            if inner_class_brace_level == 0:
                                inside_inner_class = False
                                class_path = class_path.split('$')[0]

    return override_methods


def identify_third_party_packages(source_code_path, current_project_packages):
    third_party_packages = set()
    third_party_exceptions = set()
    class_package_map = {}
    is_third_party_import = False
    trusted = set()
    untrusted = []

    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                project_specific_file_path = os.getcwd().split("/")[-1] + "/" + file_path.split("/", 1)[-1]
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for line in lines:
                    is_third_party_import = False
                    import_match = re.match(r'import\s+(static\s+)?([\w.]+(\.\*)?);', line.strip())
                    if import_match:
                        imported = import_match.group(2)
                        short_class = imported.split('.')[-1]
                        class_package_map[short_class] = imported
                        if not any(imported.startswith(std) for std in standard_java_packages):
                            if not any (imported.startswith(pkg) for pkg in current_project_packages):
                                if imported.endswith("Exception"):
                                    third_party_exceptions.add(short_class)
                                is_third_party_import = True
                                third_party_packages.add(imported)
                        if is_third_party_import:
                            json_str = "{\"body\": \"" + line.split(";")[0].strip() + "\", \"path\": \"" + project_specific_file_path + "\"}"
                            untrusted.append(json_str)
                        else:
                            trusted.add(line.split(";")[0].strip())
    
    with open("trusted.txt", 'w') as f:
        for t in sorted(trusted):
            f.write(t + "\n")
    with open("untrusted.jsonl", 'w') as f:
        for u in sorted(untrusted):
            f.write(u + "\n")
    print("Recognized", len(class_package_map), "classes from source code")
    return class_package_map, third_party_packages, third_party_exceptions


def get_implemented_methods_and_child_classes_of_third_party_types(source_code_path, class_package_map, third_party_packages, third_party_exceptions):
    child_classes_of_third_party_types = set()
    implemented_methods = {}
    interface_implementation_map = {}
    abstract_method_map = {}
    methods_using_third_party_exceptions = {}
    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                if "/java/" not in file_path:
                    continue
                class_path = file_path.split("/java/")[1].split(".")[0].replace("/", ".")
                class_base_path = class_path.split("$")[0]
                full_method_name = None

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    implemented_methods[class_path] = []
                    abstract_method_map[class_path] = []
                    lines = f.readlines()
                    outer_class_brace_level = 0
                    inner_class_brace_level = 0
                    inside_outer_class = False
                    inside_inner_class = False
                    skip_lines = 0
                    match_some_header = False
                    

                    for i, line in enumerate(lines):
                        if skip_lines > 0:
                            skip_lines -= 1
                            continue
                        multiline = line
                        match_some_header = False
                        for j in range(max_multiline):
                            if j > 0 and (i + j) < len(lines):
                                multiline += lines[i + j]
                            
                            if re.match(class_regex, multiline.strip()) and inside_outer_class:
                                inner_class_match = re.match(class_regex, multiline.strip())
                                if inner_class_match:
                                    inside_inner_class = True
                                    skip_lines += j
                                    match_some_header = True
                                    inner_class_name = inner_class_match.group(4)
                                    class_path += ('$' + inner_class_name.split("<")[0])    
                                    implemented_methods[class_path] = []
                                    abstract_method_map[class_path] = []
                                    interfaces_implemented = inner_class_match.group(7).split("implements")[1].split(",") if inner_class_match.group(7) != None else []
                                    interfaces_implemented_cleaned = [interface.strip().split("<")[0] for interface in interfaces_implemented]
                                    classes_extended = inner_class_match.group(6).split("extends")[1].split(",") if inner_class_match.group(6) != None else []
                                    classes_extended_cleaned = [clazz.strip().split("<")[0] for clazz in classes_extended]
                                    for cleaned_interface in interfaces_implemented_cleaned:
                                        if cleaned_interface in class_package_map:
                                            if not class_path in interface_implementation_map:
                                                interface_implementation_map[class_path] = set()
                                            interface_implementation_map[class_path].add(class_package_map[cleaned_interface])
                                            if class_package_map[cleaned_interface] in third_party_packages:
                                                child_classes_of_third_party_types.add(class_path)
                                    for cleaned_class in classes_extended_cleaned:
                                        if cleaned_class in class_package_map:
                                            if class_package_map[cleaned_class] in third_party_packages:
                                                child_classes_of_third_party_types.add(class_path)     
                            
                            if re.match(class_regex, multiline.strip()) and (not inside_outer_class):
                                outer_class_match = re.match(class_regex, multiline.strip())
                                if outer_class_match:
                                    inside_outer_class = True
                                    skip_lines += j
                                    match_some_header = True
                                    interfaces_implemented = outer_class_match.group(7).split("implements")[1].split(",") if outer_class_match.group(7) != None else []
                                    interfaces_implemented_cleaned = [interface.strip().split("<")[0] for interface in interfaces_implemented]
                                    classes_extended = outer_class_match.group(6).split("extends")[1].split(",") if outer_class_match.group(6) != None else []
                                    classes_extended_cleaned = [clazz.strip().split("<")[0] for clazz in classes_extended]
                                    for cleaned_interface in interfaces_implemented_cleaned:
                                        if cleaned_interface in class_package_map:
                                            if not class_path in interface_implementation_map:
                                                interface_implementation_map[class_path] = set()
                                            interface_implementation_map[class_path].add(class_package_map[cleaned_interface])
                                            if class_package_map[cleaned_interface] in third_party_packages:
                                                child_classes_of_third_party_types.add(class_path)
                                    for cleaned_class in classes_extended_cleaned:
                                        if cleaned_class in class_package_map:
                                            if class_package_map[cleaned_class] in third_party_packages:
                                                child_classes_of_third_party_types.add(class_path)
                            
                            if match_some_header:
                                break
                        
                        multi_lines = ''
                        next_line_num = i
                        for k in range(max_multiline):
                            if next_line_num >= len(lines):
                                break
                            multi_lines += lines[next_line_num]
                            next_line_num += 1

                            method_match = re.match(
                                method_regex,
                                multi_lines.strip()
                            )
                            if method_match:
                                method_signature = method_match.group(5)
                                full_method_name = class_base_path +\
                                    (("$" + class_path.split('$')[1]) if ('$' in class_path) else '') +\
                                    ":" + method_signature
                                if not full_method_name in implemented_methods[class_path]:
                                    implemented_methods[class_path].append(full_method_name)
                                break
                            abstract_method_match = re.match(
                                abstract_method_regex,
                                multi_lines.strip()
                            )
                            if abstract_method_match:
                                abstract_method_signature = abstract_method_match.group(5)
                                full_abstract_method_name = class_base_path +\
                                    (("$" + class_path.split('$')[1]) if ('$' in class_path) else '') +\
                                    ":" + abstract_method_signature
                                if not full_abstract_method_name in abstract_method_map[class_path]:
                                    abstract_method_map[class_path].append(full_abstract_method_name)
                                break
                        
                        for ex in third_party_exceptions:
                            if (ex in line) and (full_method_name is not None):
                                if not (line.strip().startswith("*") or line.strip().startswith("//") or line.strip().startswith("/*")):
                                    if class_path in methods_using_third_party_exceptions:
                                        methods_using_third_party_exceptions[class_path].add(full_method_name)
                                    else:
                                        exs = set()
                                        exs.add(full_method_name)
                                        methods_using_third_party_exceptions[class_path] = exs                        
                        
                        if not match_some_header:
                            multiline = line
                        
                        if inside_outer_class:
                            outer_class_brace_level += multiline.count('{')
                            outer_class_brace_level -= multiline.count('}')
                            if outer_class_brace_level == 0:
                                inside_outer_class = False
                        
                        if inside_inner_class:
                            inner_class_brace_level += multiline.count('{')
                            inner_class_brace_level -= multiline.count('}')
                            if inner_class_brace_level == 0:
                                inside_inner_class = False
                                class_path = class_path.split('$')[0]

    print("child_classes_of_third_party_types:", child_classes_of_third_party_types)
    return child_classes_of_third_party_types, implemented_methods, methods_using_third_party_exceptions, interface_implementation_map, abstract_method_map


def parse_callgraph(callgraph_file):
    call_graph = []
    method_param_map = {}
    junit_pionner_dependent_classes = set()
    with open(callgraph_file, 'r') as f:
        for line in f:
            if line.startswith("C:"):
                caller, callee_class = line.strip().split()
                caller_class = caller.split(':')[1]
                if callee_class.startswith('org.junitpioneer'):
                    junit_pionner_dependent_classes.add(caller_class)
            if line.startswith("M:"):
                caller, callee = line.strip().split()
                caller_method = caller.split(':')[1] + ":" +\
                    caller.split(':')[2].split('(')[0]
                caller_method = re.sub(r'\$\d+', '', re.sub(r'lambda\$', '', caller_method))
                callee_method = callee.split(')')[1]\
                    .split('(')[0]
                callee_method = re.sub(r'\$\d+', '', re.sub(r'lambda\$', '', callee_method))
                call_graph.append((caller_method, callee_method))
                caller_params = caller.split("(")[1].split(")")[0].split(",")
                callee_params = callee.split(")")[1].split("(")[1].split(")")[0].split(",")
                if caller_method in method_param_map:
                    method_param_map[caller_method].update(caller_params)
                else:
                    params = set()
                    params.update(caller_params)
                    method_param_map[caller_method] = params
                if callee_method in method_param_map:
                    method_param_map[callee_method].update(callee_params)
                else:
                    params = set()
                    params.update(callee_params)
                    method_param_map[callee_method] = params
    return call_graph, method_param_map, junit_pionner_dependent_classes


def identify_third_party_dependencies(call_graph, third_party_packages, override_methods, method_param_map, implemented_methods, child_classes_of_third_party_types, third_party_exception_dependencies, junit_pionner_dependent_classes, interface_implementation_map, abstract_method_map):
    classes_to_remove = set()
    to_examine = []
    for third_party_ex_dependent_cls in third_party_exception_dependencies:
        for third_party_ex_dependent_method in third_party_exception_dependencies[third_party_ex_dependent_cls]:
            if not third_party_ex_dependent_method in to_examine:
                to_examine.append(third_party_ex_dependent_method)
    dependent_class_methods = third_party_exception_dependencies.copy()
    examined = set()

    classes_to_remove.update(child_classes_of_third_party_types)
    classes_to_remove.update(junit_pionner_dependent_classes)
    for caller_method, callee_method in call_graph:
        caller_class = caller_method.split(":")[0]
        callee_class = callee_method.split(":")[0]
        if any((callee_class.startswith(pkg) or (callee_method.replace(":", ".").startswith(pkg))) for pkg in third_party_packages)\
            and (("<init>" in caller_method) or ("<clinit>" in caller_method) or ("setUp" in caller_method) or ("tearDown" in caller_method)):
            classes_to_remove.add(caller_class)
        if any((callee_class.startswith(pkg) or (callee_method.replace(":", ".").startswith(pkg))) for pkg in third_party_packages)\
            and (caller_method in override_methods):
            classes_to_remove.add(caller_class)
    
    for caller_method, callee_method in call_graph:
        caller_class = caller_method.split(":")[0]
        callee_class = callee_method.split(":")[0]
        
        if any((callee_class.startswith(pkg) or (callee_method.replace(":", ".").startswith(pkg))) for pkg in third_party_packages)\
            or (caller_class in classes_to_remove):
            if caller_class in dependent_class_methods:
                dependent_class_methods[caller_class].add(caller_method)
            else:
                methods = set()
                methods.add(caller_method)
                dependent_class_methods[caller_class] = methods
            to_examine.append(caller_method)
    
    while to_examine:
        method = to_examine.pop(0)
        method_class = method.split(":")[0]
        examined.add(method)

        if method in override_methods:
            classes_to_remove.add(method_class)
        
        if method_class in interface_implementation_map:
            for implemented_interface in interface_implementation_map[method_class]:
                if implemented_interface in abstract_method_map:
                    for abstract_method in abstract_method_map[implemented_interface]:
                        if method.split(":")[1] == abstract_method.split(":")[1]:
                            print("IDENTIFIED IMPLICIT OVERRIDE METHOD:", method)
                            classes_to_remove.add(method_class)
        
        for caller_method, callee_method in call_graph:
            caller_class = caller_method.split(":")[0]
            if (callee_method == method)\
                and (("<init>" in caller_method) or ("<clinit>" in caller_method) or ("setUp" in caller_method) or ("tearDown" in caller_method)):
                classes_to_remove.add(caller_class)
            if (callee_method == method) and (caller_method in override_methods):
                classes_to_remove.add(caller_class)

        for caller_method, callee_method in call_graph:
            caller_class = caller_method.split(":")[0]
            callee_class = callee_method.split(":")[0]
            classes_to_remove_copy = classes_to_remove.copy()
            for class_to_remove in classes_to_remove_copy:
                if caller_class.split("$")[0] == class_to_remove:
                    classes_to_remove.add(caller_class)
                if callee_class.split("$")[0] == class_to_remove:
                    classes_to_remove.add(callee_class)                

        for caller_method, callee_method in call_graph:
            callee_class = callee_method.split(":")[0]
            caller_class = caller_method.split(":")[0]

            if (callee_method == method) or (caller_class in classes_to_remove):
                if caller_class in dependent_class_methods:
                    dependent_class_methods[caller_class].add(caller_method)
                else:
                    methods = set()
                    methods.add(caller_method)
                    dependent_class_methods[caller_class] = methods
                if (not caller_method in examined) and (not caller_method in to_examine):
                    to_examine.append(caller_method)
        
        for dependent_class in dependent_class_methods:
            for method in dependent_class_methods[dependent_class]:
                if (("<init>" in method) or ("<clinit>" in method) or ("setUp" in method) or ("tearDown" in method)):
                    classes_to_remove.add(dependent_class)
        
        for caller_method, callee_method in call_graph:

            callee_class = callee_method.split(":")[0]
            for callee_param in method_param_map[callee_method]:
                if (callee_param in classes_to_remove) or (callee_param in third_party_packages):
                    if not any(callee_class.startswith(std) for std in standard_java_packages):
                        if callee_class in dependent_class_methods:
                            dependent_class_methods[callee_class].add(callee_method)
                        else:
                            methods = set()
                            methods.add(callee_method)
                            dependent_class_methods[callee_class] = methods
                        if (not callee_method in examined) and (not callee_method in to_examine):
                            to_examine.append(callee_method)

            if callee_class in classes_to_remove:
                if callee_class in dependent_class_methods:
                    dependent_class_methods[callee_class].add(callee_method)
                else:
                    methods = set()
                    methods.add(callee_method)
                    dependent_class_methods[callee_class] = methods
                if (not callee_method in examined) and (not callee_method in to_examine):
                    to_examine.append(callee_method)
            
            caller_class = caller_method.split(":")[0]
            for caller_param in method_param_map[caller_method]:
                if (caller_param in classes_to_remove) or (caller_param in third_party_packages):
                    if caller_class in dependent_class_methods:
                        dependent_class_methods[caller_class].add(caller_method)
                    else:
                        methods = set()
                        methods.add(caller_method)
                        dependent_class_methods[caller_class] = methods
                    if (not caller_method in examined) and (not caller_method in to_examine):
                        to_examine.append(caller_method)
            
            if caller_class in classes_to_remove:
                if caller_class in dependent_class_methods:
                    dependent_class_methods[caller_class].add(caller_method)
                else:
                    methods = set()
                    methods.add(caller_method)
                    dependent_class_methods[caller_class] = methods
                if (not caller_method in examined) and (not caller_method in to_examine):
                    to_examine.append(caller_method)
                
    return classes_to_remove, dependent_class_methods


def is_special_test_class(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    if re.search(r'@RunWith\(\s*Parameterized\.class\s*\)', content):
        return True

    if re.search(r'extends\s+TestCase', content):
        return True

    return False

def has_test_methods(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    if re.search(r'@Test', content):
        return True

    if re.search(r'public\s+void\s+test\w*\(', content):
        return True

    return False

def extract_class_name(file_path):
    class_name = file_path.split("/")[-1].split(".java")[0]
    return class_name


def refactor_code(source_code_path, dependent_class_methods, third_party_packages, classes_to_remove):
    classes_names_to_remove = [path.replace("$", ".").split(".")[-1] for path in classes_to_remove]
    for class_name in third_party_packages:
        classes_names_to_remove.append(class_name.replace("$", ".").split(".")[-1])
    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                if "/java/" not in file_path:
                    continue
                class_path = file_path.split("/java/")[1].split(".")[0].replace("/", ".")
                class_base_path = class_path.split("$")[0]

                methods_to_remove = set()
                for key, methods in dependent_class_methods.items():
                    if key.split("$")[0] == class_base_path:
                        methods_to_remove.update(methods)
                
                test_class_dependent_on_third_party_fields = False

                if not methods_to_remove:
                    if has_test_methods(file_path):
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            for i, line in enumerate(lines):
                                import_match = re.match(r'import\s+(static\s+)?([\w.]+(\.\*)?);', line.strip())
                                if import_match:
                                    imported = import_match.group(2)
                                    if (any(imported.startswith(third_pkg) for third_pkg in third_party_packages)) \
                                        or (any(imported.startswith(dep_method.replace(":", ".").replace("$", ".")) for dep_method in third_party_packages)) \
                                        or (any((imported == class_to_remove.replace("$", ".")) for class_to_remove in classes_to_remove)) \
                                        or (any((imported.rsplit('.', 1)[0] == class_to_remove.replace("$", ".")) for class_to_remove in classes_to_remove)):
                                        test_class_dependent_on_third_party_fields = True
                                        break
                    if not test_class_dependent_on_third_party_fields:
                        continue
                
                print(f"Refactoring {class_path}")

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()

                with open(file_path, 'w') as f:
                    skip_class = False
                    if test_class_dependent_on_third_party_fields:
                        classes_to_remove.add(class_base_path)
                    for class_to_remove in classes_to_remove:
                        if class_to_remove == class_base_path:
                            placeholder_written = False
                            skip_class = True
                            package, _, _ = class_base_path.rpartition('.')
                            f.write("package " + package + ";\n")
                            for i, line in enumerate(lines):
                                if placeholder_written:
                                    break
                                multiline = line
                                for j in range(max_multiline):
                                    if j > 0 and (i + j) < len(lines):
                                        multiline += lines[i + j]
                                    if re.match(class_regex, multiline.strip()):
                                        f.write(multiline.replace("\n", " ").split("{")[0].split("extends")[0].split("implements")[0])
                                        f.write("{}")
                                        placeholder_written = True
                                        break
                            break
                    if skip_class:
                        continue
                    inside_method = False
                    skip_method = False
                    annotation_buffer = []
                    method_brace_level = 0
                    outer_class_brace_level = 0
                    inner_class_brace_level = 0
                    skip_lines = 0
                    inside_outer_class = False
                    inside_inner_class = False
                    skipping_inner_class = False
                    multiline = None
                    match_some_header = False
                    annotation_cached = False
                    remove_line = False

                    for i, line in enumerate(lines):
                        multiline = line
                        if skip_lines > 0:
                            skip_lines -= 1
                            continue
                        # Skip third-party import statements
                        import_match = re.match(r'import\s+(static\s+)?([\w.]+(\.\*)?);', line.strip())
                        if import_match:
                            imported = import_match.group(2)
                            if (any(imported.startswith(third_pkg) for third_pkg in third_party_packages)) \
                                or (any(imported.startswith(dep_method.replace(":", ".").replace("$", ".")) for dep_method in third_party_packages)) \
                                or (any((imported == class_to_remove.replace("$", ".")) for class_to_remove in classes_to_remove)) \
                                or (any((imported.rsplit('.', 1)[0] == class_to_remove.replace("$", ".")) for class_to_remove in classes_to_remove)):
                                continue
                        
                        match_some_header = False
                        for j in range(max_multiline):
                            if j > 0 and (i + j) < len(lines):
                                multiline += lines[i + j]
                            if re.match(class_regex, multiline.strip()) and inside_outer_class:
                                inner_class_match = re.match(class_regex, multiline.strip())
                                if inner_class_match:
                                    inside_inner_class = True
                                    match_some_header = True
                                    skip_lines += j
                                    inner_class_name = inner_class_match.group(4)
                                    class_path += ('$' + inner_class_name.split("<")[0])
                                    for class_to_remove in classes_to_remove:
                                        if "$" in class_to_remove:
                                            parts = class_to_remove.split('$')
                                            if (parts[0] + "$" + parts[1]) == class_path:
                                                skipping_inner_class = True
                                    break
                            
                            if re.match(class_regex, multiline.strip()) and (not inside_outer_class):
                                inside_outer_class = True
                                match_some_header = True
                                skip_lines += j
                            
                            if j == 0:
                                if re.match(r'\s*@\w+(\([^()]*\))?', multiline.strip()) and not inside_method:
                                    annotation_buffer.append(multiline)
                                    annotation_cached = True
                                    if i + j < len(lines):
                                        next_line_num = i + 1
                                        next_line = lines[next_line_num]
                                        while (re.match(r'^\s*(//.*|/\*(.|[\r\n])*?\*/)?\s*$', next_line.strip()) or re.match(r'\s*@\w+(\([^()]*\))?', next_line.strip())):
                                            annotation_buffer.append(next_line)
                                            skip_lines += 1
                                            next_line_num += 1
                                            next_line = lines[next_line_num]
                                        next_lines = ''
                                        for k in range(max_multiline - 1):
                                            next_lines += lines[next_line_num]
                                            if (next_line_num + 1) < len(lines):
                                                next_line_num += 1
                                            else:
                                                break
                                            method_match = re.match(
                                                method_regex,
                                                next_lines.strip()
                                            )
                                            if method_match:
                                                method_signature = method_match.group(5)
                                                full_method_name = class_base_path +\
                                                    (("$" + class_path.split('$')[1]) if ('$' in class_path) else '') +\
                                                    ":" + method_signature
                                                exceptions_thrown = method_match.group(7).split("throws")[1].split(",") if method_match.group(7) != None else []
                                                exceptions_thrown_cleaned = [exception.strip() for exception in exceptions_thrown]
                                                if (full_method_name in methods_to_remove) or any(ex in classes_names_to_remove for ex in exceptions_thrown_cleaned):
                                                    match_some_header = True
                                                    annotation_buffer = []
                                                    annotation_cached = False
                                                    remove_line = True
                                                    break
                                    else:
                                        f.write(multiline)
                                        break
                                else:
                                    annotation_cached = False
                            
                            # Check if the line is a method header
                            method_match = re.match(
                                method_regex,
                                multiline.strip()
                            )
                            if (not inside_method) and method_match:
                                method_signature = method_match.group(5)
                                full_method_name = class_base_path +\
                                    (("$" + class_path.split('$')[1]) if ('$' in class_path) else '') +\
                                    ":" + method_signature
                                exceptions_thrown = method_match.group(7).split("throws")[1].split(",") if method_match.group(7) != None else []
                                exceptions_thrown_cleaned = [exception.strip() for exception in exceptions_thrown]
                                inside_method = True
                                skip_method = (full_method_name in methods_to_remove) or (any(ex in classes_names_to_remove for ex in exceptions_thrown_cleaned))
                                method_brace_level = 0  # Start counting from the opening brace
                                match_some_header = True
                                skip_lines += j
                            
                            if match_some_header:
                                break

                        if annotation_cached:
                            continue
                        
                        if annotation_buffer:
                            for annotation in annotation_buffer:
                                if not skipping_inner_class:
                                    f.write(annotation)
                            annotation_buffer = []
                            annotation_cached = False
                        
                        if not match_some_header:
                            multiline = line

                        if inside_method:
                            method_brace_level += multiline.count('{')
                            method_brace_level -= multiline.count('}')

                            if method_brace_level == 0:
                                inside_method = False
                                if skip_method:
                                    skip_method = False
                                    continue
                            if skip_method:
                                continue

                        if inside_outer_class:
                            outer_class_brace_level += multiline.count('{')
                            outer_class_brace_level -= multiline.count('}')
                            if outer_class_brace_level == 0:
                                inside_outer_class = False
                        
                        if inside_inner_class:
                            inner_class_brace_level += multiline.count('{')
                            inner_class_brace_level -= multiline.count('}')
                            if inner_class_brace_level == 0:
                                inside_inner_class = False
                                class_path = class_path.split('$')[0]
                                if skipping_inner_class:
                                    skipping_inner_class = False
                                    continue

                        if remove_line:
                            remove_line = False
                            continue

                        if skipping_inner_class:
                            continue

                        f.write(multiline)

    classes_removed = []
    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)

                if is_special_test_class(file_path) and not has_test_methods(file_path):
                    class_name = extract_class_name(file_path)
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)
                    classes_removed.append(class_name)

    for root, _, files in os.walk(source_code_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    for class_name in classes_removed:
                        if re.search(r'extends\s+' + re.escape(class_name), content):
                            print(f"Deleting file (depends on removed class): {file_path}")
                            os.remove(file_path)
                            break



def main(project_name):

    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_dir = os.path.dirname(os.path.dirname(script_dir)) + f"/java_projects/automated_reduced_projects/{project_name}"

    
    if not os.path.isdir(project_dir):
        print(f"Error: Reduced Project directory '{project_dir}' does not exist.")
        sys.exit(1)
    try:
        os.chdir(project_dir)
    except FileNotFoundError:
        print(f"Error: Directory '{project_dir}' does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for directory '{project_dir}'.")
        sys.exit(1)

    if not os.path.isfile('callgraph.txt'):
        print(f"Error: 'callgraph.txt' not found in {project_dir}.")
        sys.exit(1)

    current_project_packages = identify_current_project_packages(source_code_path)
    class_package_map, third_party_packages, third_party_exceptions = identify_third_party_packages(source_code_path, current_project_packages)
    child_classes_of_third_party_types, implemented_methods, third_party_exception_dependencies, interface_implementation_map, abstract_method_map = get_implemented_methods_and_child_classes_of_third_party_types(
        source_code_path,
        class_package_map,
        third_party_packages,
        third_party_exceptions
    )
    call_graph, method_param_map, junit_pionner_dependent_classes = parse_callgraph('callgraph.txt')
    override_methods = identify_override_methods(source_code_path)
    classes_to_remove, dependent_methods = identify_third_party_dependencies(
        call_graph,
        third_party_packages,
        override_methods,
        method_param_map,
        implemented_methods,
        child_classes_of_third_party_types,
        third_party_exception_dependencies,
        junit_pionner_dependent_classes,
        interface_implementation_map,
        abstract_method_map
    )
    refactor_code(source_code_path, dependent_methods, third_party_packages, classes_to_remove)
    print("Refactored code to remove third-party dependencies and their dependents.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reduce_third_party_libs.py project_name")
        sys.exit(1)
    
    project_name = sys.argv[1]
    main(project_name)
