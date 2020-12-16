"""
    File containing CommandBuild class, who implements build command
"""


from .command_bool_interface import CommandBoolInterface


class CommandBuild(CommandBoolInterface):
    """
        This class implements build command, letting users to create an executable using the
        Makefile in the project
    """
    def __init__(self, makefile, writer):
        super().__init__()
        self.makefile = makefile
        self.writer = writer

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
        if not self.writer.exists_file(executable):
            print(self.fail_text())

    def _compile_project(self):
        return self.makefile.compile_project()
