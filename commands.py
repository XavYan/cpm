from decouple import config

class CommandInterface:
  def __init__ (self):
    self.arg = ""

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

  def set_arg (self, arg):
    self.arg = arg

  def execute (self):
    raise NotImplementedError

class CommandInstall(CommandInterface):
  def __init__ (self):
    super()
  
  def __str__ (self):
    return "install"

  def help (self):
    return "Install module files inside {}".format(config('DIR_PATH'))

  def argument_name (self):
    return "module"

  def short_option (self):
    return "-i"

  def long_option (self):
    return "--install"

  def set_arg (self, arg):
    self.arg = arg

  def execute (self):
    pass

class CommandAdd(CommandInterface):
  def __init__ (self):
    super()

  def __str__ (self):
    return "add"
  
  def help (self):
    return "Add a new module to be imported in other projects. You need to include the name of the files, for example: 'cpm add common' to add common.{} and common.{}".format(config('HEADER_EXT_FILE'), config('SOURCE_EXT_FILE'))
  
  def argument_name (self):
    return "module"

  def short_option (self):
    return "-a"

  def long_option (self):
    return "--add"

  def set_arg (self, arg):
    self.arg = arg

  def execute (self):
    pass