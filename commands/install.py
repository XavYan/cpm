from .command_interface import CommandInterface
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
        return "Install module from {} to {} project directory".format(config('DIR_PATH'), config('IMPORT_FOLDER'))

    def argument_name(self):
        return "module"

    def short_option(self):
        return "-i"

    def long_option(self):
        return "--install"

    def success_text(self):
        return "Module installed successfully"

    def execute(self, module, gl=False):
        if not gl:
            self._import_module(module)
        else:
            self._import_gl_module(module)

    @staticmethod
    def _import_module(module):
        try:
            module_global_path = join(config('DIR_PATH'), module)
            if exists(module_global_path) and isdir(module_global_path):
                if not exists(config('IMPORT_FOLDER')):
                    mkdir(config('IMPORT_FOLDER'))

                module_global_path = join(config('DIR_PATH'), module)
                copytree(module_global_path, join(config('IMPORT_FOLDER'), module))
            else:
                raise NotADirectoryError
        except NotADirectoryError:
            print("Cannot execute install:", module, "is not a directory or doesn't exists")
            raise

    @staticmethod
    def _import_gl_module(module):
        try:
            if not exists(module):
                raise FileNotFoundError
            if not isdir(module):
                raise NotADirectoryError

            module_global_path = join(config('DIR_PATH'), module)
            copytree(module, module_global_path)
        except FileNotFoundError:
            print("Cannot execute global install:", module, "does not exists")
            raise
        except NotADirectoryError:
            print("Cannot execute global install:", module, "is not a directory")
            raise
