from .command_arg_interface import CommandArgInterface
from ._constants import BASE_DIR
from makefile import Makefile
from os import makedirs
from os.path import join


class CommandInit(CommandArgInterface):
    def __init__(self):
        self.makefile = Makefile()

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

    def execute(self, arg):
        try:
            self._create_base_dir(arg)
            self.makefile.generate(arg, arg)
            with open('{}/src/main.cc'.format(arg), 'w') as main:
                main.write('#include <iostream>\n\n')
                main.write('int main (int argc, char* argv[]) {\n')
                main.write('\tstd::cout << "Hello World!\\n";\n')
                main.write('}\n')
        except FileExistsError:
            print(self.fail_text("{arg} exists".format(arg=arg)))
        except:
            print(self.fail_text())
            raise

    @staticmethod
    def _create_base_dir(package):
        for key, value in BASE_DIR.items():
            if value:
                makedirs(join(package, key))
