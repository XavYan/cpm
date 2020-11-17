from .interface import CommandInterface
from .constants import BASE_DIR
from makefile import Makefile

from decouple import config
from os import makedirs
from os.path import join


class CommandInit(CommandInterface):
    def __str__(self):
        return "init"

    def argument_name(self):
        return "package"

    def help(self):
        return "Creates a new C++ project"

    def short_option(self):
        return ""

    def long_option(self):
        return "--init"

    def success_text(self):
        return "Package directory created successfully"

    def execute(self, package):
        self._create_base_dir(package)
        Makefile.generate(package, package)

    @staticmethod
    def _create_base_dir(package):
        try:
            for key, value in BASE_DIR.items():
                if value:
                    makedirs(join(package, key))
        except FileExistsError:
            print("Cannot execute init correctly:", package, "exists")
