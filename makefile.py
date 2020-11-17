from os.path import join
from decouple import config


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
    def add_action(module, object_list=[], separator=True, template=False, path='./'):
        with open(join(path, 'Makefile'), 'a+') as makefile:
            makefile.write("build/{}.o:".format(module))
            makefile.write(" include/{}.h".format(module))

            if not template:
                makefile.write(" src/{}.cc".format(module))

            for obj in object_list:
                makefile.write(" build/{}.o".format(obj))

            makefile.write('\n')

            makefile.write('\t$(CC) $(CFLAGS) -c -o build/{}.o'.format(module))

            if not template:
                makefile.write(" src/{}.cc".format(module))

            for obj in object_list:
                makefile.write(' build/{}.o'.format(obj))

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
                new_line = " ".join([line.rstrip(), 'build/{}.o'.format(module)]) + '\n'
                new_lines.append(new_line)
                all_detected = True
            elif all_detected:
                new_line = " ".join([line.rstrip(), 'build/{}.o'.format(module)]) + '\n'
                new_lines.append(new_line)
                all_detected = False
            else:
                new_lines.append(line)

        with open(filename, 'w') as makefile:
            makefile.writelines(new_lines)

    @staticmethod
    def add_base_all_action(makefile, package, separator=True):
        makefile.write('all: src/main.cc\n')
        makefile.write('\t{compiler} {options} -o {package} src/main.cc'
                       .format(compiler="$(CC)", options="$(CFLAGS)", package=package))
        if separator:
            makefile.write('\n')
