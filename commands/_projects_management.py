import subprocess
from decouple import config
from os.path import exists, join, basename
from os import listdir, getcwd


def compile_project(path='./'):
    import_folder_location = join(path, config('IMPORT_FOLDER'))
    if exists(import_folder_location):
        modules = listdir(import_folder_location)
        for module in modules:
            subprocess.call(['make', '-C', '{folder}'.format(folder=join(import_folder_location, module))])
    subprocess.call('make')
    return join(path, basename(getcwd()))
