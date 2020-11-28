from unittest import TestCase

from makefile import Makefile
from tests.writefake import WriterFake


class TestMakefile(TestCase):
    def setUp(self):
        self.module = "matrix"

    def test_generate(self):
        self.fail()

    def test_add_variable(self):
        self.fail()

    def test_add_action(self):
        self.fail()

    def test_delete_action(self):
        self.fail()

    def test_update_all_with_util(self):
        self.fail()

    def test_update_all_with_module(self):
        lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc",
            "\n"
        ]

        writerfake = WriterFake()
        makefile = Makefile(writerfake)

        writerfake.set_lines_to_read(lines)

        lines[0] += " build\\matrix.o"
        lines[1] += " build\\matrix.o"

        makefile.update_all_with_module('Makefile', 'matrix')

        self.assertEqual(writerfake.get_written_lines(), lines)

    def test_add_base_all_action(self):

        lines = [
            "all: src\\main.cc",
            "\t$(CC) $(CFLAGS) -o matrix src\\main.cc",
            "\n"
        ]

        writerfake = WriterFake()
        makefile = Makefile(writerfake)
        makefile.add_base_all_action('Makefile', 'matrix')

        self.assertEqual(writerfake.get_written_lines(), lines)

        lines.pop()
        writerfake.clean_buffer()

        makefile.add_base_all_action('Makefile', 'matrix', separator=False)

        self.assertEqual(writerfake.get_written_lines(), lines)
