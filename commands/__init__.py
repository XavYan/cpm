from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit

from os import listdir
from os.path import splitext

def initializeCommand (command):
  commands = {
    'add': CommandAdd(),
    'install': CommandInstall(),
    'init': CommandInit()
  }

  return commands[command]