"""
    File containing CommandInstall class, who implements install command
"""


from os import mkdir
from os.path import join, isdir
from shutil import make_archive, unpack_archive

from decouple import config

from .command_arg_interface import CommandArgInterface


def _compress_module(from_path, to_path):
    return make_archive(to_path, config('COMPRESS_ALGORITHM'), base_dir=from_path)


def _decompress_module(from_path, to_path):
    return unpack_archive(from_path, to_path)


class CommandInstall(CommandArgInterface):
    """
        This class implements install command, which is used to install new project made by us
        to cpm_modules files, to use them in new projects
    """
    def __init__(self, makefile, writer):
        super().__init__()
        self.makefile = makefile
        self.writer = writer

    def __str__(self):
        if self.global_option:
            return "global install"
        return "install"

    def help(self):
        cpm_modules_path = config('DIR_PATH')
        utils_path = config('IMPORT_FOLDER')
        return f"Install module from {cpm_modules_path} to {utils_path} project directory"

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
            if not self.global_option:
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

        if not self.writer.exists_file(module_global_path):
            raise FileNotFoundError

        if not self.writer.exists_file(config('IMPORT_FOLDER')):
            mkdir(config('IMPORT_FOLDER'))

        _decompress_module(module_global_path, config('IMPORT_FOLDER'))
        self.makefile.update_all_with_util('Makefile', module)
        # copytree(module_global_path, join(config('IMPORT_FOLDER'), module))

    def _import_gl_module(self, module):
        if not self.writer.exists_file(module):
            raise FileNotFoundError
        if not isdir(module):
            raise NotADirectoryError

        module_global_path = join(config('DIR_PATH'), module)
        _compress_module(module, module_global_path)
        # copytree(module, module_global_path)
