from unittest import TestCase

from commands import CommandAdd
from makefile import Makefile
from tests.writerfake import WriterFake


class TestCommandTemplateAdd(TestCase):
    def setUp(self):
        self.module = "vector"
        self.writerfake = WriterFake()
        self.makefile = Makefile(self.writerfake)
        self.cmd_tadd = CommandAdd(self.makefile, self.writerfake, template=True)

    def test_str_is_tadd(self):
        self.assertEqual(self.cmd_tadd.__str__(), "tadd")

    def test_short_option(self):
        self.assertEqual(self.cmd_tadd.short_option(), "-t")

    def test_long_option(self):
        self.assertEqual(self.cmd_tadd.long_option(), "--tadd")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_tadd.help()), str)

    def test__add_header_file(self):
        expected_lines = [
            '#pragma once',
            '\n',
            'template<class T>',
            'class {module} {{'.format(module=self.module),
            'public:',
            '\t{module}();'.format(module=self.module),
            '};',
            '\n',
            'template<class T>',
            '{module}<T>::{module}() {{}}'.format(module=self.module)
        ]

        self.writerfake.set_exists_file(False)

        self.cmd_tadd._add_header_file(self.module, template=True)

        header_filename = f'include/{self.module}.h'
        self.assertEqual(expected_lines, self.writerfake.get_lines_from_file(header_filename))
