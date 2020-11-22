from .command_arg_interface import CommandArgInterface
from decouple import config
from os.path import exists, join
from os import remove
from shutil import rmtree


class CommandRemove(CommandArgInterface):
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
            if self.gl:
                filepath = join(config('DIR_PATH'), arg + '.' + config('COMPRESS_ALGORITHM'))
            else:
                filepath = join(config('IMPORT_FOLDER'), arg)
            self._remove_module(filepath)
        except FileNotFoundError:
            print(self.fail_text("Cannot found {} directory".format(filepath)))
            raise

    def _remove_module(self, filepath):
        if not exists(filepath):
            raise FileNotFoundError
        if self.gl:
            remove(filepath)
        else:
            rmtree(filepath)
