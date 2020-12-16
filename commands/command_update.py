"""
    File containing CommandUpdate class, who implements update command
"""


import random
import subprocess
from os import chdir, getcwd

from .command_bool_interface import CommandBoolInterface


class CommandUpdate(CommandBoolInterface):
    """
        This class implements update command, to update the project to a greater version, if
        available
    """
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
        actual_folder = getcwd()

        subprocess.call(['git', 'clone', url_repository, dst_folder])
        # Verify versions
        # If local version is lower than remote version, proceed
        # Need to be done...
        # -> Execute UNINSTALL.sh
        print(f"Uninstalling cpm: 'bash {dst_folder}/UNINSTALL.sh'")
        chdir(dst_folder)
        subprocess.call(['bash', './UNINSTALL.sh'])
        # -> Execute INSTALL.sh
        print(f"Installing cpm: 'bash {dst_folder}/INSTALL.sh'")
        subprocess.call(['bash', './INSTALL.sh'])
        chdir(actual_folder)
        # Delete cloned repository
        print(f"Removing {dst_folder}")
        subprocess.call(['rm', '-rf', dst_folder])
