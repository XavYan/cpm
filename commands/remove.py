from .interface import CommandInterface

from decouple import config
from os.path import exists, join
from shutil import rmtree

class CommandRemove(CommandInterface):
  def __init__ (self):
    super()

  def __str__ (self):
    return "remove"

  def argument_name (self):
    return "module"

  def help (self):
    return "Remove installed module"

  def short_option (self):
    return "-r"

  def long_option (self):
    return "--remove"

  def execute (self, module):
    try:
      filepath = join(config('IMPORT_FOLDER'), module)
      if exists(filepath):
        rmtree(filepath)
      else:
        raise FileNotFoundError
    except FileNotFoundError:
      print("Cannot execute remove: Cannot found", filepath, "directory")