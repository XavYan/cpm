"""
    File containing CommandArgInterface class
"""


from .command_interface import CommandInterface


class CommandArgInterface(CommandInterface):
    """
        Class interface for commands with arguments
    """
    def __str__(self):
        return "argument_command"

    def action(self):
        return "store"

    def argument_name(self):
        return "argument"

    def help(self):
        raise NotImplementedError

    def short_option(self):
        raise NotImplementedError

    def long_option(self):
        raise NotImplementedError

    def success_text(self):
        raise NotImplementedError

    def execute(self, arg):
        """
        This contains command functionality to be executed
        :param arg: Argument needed by the command
        """
        raise NotImplementedError
