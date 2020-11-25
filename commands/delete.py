from os import remove
from os.path import exists, join

from decouple import config

from commands.command_arg_interface import CommandArgInterface
from makefile import Makefile


class CommandDelete(CommandArgInterface):
    def __init__(self):
        super()
        self.makefile = Makefile()

    def __str__(self):
        return "delete"

    def argument_name(self):
        return "class"

    def help(self):
        return "Delete class from project"

    def short_option(self):
        return "-d"

    def long_option(self):
        return "--delete"

    def success_text(self):
        return "Class deleted successfully"

    def execute(self, arg):
        try:
            source_file = join(config('SRC'), arg + '.' + config('SOURCE_EXT_FILE'))
            header_file = join(config('INCLUDE'), arg + '.' + config('HEADER_EXT_FILE'))

            remove(header_file)
            if exists(source_file):
                remove(source_file)

            self.makefile.delete_action(arg)
        except FileNotFoundError:
            print(self.fail_text("File not found"))
