import os
import subprocess
from subprocess import Popen


def field_exercise_validation(fragment, args):

    prefix_path = f"data/recomposed_projects/{args.model_name}/{args.prompt_type}/{args.temperature}/{args.project_name}"
    os.makedirs(prefix_path, exist_ok=True)
    
    os.system(f"python3 src/postprocessing/recompose.py --project_name={args.project_name} \
                                                        --model_name={args.model_name} \
                                                        --output_dir=data/recomposed_projects \
                                                        --type={args.prompt_type} \
                                                        --temperature={args.temperature} \
                                                        --fragment_name={fragment['fragment_name']} \
                                                        --suffix={args.suffix}")

    current_path = os.getcwd()
    os.chdir(prefix_path)
    relative_file_path = f"{'/'.join(fragment['schema_name'].split('.')[1:])}.py"
    assert os.path.exists(relative_file_path), f"File {relative_file_path} does not exist"

    p = Popen(['python3', relative_file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(timeout=100)

    os.chdir(current_path)
    
    if p.returncode == 0:
        return True, None
    
    return False, stderr.decode('utf-8')
