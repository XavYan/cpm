from .interface import CommandInterface
from decouple import config
from os import mkdir
from os.path import exists, join, isdir
from shutil import copytree

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
    MODULE_PATH = join(config('DIR_PATH'), module)
    if exists(MODULE_PATH) and isdir(MODULE_PATH):
      print("Module", module, "exists")
      self._import_module(module)
    else:
      raise FileNotFoundError

  def _import_module (self, module):
    if not exists(config('IMPORT_FOLDER')):
      mkdir(config('IMPORT_FOLDER'))

    MODULE_PATH = join(config('DIR_PATH'), module)
    copytree(MODULE_PATH, join(config('IMPORT_FOLDER'), module))