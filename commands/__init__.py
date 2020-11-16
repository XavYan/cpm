from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove


def initialize_command(command):
    commands = {
        'add': CommandAdd(),
        'install': CommandInstall(),
        'init': CommandInit(),
        'remove': CommandRemove()
    }

    return commands[command]
