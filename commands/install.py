from .command_arg_interface import CommandArgInterface
from decouple import config
from os import mkdir
from os.path import exists, join, isdir
from shutil import make_archive, unpack_archive
from makefile import Makefile


class CommandInstall(CommandArgInterface):
    def __init__(self):
        self.makefile = Makefile()

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
        module_global_path = join(config('DIR_PATH'), module + '.' + config('COMPRESS_ALGORITHM'))

        if not exists(module_global_path):
            raise FileNotFoundError

        if not exists(config('IMPORT_FOLDER')):
            mkdir(config('IMPORT_FOLDER'))

        self._decompress_module(module_global_path, config('IMPORT_FOLDER'))
        self.makefile.update_all_with_util('Makefile', module)
        # copytree(module_global_path, join(config('IMPORT_FOLDER'), module))

    def _import_gl_module(self, module):
        if not exists(module):
            raise FileNotFoundError
        if not isdir(module):
            raise NotADirectoryError

        module_global_path = join(config('DIR_PATH'), module)
        self._compress_module(module, module_global_path)
        # copytree(module, module_global_path)

    def _compress_module(self, fromPath, toPath):
        return make_archive(toPath, config('COMPRESS_ALGORITHM'), base_dir=fromPath)

    def _decompress_module(self, fromPath, toPath):
        return unpack_archive(fromPath, toPath)