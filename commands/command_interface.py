class CommandInterface:
    def __init__(self):
        pass

    def __str__(self):
        return "command"

    def action(self):
        raise NotImplementedError

    def help(self):
        raise NotImplementedError

    def short_option(self):
        raise NotImplementedError

    def long_option(self):
        raise NotImplementedError

    def success_text(self):
        raise NotImplementedError

    def fail_text(self):
        raise NotImplementedError
