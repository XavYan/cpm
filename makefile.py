from os.path import join
from decouple import config


def filepath(folder, filename, ext):
    return "{path}.{ext}".format(path=join(folder, filename), ext=ext)


class Makefile:
    def generate(self, package, path='./'):
        with open(join(path, 'Makefile'), 'w') as makefile:
            Makefile.add_variable(makefile, "CC", config('MAKEFILE_COMPILER'))
            Makefile.add_variable(makefile, "CFLAGS", config('MAKEFILE_COMPILER_OPTIONS'))
            makefile.write("\n")
            Makefile.add_base_all_action(makefile, package)

    def add_variable(self, makefile, name, value):
        makefile.write(name + "=" + value + "\n")

    def add_action(self, module, object_list=[], separator=True, path='./'):
        with open(join(path, 'Makefile'), 'a+') as makefile:
            makefile.write(filepath(config('BUILD'), module, 'o') + ':')
            makefile.write(" " + filepath(config('INCLUDE'), module, config('HEADER_EXT_FILE')))

            makefile.write(" " + filepath(config('SRC'), module, config('SOURCE_EXT_FILE')))

            for obj in object_list:
                makefile.write(" " + filepath(config('BUILD'), obj, 'o'))

            makefile.write('\n')

            makefile.write('\t$(CC) $(CFLAGS) -c -o ' + filepath(config('BUILD'), module, 'o'))

            makefile.write(" " + filepath(config('SRC'), module, config('SOURCE_EXT_FILE')))

            for obj in object_list:
                makefile.write(' ' + filepath(config('BUILD'), obj, 'o'))

            if separator:
                makefile.write('\n')

            Makefile.update_all_with_module(join(path, 'Makefile'), module)

    def delete_action(self, module):
        with open('Makefile', 'r') as makefile:
            lines = makefile.readlines()

        action = join(config('BUILD'), module) + '.o'

        new_lines = []
        all_detected = False
        action_line_detected = False
        for line in lines:
            if 'all:' in line or all_detected:
                new_lines.append(line.replace(action, ""))
                all_detected = not all_detected
            elif (action + ':') in line or action_line_detected:
                action_line_detected = not action_line_detected
            else:
                new_lines.append(line)

        with open('Makefile', 'w') as makefile:
            makefile.writelines(new_lines)

    def update_all_with_util(self, filename, module):
        with open(filename, 'r') as makefile:
            lines = makefile.readlines()

        build_util_folder = join(config('IMPORT_FOLDER'), module)

        new_lines = []
        all_detected = False
        for line in lines:
            if 'all:' in line:
                new_line = " ".join([line.rstrip(), filepath(build_util_folder, module, 'o') + '\n'])
                new_lines.append(new_line)
                all_detected = True
            elif all_detected:
                new_line = " ".join([line.rstrip(), filepath(build_util_folder, module, 'o') + '\n'])
                new_lines.append(new_line)
                all_detected = False
            else:
                new_lines.append(line)

        with open(filename, 'w') as makefile:
            makefile.writelines(new_lines)

    def update_all_with_module(self, filename, module):
        with open(filename, 'r') as makefile:
            lines = makefile.readlines()

        new_lines = []
        all_detected = False
        for line in lines:
            if 'all:' in line:
                new_line = " ".join([line.rstrip(), filepath(config('BUILD'), module, 'o') + '\n'])
                new_lines.append(new_line)
                all_detected = True
            elif all_detected:
                new_line = " ".join([line.rstrip(), filepath(config('BUILD'), module, 'o') + '\n'])
                new_lines.append(new_line)
                all_detected = False
            else:
                new_lines.append(line)

        with open(filename, 'w') as makefile:
            makefile.writelines(new_lines)

    def add_base_all_action(self, makefile, package, separator=True):
        makefile.write('all: ' + filepath(config('SRC'), 'main', config('SOURCE_EXT_FILE')) + '\n')
        makefile.write('\t$(CC) $(CFLAGS) -o {package} '.format(package=package) +
                       filepath(config('SRC'), 'main', config('SOURCE_EXT_FILE')))
        if separator:
            makefile.write('\n')
