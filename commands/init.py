from .interface import CommandInterface
from .constants import BASE_DIR

from decouple import config
from os import makedirs
from os.path import join

class CommandInit(CommandInterface):
    def __str__(self):
        return "init"

    def argument_name(self):
        return "package"

    def help(self):
        return "Creates a new C++ project"

    def short_option(self):
        return ""

    def long_option(self):
        return "--init"

    def final_text(self):
        return "Package directory created successfully"

    def execute(self, package):
        self._create_base_dir(package)
        if config('MAKEFILE') == "True":
            self._create_makefile(package)

    @staticmethod
    def _create_base_dir(package):
        try:
            for key, value in BASE_DIR.items():
                if value:
                    makedirs(join(package, key))
        except FileExistsError:
            print("Cannot execute init correctly:", package, "exists")

    @staticmethod
    def _create_makefile(package):
        with open(join(package, 'Makefile'), 'w') as makefile:
            makefile.write("CC=g++\n")
            makefile.write("CFLAGS=-g -std=c++17 -Wall -Wextra -I$(INCLUDE) -Iutils\n")
            makefile.write("INCLUDE=include\n")
            makefile.write("BUILD=build\n")
            makefile.write("SRC=src\n")
            makefile.write("EXECUTABLE=" + package + ".out" + "\n")
            makefile.write(
                "all: $(INCLUDE)/*." + config('HEADER_EXT_FILE') + " $(SRC)/*." + config('SOURCE_EXT_FILE') + "\n")
            makefile.write(
                "\t$(CC) $(CFLAGS) -o $(EXECUTABLE) $(INCLUDE)/*." + config('HEADER_EXT_FILE') + " $(SRC)/*." + config(
                    'SOURCE_EXT_FILE') + "\n")
