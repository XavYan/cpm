from os.path import exists
from .command_bool_interface import CommandBoolInterface


class CommandBuild(CommandBoolInterface):
    def __init__(self, makefile):
        super().__init__()
        self.makefile = makefile

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
        executable = self._compile_project()
        print('---------------------------------------')
        if not exists(executable):
            print(self.fail_text())

    def _compile_project(self):
        return self.makefile.compile_project()
