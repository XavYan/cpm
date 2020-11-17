from .interface import CommandInterface
from decouple import config
from os.path import exists, join
from shutil import rmtree


class CommandRemove(CommandInterface):
    def __init__(self):
        super()

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

    def execute(self, module, gl=False):
        if gl:
            self._remove_module(join(config('DIR_PATH'), module))
        else:
            self._remove_module(join(config('IMPORT_FOLDER'), module))

    @staticmethod
    def _remove_module(filepath):
        try:
            if exists(filepath):
                rmtree(filepath)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("Cannot execute remove: Cannot found", filepath, "directory")
            raise
