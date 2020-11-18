from os.path import join
from decouple import config


def filepath(folder, filename, ext):
    return "{folder}/{filename}.{ext}".format(folder=folder, filename=filename, ext=ext)


class Makefile:
    @staticmethod
    def generate(package, path='./'):
        with open(join(path, 'Makefile'), 'w') as makefile:
            Makefile.add_variable(makefile, "CC", config('MAKEFILE_COMPILER'))
            Makefile.add_variable(makefile, "CFLAGS", config('MAKEFILE_COMPILER_OPTIONS'))
            makefile.write("\n")
            Makefile.add_base_all_action(makefile, package)

    @staticmethod
    def add_variable(makefile, name, value):
        makefile.write(name + "=" + value + "\n")

    @staticmethod
    def add_action(module, object_list=[], separator=True, path='./'):
        with open(join(path, 'Makefile'), 'a+') as makefile:
            makefile.write(filepath(config('BUILD'), module, 'o'))
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

    @staticmethod
    def update_all_with_module(filename, module):
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

    @staticmethod
    def add_base_all_action(makefile, package, separator=True):
        makefile.write('all:' + filepath(config('SRC'), 'main', config('SOURCE_EXT_FILE')) + '\n')
        makefile.write('\t$(CC) $(CFLAGS) -o {package} '.format(package=package) +
                       filepath(config('SRC'), 'main', config('SOURCE_EXT_FILE')))
        if separator:
            makefile.write('\n')
