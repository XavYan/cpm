class CommandInterface:
  def __init__ (self):
    pass

  def __str__ (self):
    return "command"

  def argument_name (self):
    return "value"

  def help (self):
    raise NotImplementedError

  def short_option (self):
    raise NotImplementedError

  def long_option (self):
    raise NotImplementedError

  def final_text (self):
    raise NotImplementedError

  def execute (self):
    pass