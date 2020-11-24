from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove
from .run import CommandRun
from .build import CommandBuild


def initialize_command(command):
    commands = {
        'add': CommandAdd(),
        'init': CommandInit(),
        'tadd': CommandAdd(template=True),
        'run': CommandRun(),
        'build': CommandBuild()
    }

    return commands[command]
