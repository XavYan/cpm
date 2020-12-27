"""
    This file implements Makefile class, who works with Makefile manipulation
"""


import subprocess
from os import listdir, getcwd
from os.path import join, exists, basename
from decouple import config


def filepath(folder, filename, ext):
    """
    Returns a filepath with extension
    :param folder: Path to the folder
    :param filename: Name of the file
    :param ext: Extension to be added to the file
    :return: Filepath of filename with extension
    """
    return "{path}.{ext}".format(path=join(folder, filename), ext=ext)


class Makefile:
    """
        Class to manipulate Makefile files
    """
    def __init__(self, writer):
        self.writer = writer

    def generate(self, package, path='./'):
        """
        It generates a new Makefile to the project
        :param package: Name of the project
        :param path: Path to the project. Actual by default
        """
        filename = join(path, 'Makefile')
        self.add_variable(filename, "CC", config('MAKEFILE_COMPILER'))
        self.add_variable(filename, "CFLAGS", config('MAKEFILE_COMPILER_OPTIONS'))
        self.writer.append_empty_line(filename)
        self.add_base_all_action(filename, package)

    def add_variable(self, filename, name, value):
        """
        Add a Makefile variable to especified file
        :param filename: Name of the file
        :param name: Name of the variable
        :param value: Value of the variable
        """
        line = name + "=" + value
        self.writer.append_lines([line], filename)

    def add_action(self, module, object_list=None, path='./'):
        """
        Add an action to the Makefile
        :param module: Name of the action
        :param object_list: Action dependency list
        :param path: Path of the project
        """
        if object_list is None:
            object_list = []

        build_module = filepath(config('BUILD'), module, 'o')
        header_module = filepath(config('INCLUDE'), module, config('HEADER_EXT_FILE'))
        source_module = filepath(config('SRC'), module, config('SOURCE_EXT_FILE'))

        action_header_line = build_module + ': ' + ' '.join([header_module, source_module])
        for obj in object_list:
            action_header_line += " " + filepath(config('BUILD'), obj, 'o')

        action_source_line = '\t$(CC) $(CFLAGS) -c -o {build} {source}'.format(build=build_module,
                                                                               source=source_module)
        for obj in object_list:
            action_source_line += ' ' + filepath(config('BUILD'), obj, 'o')

        lines = [
            action_header_line,
            action_source_line
        ]

        self.writer.append_lines(lines, 'Makefile')
        self.update_all_with_module(join(path, 'Makefile'), module)

    def delete_action(self, module):
        """
        Deletes an especific action from Makefile
        :param module: Name of the action to be deleted
        """
        lines = self.writer.read_lines('Makefile')

        action = join(config('BUILD'), module) + '.o'

        new_lines = []
        all_detected = False
        action_line_detected = False
        for line in lines:
            if 'all:' in line or all_detected:
                new_lines.append(line.replace(action, "").rstrip())
                all_detected = not all_detected
            elif action + ':' in line or action_line_detected:
                action_line_detected = not action_line_detected
            else:
                new_lines.append(line)

        self.writer.write_lines(new_lines, 'Makefile')

    def update_all_with_util(self, filename, module):
        """
        Add an action dependency to all action. Special for utils based action
        :param filename: Name of the Makefile file
        :param module: Name of the action to be added
        """
        lines = self.writer.read_lines(filename)

        build_util_folder = join(config('IMPORT_FOLDER'), module)

        new_lines = []
        all_detected = False
        for line in lines:
            if 'all:' in line:
                new_line = " ".join([line.rstrip(), filepath(build_util_folder, module, 'o')])
                new_lines.append(new_line)
                all_detected = True
            elif all_detected:
                new_line = " ".join([line.rstrip(), filepath(build_util_folder, module, 'o')])
                new_lines.append(new_line)
                all_detected = False
            else:
                new_lines.append(line)

        self.writer.write_lines(new_lines, filename)

    def update_all_with_module(self, filename, module):
        """
        Add an action dependency to all action. For tipical action
        :param filename: Name of the Makefile file
        :param module: Name of the action to be added
        """
        lines = self.writer.read_lines(filename)

        new_lines = []
        all_detected = False
        for line in lines:
            if 'all:' in line:
                new_line = " ".join([line.rstrip(), filepath(config('BUILD'), module, 'o')])
                new_lines.append(new_line)
                all_detected = True
            elif all_detected:
                new_line = " ".join([line.rstrip(), filepath(config('BUILD'), module, 'o')])
                new_lines.append(new_line)
                all_detected = False
            else:
                new_lines.append(line)

        self.writer.write_lines(new_lines, filename)

    def add_base_all_action(self, filename, package, separator=True):
        """
        Add all action, base for all Makefile files
        :param filename: Name of the Makefile file
        :param package: Name of the project
        :param separator: True if wants to add an empty line after all action
        """
        source = filepath(config('SRC'), 'main', config('SOURCE_EXT_FILE'))
        lines = [
            'all: {source}'.format(source=source),
            '\t$(CC) $(CFLAGS) -o {package} {source}'.format(package=package, source=source)
        ]
        self.writer.append_lines(lines, filename)
        if separator:
            self.writer.append_empty_line(filename)

    def compile_project(self, path='./'):
        """
        To compile a project with Makefile
        :param path: Path to the project. Must be a Makefile inside it
        """
        import_folder_location = join(path, config('IMPORT_FOLDER'))
        if exists(import_folder_location):
            modules = listdir(import_folder_location)
            for module in modules:
                folder = join(import_folder_location, module)
                subprocess.call(['make', '-C', f'{folder}'])
        subprocess.call('make')
        return join(path, basename(getcwd()))

    def execute_file(self, filename):
        """
        Runs an executable file
        :param filename: Name of the executable
        :return:
        """
        subprocess.call(filename)
