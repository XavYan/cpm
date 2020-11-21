from .command_arg_interface import CommandArgInterface
from decouple import config
from os import mkdir
from os.path import exists, join, isdir
from shutil import copytree


class CommandInstall(CommandArgInterface):
    def __str__(self):
        if self.gl:
            return "global install"
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

    def execute(self, arg):
        try:
            if not self.gl:
                self._import_module(arg)
            else:
                self._import_gl_module(arg)
        except FileNotFoundError:
            print(self.fail_text("{} does not exists".format(arg)))
            raise
        except NotADirectoryError:
            print(self.fail_text("{} is not a directory".format(arg)))
            raise

    def _import_module(self, module):
        module_global_path = join(config('DIR_PATH'), module)

        if not exists(module_global_path):
            raise FileNotFoundError
        if not isdir(module_global_path):
            raise NotADirectoryError

        if not exists(config('IMPORT_FOLDER')):
            mkdir(config('IMPORT_FOLDER'))

        module_global_path = join(config('DIR_PATH'), module)
        copytree(module_global_path, join(config('IMPORT_FOLDER'), module))

    def _import_gl_module(self, module):
        if not exists(module):
            raise FileNotFoundError
        if not isdir(module):
            raise NotADirectoryError

        module_global_path = join(config('DIR_PATH'), module)
        copytree(module, module_global_path)
