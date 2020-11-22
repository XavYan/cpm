from os.path import exists
from .command_bool_interface import CommandBoolInterface
from ._projects_management import compile_project


class CommandBuild(CommandBoolInterface):
    def __str__(self):
        return "build"

    def help(self):
        return "Compile the project, without executing it. Use it in root directory"

    def short_option(self):
        return "-b"

    def long_option(self):
        return "--build"

    def success_text(self):
        return "Program built successfully"

    def execute(self):
        executable = compile_project()
        print('---------------------------------------')
        if not exists(executable):
            print(self.fail_text())
