import os
import subprocess
import configparser

def open_file_explorer(path):
    path = os.path.realpath(path)
    subprocess.run(f'explorer /select,"{path}"')

def find_env_files(path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                print(f'{extension} file found: {full_path}')
                open_file_explorer(full_path)

def read_config():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    return config['DEFAULT']['Path'], config['DEFAULT']['FileExtension']

path, extension = read_config()
find_env_files(path, extension)
