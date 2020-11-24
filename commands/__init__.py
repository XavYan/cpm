from .add import CommandAdd
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove
from .run import CommandRun
from .build import CommandBuild
from .version import CommandVersion


def initialize_command(command):
    commands = {
        'add': CommandAdd(),
        'init': CommandInit(),
        'tadd': CommandAdd(template=True),
        'run': CommandRun(),
        'build': CommandBuild(),
        'version': CommandVersion()
    }

    return commands[command]
