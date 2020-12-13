from os.path import join

from decouple import config

from commands.command_arg_interface import CommandArgInterface


class CommandDelete(CommandArgInterface):
    def __init__(self, makefile, writer):
        super().__init__()
        self.makefile = makefile
        self.writer = writer

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

            self.writer.remove_file(header_file)
            if self.writer.exists_file(source_file):
                self.writer.remove_file(source_file)

            self.makefile.delete_action(arg)
        except FileNotFoundError:
            print(self.fail_text("File not found"))
            raise
