from unittest import TestCase

from commands import CommandAdd
from makefile import Makefile
from tests.writerfake import WriterFake


class TestCommandAdd(TestCase):
    def setUp(self):
        self.module = "vector"
        self.writerfake = WriterFake()
        self.makefile = Makefile(self.writerfake)
        self.cmd_add = CommandAdd(self.makefile, self.writerfake)

    def test_str_is_add(self):
        self.assertEqual(self.cmd_add.__str__(), "add")

    def test_argument_name(self):
        self.assertEqual(self.cmd_add.argument_name(), "class")

    def test_help(self):
        self.assertEqual(type(self.cmd_add.help()), str)

    def test_short_option(self):
        self.assertEqual(self.cmd_add.short_option(), "-a")

    def test_long_option(self):
        self.assertEqual(self.cmd_add.long_option(), "--add")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_add.success_text()), str)

    def test__add_header_file(self):
        expected_lines = [
            '#pragma once',
            '\n',
            'class {module} {{'.format(module=self.module),
            'public:',
            '\t{module}();'.format(module=self.module),
            '};'
        ]

        self.writerfake.set_exists_file(False)

        self.cmd_add._add_header_file(self.module)

        header_filename = f'include/{self.module}.h'
        final_lines = self.writerfake.get_lines_from_file(header_filename)

        self.assertEqual(expected_lines, final_lines)

    def test__add_source_file(self):
        expected_lines = [
            '#include <{module}.h>'.format(module=self.module),
            '\n',
            '{module}::{module}() {{}}'.format(module=self.module)
        ]

        self.writerfake.set_exists_file(False)

        self.cmd_add._add_source_file(self.module)

        source_filename = f'src/{self.module}.cc'
        final_lines = self.writerfake.get_lines_from_file(source_filename)

        self.assertEqual(expected_lines, final_lines)
