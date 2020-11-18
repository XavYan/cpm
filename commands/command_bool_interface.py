from .command_interface import CommandInterface


class CommandBoolInterface(CommandInterface):
    def __str__(self):
        return "command"

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

    def fail_text(self, message):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError
