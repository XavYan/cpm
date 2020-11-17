from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove


def initialize_command(command):
    commands = {
        'add': CommandAdd(),
        'install': CommandInstall(),
        'init': CommandInit(),
        'remove': CommandRemove(),
        'tadd': CommandAdd(template=True)
    }

    return commands[command]
