"""
    File containing CommandInterface class
"""


class CommandInterface:
    """
        Base class interface for commands
    """
    def __init__(self):
        self.global_option = False

    def __str__(self):
        return "command"

    def set_global(self, global_option=False):
        """
        Set global boolean option
        :param global_option: New boolean value
        """
        self.global_option = global_option
        return self.global_option

    def argument_name(self):
        """
        :return: Argument name for commands with arguments
        """
        raise NotImplementedError

    def action(self):
        """
        :return: Action command type
        """
        raise NotImplementedError

    def help(self):
        """
        :return: Help text for --help option
        """
        raise NotImplementedError

    def short_option(self):
        """
        :return: Short option for this command
        """
        raise NotImplementedError

    def long_option(self):
        """
        :return: Long option for this command
        """
        raise NotImplementedError

    def success_text(self):
        """
        :return: Text showed when command succeed
        """
        raise NotImplementedError

    def fail_text(self, message="Undefined error"):
        """
        :param message: Message shown within return text
        :return: Meesage shown when command fails
        """
        return "Cannot execute {program}: {message}".format(program=self, message=message)
