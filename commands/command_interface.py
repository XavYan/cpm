class CommandInterface:
    def __init__(self):
        self.gl = False

    def __str__(self):
        return "command"

    def set_global(self, gl=False):
        self.gl = gl
        return self.gl

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

    def fail_text(self, message="Undefined error"):
        return "Cannot execute {program}: {message}".format(program=self, message=message)
