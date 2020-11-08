from .interface import CommandInterface
from decouple import config

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

  def execute (self, module):
    pass