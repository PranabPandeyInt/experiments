import os
import yaml
path = os.getcwd()
path_directory = path+'page'
file = Path(path_directory ).glob('*')
for filename in file:
    yaml_file = open(filename)
    parsed_yaml = yaml.safe_load(yaml_file)
    print(parsed_yaml['name'])
