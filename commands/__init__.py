from makefile import Makefile
from writer import Writer
from .add import CommandAdd
from .command_update import CommandUpdate
from .delete import CommandDelete
from .install import CommandInstall
from .init import CommandInit
from .remove import CommandRemove
from .run import CommandRun
from .build import CommandBuild
from .version import CommandVersion

writer = Writer()
makefile_processor = Makefile(writer)

commands = {
    'add': CommandAdd(makefile_processor, writer),
    'init': CommandInit(makefile_processor, writer),
    'tadd': CommandAdd(makefile_processor, writer, template=True),
    'delete': CommandDelete(makefile_processor, writer),
    'run': CommandRun(makefile_processor, writer),
    'build': CommandBuild(makefile_processor, writer),
    'version': CommandVersion()
}


def initialize_command(command):
    return commands[command]


def command_list():
    return commands.keys()
