from .command_interface import CommandInterface


class CommandArgInterface(CommandInterface):
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
        raise NotImplementedError
