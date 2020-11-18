from os import getcwd, remove
from os.path import basename
from .command_bool_interface import CommandBoolInterface
import subprocess


class CommandRun(CommandBoolInterface):
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

    def fail_text(self, message="Undefined error"):
        return "Cannot execute run: {}".format(message)

    def execute(self):
        subprocess.call('make')
        print('---------------------------------------')
        executable = './{}'.format(basename(getcwd()))
        subprocess.call(executable)
        remove(executable)
