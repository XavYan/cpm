import random
import subprocess

from .command_bool_interface import CommandBoolInterface


class CommandUpdate(CommandBoolInterface):
    def __str__(self):
        return "update"

    def help(self):
        return "Update cpm program, if needed"

    def short_option(self):
        return None

    def long_option(self):
        return "--update"

    def success_text(self):
        return "Updated successfully"

    def execute(self):
        # Clone git project to /tmp
        url_repository = 'https://github.com/XavYan/cpm'
        dst_folder = f'/tmp/cpm_{random.randint(1,10000)}'
        subprocess.call(['git', 'clone', url_repository, dst_folder])
        # TODO: Verify versions
        # TODO: If local version is lower than remote version, proceed
        # -> Execute UNINSTALL.sh
        subprocess.call([f'{dst_folder}/UNINSTALL.sh'])
        # -> Execute INSTALL.sh
        subprocess.call([f'{dst_folder}/INSTALL.sh'])
        # Delete cloned repository
        subprocess.call(['rm', '-rf', dst_folder])
