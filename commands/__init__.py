from makefile import Makefile
from writer import Writer
from .add import CommandAdd
from .delete import CommandDelete
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove
from .run import CommandRun
from .build import CommandBuild
from .version import CommandVersion


def initialize_command(command):

    writer = Writer()
    makefile_processor = Makefile(writer)

    commands = {
        'add': CommandAdd(makefile_processor),
        'init': CommandInit(makefile_processor),
        'tadd': CommandAdd(makefile_processor, template=True),
        'delete': CommandDelete(makefile_processor),
        'run': CommandRun(),
        'build': CommandBuild(),
        'version': CommandVersion()
    }

    return commands[command]
