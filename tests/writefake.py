from copy import deepcopy

class WriterFake:
    def __init__(self):
        self.last_read_lines = []
        self.last_wrote_lines = []

    def set_lines_to_read(self, lines):
        self.last_read_lines = deepcopy(lines)

    def clean_buffer(self):
        self.last_read_lines = []
        self.last_wrote_lines = []

    def get_written_lines(self):
        return self.last_wrote_lines

    def read_lines(self, filename):
        return self.last_read_lines

    def write_lines(self, lines, filename):
        self.last_wrote_lines = lines

    def append_lines(self, lines, filename):
        self.last_wrote_lines.extend(lines)

    def append_empty_line(self, filename):
        self.last_wrote_lines.append('\n')
