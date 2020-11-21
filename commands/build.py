from os import getcwd
from os.path import basename, exists
from .command_bool_interface import CommandBoolInterface
import subprocess


class CommandBuild(CommandBoolInterface):
    def __str__(self):
        return "build"

    def help(self):
        return "Compile and execute program without deleting it. Use it in root directory"

    def short_option(self):
        return "-b"

    def long_option(self):
        return "--build"

    def success_text(self):
        return "Program built successfully"

    def fail_text(self, message="Undefined error"):
        return "Cannot execute {program}: {message}".format(program=self, message=message)

    def execute(self):
        subprocess.call('make')
        print('---------------------------------------')
        executable = './{}'.format(basename(getcwd()))
        if exists(executable):
            subprocess.call(executable)
        else:
            print(self.fail_text())
