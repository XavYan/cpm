"""
    File containing CommandBoolInterface class
"""


from .command_interface import CommandInterface


class CommandBoolInterface(CommandInterface):
    """
        This interface class is for boolean commands
    """
    def __str__(self):
        return "command"

    def argument_name(self):
        return None

    def action(self):
        return "store_true"

    def help(self):
        raise NotImplementedError

    def short_option(self):
        raise NotImplementedError

    def long_option(self):
        raise NotImplementedError

    def success_text(self):
        raise NotImplementedError

    def execute(self):
        """
        This method will contain the command functionality, to be executed
        """
        raise NotImplementedError
