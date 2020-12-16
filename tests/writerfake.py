from copy import deepcopy

from writer import Writer


class WriterFake(Writer):
    def __init__(self):
        super().__init__()
        self.removed_files = []
        self.lines = []
        self.last_created_folders = []
        self.exists_file_response = True

    def set_lines(self, lines):
        self.lines = deepcopy(lines)

    def clean_buffer(self):
        self.lines = []

    def get_lines(self):
        return self.lines

    def read_lines(self, filename):
        return self.lines

    def write_lines(self, lines, filename):
        self.lines = lines

    def append_lines(self, lines, filename):
        self.lines.extend(lines)

    def append_empty_line(self, filename):
        self.lines.append('\n')

    def create_new_folder(self, folder_name):
        self.last_created_folders.append(folder_name)
        
    def remove_file(self, filename):
        self.removed_files.append(filename)

    def get_removed_files(self):
        return self.removed_files

    def get_created_folders(self):
        return self.last_created_folders

    def exists_file(self, filename):
        return self.exists_file_response

    def set_exists_file(self, exists):
        self.exists_file_response = exists
