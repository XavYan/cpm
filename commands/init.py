from os import makedirs
from os.path import join

from ._constants import BASE_DIRS
from .command_arg_interface import CommandArgInterface


class CommandInit(CommandArgInterface):
    def __init__(self, makefile, writer):
        super().__init__()
        self.makefile = makefile
        self.writer = writer

    def __str__(self):
        return "init"

    def argument_name(self):
        return "module"

    def help(self):
        return "Creates a new C++ project"

    def short_option(self):
        return None

    def long_option(self):
        return "--init"

    def success_text(self):
        return "Package directory created successfully"

    def execute(self, arg):
        try:
            self._create_base_dir(arg)
            self.makefile.generate(arg, arg)
            # with open('{}/src/main.cc'.format(arg), 'w') as main:
            #     main.write('#include <iostream>\n\n')
            #     main.write('int main (int argc, char* argv[]) {\n')
            #     main.write('\tstd::cout << "Hello World!\\n";\n')
            #     main.write('}\n')
            lines_to_add = [
                '#include <iostream>',
                '\n',
                'int main (int argc, char* argv[]) {',
                '\tstd::cout << "Hello World!\\n";',
                '}'
            ]
            self.writer.write_lines(lines_to_add, '{}/src/main.cc'.format(arg))

        except FileExistsError:
            print(self.fail_text("{arg} exists".format(arg=arg)))
        except:
            print(self.fail_text())
            raise

    def _create_base_dir(self, package):
        for key, value in BASE_DIRS.items():
            if value:
                self.writer.create_new_folder(join(package, key))
