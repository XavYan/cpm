from .interface import CommandInterface
from makefile import Makefile

from decouple import config
from os import listdir
from os.path import join, exists
from shutil import copytree


class CommandAdd(CommandInterface):
    def __init__(self):
        super()

    def __str__(self):
        return "add"

    def help(self):
        return "Create a new class to the project. Also includes it to Makefile for compiling"

    def argument_name(self):
        return "module"

    def short_option(self):
        return "-a"

    def long_option(self):
        return "--add"

    def success_text(self):
        return "Module added to " + config('DIR_PATH') + " successfully"

    def execute(self, module, gl=False):
        try:
            header_filename = 'include/{}.h'.format(module)
            source_filename = 'src/{}.cc'.format(module)

            if exists(header_filename) or exists(source_filename):
                raise FileExistsError

            with open(header_filename, 'w') as file:
                file.write('#pragma once\n\n')
                file.write('class {} {{\n'.format(module))
                file.write('public:\n')
                file.write('\t{}();\n'.format(module))
                file.write('};\n')

            with open(source_filename, 'w') as file:
                file.write('#include <{}.h>\n\n'.format(module))
                file.write('{module}::{module}() {{}}\n'.format(module=module))

            Makefile.add_action(module)

        except FileNotFoundError:
            print("Cannot execute add:", "file not found")
        except FileExistsError:
            print("Cannot execute add:", module, "already exists in this project")
