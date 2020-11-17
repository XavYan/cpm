from .interface import CommandInterface
from ._constants import BASE_DIR
from makefile import Makefile
from sys import exc_info

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

    def execute(self, package, gl=False):
        try:
            self._create_base_dir(package)
            Makefile.generate(package, package)
            with open('{}/src/main.cc'.format(package), 'w') as main:
                main.write('#include <iostream>\n\n')
                main.write('int main (int argc, char* argv[]) {\n')
                main.write('\tstd::cout << "Hello World!\\n";\n')
                main.write('}\n')
        except:
            print("Unexpected error:", exc_info())
            raise

    @staticmethod
    def _create_base_dir(package):
        try:
            for key, value in BASE_DIR.items():
                if value:
                    makedirs(join(package, key))
        except FileExistsError:
            print("Cannot execute init correctly:", package, "exists")
