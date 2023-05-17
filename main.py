import os
import subprocess

def open_file_explorer(path):
    path = os.path.realpath(path)
    subprocess.run(f'explorer /select,"{path}"')

def find_env_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.env'):
                full_path = os.path.join(root, file)
                print(f'.env file found: {full_path}')
                open_file_explorer(full_path)

find_env_files('D:\\')
