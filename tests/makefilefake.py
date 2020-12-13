from os import listdir, getcwd
from os.path import join, exists, basename

from decouple import config

from makefile import Makefile


class MakefileFake(Makefile):
    def __init__(self, writer, current_dir):
        super().__init__(writer)
        self.current_dir = current_dir
        self.compiled_paths = []
        self.existing_folders = []
        self.executed_file = ""

    def set_existing_utils_folders(self, folders):
        self.existing_folders.extend(folders)

    def set_existing_utils_folder(self, folder):
        self.existing_folders.append(folder)

    def get_compiled_paths(self):
        return self.compiled_paths

    def compile_project(self, path='./'):
        import_folder_location = join(path, config('IMPORT_FOLDER'))
        if exists(import_folder_location):
            modules = listdir(import_folder_location)
            for module in modules:
                self.compiled_paths.append(join(import_folder_location, module))
        self.compiled_paths.append(join(path, self.current_dir))
        return join(path, self.current_dir)

    def get_executed_file(self):
        return self.executed_file

    def execute_file(self, filename):
        self.executed_file = filename
