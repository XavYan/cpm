from decouple import config

from .command_bool_interface import CommandBoolInterface


class CommandVersion(CommandBoolInterface):
    def __str__(self):
        return "version"

    def help(self):
        return "Show actual installed version"

    def short_option(self):
        return "-v"

    def long_option(self):
        return "--version"

    def success_text(self):
        return ""

    def execute(self):
        print("Actual version is", config('VERSION'))
