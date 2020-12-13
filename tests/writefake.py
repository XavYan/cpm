from copy import deepcopy


class WriterFake:
    def __init__(self):
        self.lines = []
        self.last_created_folders = []

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

    def create_new_folder(self, filename):
        self.last_created_folders.append(filename)

    def get_created_folders(self):
        return self.last_created_folders
