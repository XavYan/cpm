from copy import deepcopy

from writer import Writer


class WriterFake(Writer):
    def __init__(self):
        super().__init__()
        self.removed_files = []
        self.lines: dict[str] = {}
        self.last_created_folders = []
        self.exists_file_response = True

    def set_lines(self, filename, lines):
        self.lines[filename] = deepcopy(lines)

    def clean_buffer(self):
        self.lines = []

    def get_all_lines(self):
        return self.lines

    def get_lines_from_file(self, filename):
        return self.lines[filename]

    def read_lines(self, filename):
        return self.lines[filename]

    def write_lines(self, lines, filename):
        self.lines[filename] = lines

    def append_lines(self, lines, filename):
        if filename not in self.lines.keys():
            self.lines[filename] = []
        self.lines[filename].extend(lines)

    def append_empty_line(self, filename):
        self.append_lines(['\n'], filename)

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
