from .interface import CommandInterface
from decouple import config
from os import mkdir
from os.path import exists, join, isdir
from shutil import copytree


class CommandInstall(CommandInterface):
    def __init__(self):
        super()

    def __str__(self):
        return "install"

    def help(self):
        return "Install module files inside {}".format(config('DIR_PATH'))

    def argument_name(self):
        return "module"

    def short_option(self):
        return "-i"

    def long_option(self):
        return "--install"

    def final_text(self):
        return "Module installed successfully"

    def execute(self, module):
        module_global_path = join(config('DIR_PATH'), module)
        if exists(module_global_path) and isdir(module_global_path):
            print("Module", module, "exists")
            self._import_module(module)
        else:
            raise NotADirectoryError

    @staticmethod
    def _import_module(module):
        if not exists(config('IMPORT_FOLDER')):
            mkdir(config('IMPORT_FOLDER'))

        module_global_path = join(config('DIR_PATH'), module)
        copytree(module_global_path, join(config('IMPORT_FOLDER'), module))
