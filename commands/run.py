from .command_bool_interface import CommandBoolInterface


class CommandRun(CommandBoolInterface):
    def __init__(self, makefile, writer):
        super().__init__()
        self.makefile = makefile
        self.writer = writer

    def __str__(self):
        return "run"

    def help(self):
        return "Compile and execute program. It deletes the executable after executing. Use it in root directory"

    def short_option(self):
        return "-r"

    def long_option(self):
        return "--run"

    def success_text(self):
        return "Program ran successfully"

    def execute(self):
        executable = self.makefile.compile_project()
        print('---------------------------------------')
        if self.writer.exists_file(executable):
            self.makefile.execute_file(executable)
            self.writer.remove_file(executable)
        else:
            print(self.fail_text(f"'{executable}' not found"))
