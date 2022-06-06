import os
import yaml
from pathlib import Path
path_directory = os.getcwd()
file = Path(path_directory ).glob('*.yaml',recursive=True)
for filename in file:
    yaml_file = open(filename)
    parsed_yaml = yaml.safe_load(yaml_file)
    print(parsed_yaml['name'])
