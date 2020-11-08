from .add import CommandAdd
from .install import CommandInstall

def initializeCommand (command):
  commands = {
    'add': CommandAdd(),
    'install': CommandInstall()
  }

  return commands[command]