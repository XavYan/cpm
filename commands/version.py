"""
    File containing CommandVersion class, who implements version command
"""

from _version import __version__
from .command_bool_interface import CommandBoolInterface


class CommandVersion(CommandBoolInterface):
    """
        This class implements version command. You can use it to get actual installed version
        of cpm
    """
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
        print("Actual version is", __version__)
