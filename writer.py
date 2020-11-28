class Writer:
    def __init__(self):
        pass

    def read_lines(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines

    def write_lines(self, lines, filename):
        with open(filename, 'w') as file:
            file.writelines(lines)

    def append_lines(self, lines, filename):
        with open(filename, 'a+') as file:
            for line in lines:
                file.write(line.rstrip() + '\n')

    def append_empty_line(self, filename):
        with open(filename, 'a+') as file:
            file.write('\n')
