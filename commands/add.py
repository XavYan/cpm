from .command_arg_interface import CommandArgInterface


class CommandAdd(CommandArgInterface):
    def __init__(self, makefile, writer, template=False):
        super().__init__()
        self.makefile = makefile
        self.writer = writer
        self.template = template

    def __str__(self):
        if self.template:
            return "tadd"
        return "add"

    def argument_name(self):
        return "class"

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

    def execute(self, arg):
        try:
            self._add_header_file(arg, self.template)

            if not self.template:
                self._add_source_file(arg)
                self.makefile.add_action(arg)

        except FileNotFoundError:
            print(self.fail_text("file not found"))
        except FileExistsError:
            print(self.fail_text("{} already exists in this project".format(arg)))

    def _add_header_file(self, module, template=False):
        header_filename = 'include/{}.h'.format(module)

        if self.writer.exists_file(header_filename):
            raise FileExistsError

        lines = [
            '#pragma once',
            '\n'
        ]

        if template:
            lines.append('template<class T>')

        lines.extend([
            'class {module} {{'.format(module=module),
            'public:',
            '\t{module}();'.format(module=module),
            '};'
        ])

        if template:
            lines.extend([
                '\n',
                'template<class T>',
                '{module}<T>::{module}() {{}}'.format(module=module)
            ])

        self.writer.write_lines(lines, header_filename)

    def _add_source_file(self, module):
        source_filename = 'src/{module}.cc'.format(module=module)

        if self.writer.exists_file(source_filename):
            raise FileExistsError

        lines = [
            '#include <{module}.h>'.format(module=module),
            '\n',
            '{module}::{module}() {{}}'.format(module=module)
        ]

        self.writer.write_lines(lines, source_filename)
