from .interface import CommandInterface

from decouple import config
from os import listdir
from os.path import join
from shutil import copytree

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

  def final_text (self):
    return "Module added to " + config('DIR_PATH') + " successfully"

  def execute (self, module):
    try:
      files = listdir(module)
      for file in files:
        print(join(module, file))
      copytree(module, join(config('DIR_PATH'), module))
    except NotADirectoryError:
      print("Cannot execute add:", module, "is not a directory")
    except FileNotFoundError:
      print("Cannot execute add: cannot found", module)