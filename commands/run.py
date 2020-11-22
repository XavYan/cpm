from os import getcwd, remove, listdir
from os.path import basename, exists, join
from .command_bool_interface import CommandBoolInterface
import subprocess
from decouple import config


class CommandRun(CommandBoolInterface):
    def __str__(self):
        return "run"

    def help(self):
        return "Compile and execute program. It deletes the executable after executing. Use it in root directory"

    def short_option(self):
        return "-r"

    def long_option(self):
        return "--run"

    def success_text(self):
        return "Program ran successfully"

    def execute(self):
        if exists(config('IMPORT_FOLDER')):
            modules = listdir(config('IMPORT_FOLDER'))
            for module in modules:
                subprocess.call(['make', '-C', '{folder}'.format(folder=join(config('IMPORT_FOLDER'), module))])
                print('done')
        subprocess.call('make')
        print('---------------------------------------')
        executable = './{}'.format(basename(getcwd()))
        if exists(executable):
            subprocess.call(executable)
            remove(executable)
        else:
            print(self.fail_text("'{executable}' not found".format(executable=executable)))
