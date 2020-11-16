from os.path import join
from decouple import config


class Makefile:
    @staticmethod
    def generate_makefile(package, path='./'):
        with open(join(path, 'Makefile'), 'w') as makefile:
            Makefile.add_variable(makefile, "CC", config('MAKEFILE_COMPILER'))
            Makefile.add_variable(makefile, "CFLAGS", config('MAKEFILE_COMPILER_OPTIONS'))
            makefile.write("\n")
            Makefile.add_base_all_action(makefile, package)

    @staticmethod
    def add_variable(makefile, name, value):
        makefile.write(name + "=" + value + "\n")

    @staticmethod
    def add_action(name, object_list=[], separator=True, path='./'):
        with open(join(path, 'Makefile'), 'a+') as makefile:
            makefile.write("{}:".format(name))

            for obj in object_list:
                makefile.write(" build/{}.o".format(obj))

            makefile.write('\n')

            makefile.write('\t$(CC) $(CFLAGS) -c -o {}'.format(name))
            for obj in object_list:
                makefile.write(' build/{}.o'.format(obj))
                # TODO: Finish this part

            if separator:
                makefile.write('\n')

    @staticmethod
    def add_base_all_action(makefile, package, separator=True):
        makefile.write('all: src/main.cc\n')
        makefile.write('\t{compiler} {options} -o {package} src/main.cc'
                       .format(compiler="$(CC)", options="$(CFLAGS)", package=package))
        if separator:
            makefile.write('\n')
