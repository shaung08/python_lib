import os
import yaml
import zipfile

def read_file(filename):
    f = open(filename, "r")
    data = f.readlines()
    f.close()
    return data

def write_file(filename, data):
    f = open(filename,  "w")
    f.writelines(data)
    f.close()

def read_yml(filename):
    f = open(filename, "r")
    data = yaml.safe_load(f)
    f.close()
    return data

def unzip_files(save_path, path_):
    with zipfile.ZipFile(path_, 'r') as zf:
        zf.extractall(path=save_path)

def check_folder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

def write_byte_file(content, path):
    f = open(path, "wb")
    f.write(content)
    f.close()
