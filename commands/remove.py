"""
    File containing CommandRemove class, who implements remove command
"""


from shutil import rmtree
from os.path import join
from os import remove
from decouple import config
from .command_arg_interface import CommandArgInterface


class CommandRemove(CommandArgInterface):
    """
        This class implements remove command, used to remove modules from utils folder. With
        --global option, it removes the module from cpm_modules folder
    """
    def __init__(self, writer):
        super().__init__()
        self.writer = writer

    def __str__(self):
        return "remove"

    def argument_name(self):
        return "module"

    def help(self):
        return "Remove installed module"

    def short_option(self):
        return "-R"

    def long_option(self):
        return "--remove"

    def success_text(self):
        return "Module removed successfully"

    def execute(self, arg):
        filepath = ""
        try:
            if self.global_option:
                filepath = join(config('DIR_PATH'), arg + '.' + config('COMPRESS_ALGORITHM'))
            else:
                filepath = join(config('IMPORT_FOLDER'), arg)
            self._remove_module(filepath)
        except FileNotFoundError:
            print(self.fail_text("Cannot found {} directory".format(filepath)))
            raise

    def _remove_module(self, filepath):
        if not self.writer.exists_file(filepath):
            raise FileNotFoundError
        if self.global_option:
            remove(filepath)
        else:
            rmtree(filepath)
