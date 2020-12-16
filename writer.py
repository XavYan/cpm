"""
    This file contains the Writer class
"""


from os import makedirs, remove
from os.path import exists


class Writer:
    """
        This class is used to work with files for reading and writing
    """
    def __init__(self):
        pass

    def read_lines(self, filename):
        """
        To get all lines from a file
        :param filename: Name of the file
        :return: An array of all the lines from the file
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines

    def write_lines(self, lines, filename):
        """
        To write all lines given by parameter to a file. Old file info will be deleted
        :param lines: An array with all lines to be written into the file
        :param filename: Name of the file to be written
        """
        with open(filename, 'w') as file:
            file.writelines(map(lambda line: line.rstrip() + '\n', lines))

    def append_lines(self, lines, filename):
        """
        To add several lines to the end of the file
        :param lines: Lines to be added
        :param filename: Name of the file
        """
        with open(filename, 'a+') as file:
            for line in lines:
                file.write(line.rstrip() + '\n')

    def append_empty_line(self, filename):
        """
        This method adds an empty line to the file
        :param filename: Name of the file
        """
        with open(filename, 'a+') as file:
            file.write('\n')

    def create_new_folder(self, folder_name):
        """
        It creates a new folder
        :param folder_name: Name of the new folder
        """
        makedirs(folder_name)

    def remove_file(self, filename):
        """
        Remove a file
        :param filename: Name of the file to be removed
        :return:
        """
        if not self.exists_file(filename):
            raise FileNotFoundError
        remove(filename)

    def exists_file(self, filename):
        """
        Return true if the file exists
        :param filename: Name of the file
        :return: True if file exists, False otherwise
        """
        return exists(filename)
