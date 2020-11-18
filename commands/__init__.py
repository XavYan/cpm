from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove
from .run import CommandRun


def initialize_command(command):
    commands = {
        'add': CommandAdd(),
        'install': CommandInstall(),
        'init': CommandInit(),
        'remove': CommandRemove(),
        'tadd': CommandAdd(template=True),
        'run': CommandRun()
    }

    return commands[command]
