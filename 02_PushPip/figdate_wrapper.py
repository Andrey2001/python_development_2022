import sys
import venv
import tempfile # creation tmp directory
import subprocess
import shutil   # deletion tmp directory


temp_path = tempfile.mkdtemp()
venv.create(temp_path, with_pip=True)

args = [temp_path + '/bin/pip', 'install', 'pyfiglet']
subprocess.run(args) # "/временное/env/окружение/bin/pip install pyfiglet"

args = [temp_path + '/bin/python3', '-m', 'figdate'] + sys.argv[1:]
subprocess.run(args) # "python3 -m figdate"

shutil.rmtree(temp_path)