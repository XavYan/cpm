from unittest import TestCase

from makefile import Makefile
from tests.writerfake import WriterFake


class TestMakefile(TestCase):
    def setUp(self):
        self.package = "matrix"
        self.action = "vector"
        self.filename = "Makefile"

        self.writerfake = WriterFake()
        self.makefile = Makefile(self.writerfake)

    def test_generate(self):
        expected_lines = [
            "CC=g++",
            "CFLAGS=-g -std=c++17 -Wall -Wextra -Iinclude -Iutils",
            "\n",
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o {package} src\\main.cc".format(package=self.package),
            "\n"
        ]

        self.makefile.generate(self.package)

        final_lines = self.writerfake.get_lines_from_file(self.filename)
        self.assertEqual(expected_lines, final_lines)

    def test_add_variable(self):
        expected_lines = ["CC=g++"]

        self.makefile.add_variable('CC', 'g++')

        final_lines = self.writerfake.get_lines_from_file(self.filename)
        self.assertEqual(expected_lines, final_lines)

    def test_add_action(self):
        expected_lines = [
            "all: src\\main.cc build\\{action}.o".format(action=self.action),
            "\t$(CC) $(CFLAGS) -o {package} src\\main.cc build\\{action}.o".format(package=self.package, action=self.action),
            "\n",
            "build\\{action}.o: include\\{action}.h src\\{action}.cc".format(action=self.action),
            "\t$(CC) $(CFLAGS) -c -o build\\{action}.o src\\{action}.cc".format(action=self.action)
        ]

        self.makefile.add_base_all_action(self.package)
        self.makefile.add_action(self.action)

        written_lines = self.writerfake.get_lines_from_file(self.filename)
        self.assertEqual(expected_lines, written_lines)

    def test_delete_action(self):
        initial_lines = [
            "all: src\\main.cc build\\{action}.o".format(action=self.action),
            "\t$(CC) $(CFLAGS) -o {package} src\\main.cc build\\{action}.o".format(package=self.package, action=self.action),
            "\n",
            "build\\{action}.o: include\\{action}.h src\\{action}.cc".format(action=self.action),
            "\t$(CC) $(CFLAGS) -c -o build\\{action}.o src\\{action}.cc".format(action=self.action)
        ]
        expected_lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o {package} src\\main.cc".format(package=self.package),
            "\n"
        ]

        self.writerfake.set_lines(self.filename, initial_lines)

        self.makefile.delete_action(self.action)

        final_lines = self.writerfake.get_lines_from_file(self.filename)
        self.assertEqual(expected_lines, final_lines)

    def test_update_all_with_util(self):
        new_util = "utils/{action}\\{action}.o".format(action=self.action)

        initial_lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o {package} src\\main.cc".format(package=self.package),
            "\n"
        ]
        expected_lines = [
            "all: src\\main.cc {util}".format(util=new_util),
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc {util}".format(util=new_util),
            "\n"
        ]

        self.writerfake.set_lines(self.filename, initial_lines)
        self.makefile.update_all_with_util(self.action)

        final_lines = self.writerfake.get_lines_from_file(self.filename)

        self.assertEqual(expected_lines, final_lines)

    def test_update_all_with_module(self):
        expected_lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc",
            "\n"
        ]

        self.writerfake.set_lines(self.filename, expected_lines)

        expected_lines[0] += " build\\matrix.o"
        expected_lines[1] += " build\\matrix.o"

        self.makefile.update_all_with_module('matrix')

        final_lines = self.writerfake.get_lines_from_file(self.filename)

        self.assertEqual(expected_lines, final_lines)

    def test_add_base_all_action_with_separator(self):
        expected_lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc",
            "\n"
        ]

        self.makefile.add_base_all_action('matrix')

        final_lines = self.writerfake.get_lines_from_file(self.filename)

        self.assertEqual(expected_lines, final_lines)

    def test_add_base_all_action_without_separator(self):
        expected_lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc"
        ]

        self.makefile.add_base_all_action('matrix', separator=False)

        final_lines = self.writerfake.get_lines_from_file(self.filename)

        self.assertEqual(expected_lines, final_lines)
