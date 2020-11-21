from .command_arg_interface import CommandArgInterface
from makefile import Makefile
from os.path import exists


class CommandAdd(CommandArgInterface):
    def __init__(self, template=False):
        super()
        self.template = template

    def __str__(self):
        if self.template:
            return "tadd"
        return "add"

    def argument_name(self):
        return "module"

    def help(self):
        if self.template:
            return "Create a new template class to the project"
        return "Create a new class to the project. Also includes it to Makefile for compiling"

    def short_option(self):
        if self.template:
            return "-t"
        return "-a"

    def long_option(self):
        if self.template:
            return "--tadd"
        return "--add"

    def success_text(self):
        if self.template:
            return "Created template class successfully"
        return "Created class successfully"

    def fail_text(self, message="Unexpected error"):
        if self.template:
            return "Cannot execute tadd: {}".format(message)
        return "Cannot execute add: {}".format(message)

    def execute(self, arg):
        try:
            self._add_header_file(arg, self.template)

            if not self.template:
                self._add_source_file(arg)
                Makefile.add_action(arg)

        except FileNotFoundError:
            print(self.fail_text("file not found"))
        except FileExistsError:
            print(self.fail_text("{} already exists in this project".format(arg)))

    @staticmethod
    def _add_header_file(module, template=False):
        header_filename = 'include/{}.h'.format(module)

        if exists(header_filename):
            raise FileExistsError

        with open(header_filename, 'w') as file:
            file.write('#pragma once\n\n')

            if template:
                file.write('template<class T>\n')

            file.write('class {} {{\n'.format(module))
            file.write('public:\n')
            file.write('\t{}();\n'.format(module))
            file.write('};\n')

            if template:
                file.write('\ntemplate<class T>\n')
                file.write('{module}<T>::{module}() {{}}\n'.format(module=module))

    @staticmethod
    def _add_source_file(module):
        source_filename = 'src/{}.cc'.format(module)

        if exists(source_filename):
            raise FileExistsError

        with open(source_filename, 'w') as file:
            file.write('#include <{}.h>\n\n'.format(module))
            file.write('{module}::{module}() {{}}\n'.format(module=module))
