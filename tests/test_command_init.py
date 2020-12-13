from os.path import join
from unittest import TestCase

from commands import CommandInit
from makefile import Makefile
from tests.writefake import WriterFake


class TestCommandInit(TestCase):
    def setUp(self):
        self.project_name = "matrix"
        self.writerfake = WriterFake()
        self.makefile = Makefile(self.writerfake)
        self.cmd_init = CommandInit(self.makefile, self.writerfake)

    def test_str_is_init(self):
        self.assertEqual(self.cmd_init.__str__(), "init")

    def test_argument_name(self):
        self.assertEqual(self.cmd_init.argument_name(), "module")

    def test_help(self):
        self.assertEqual(type(self.cmd_init.help()), str)

    def test_short_option(self):
        self.assertIsNone(self.cmd_init.short_option())

    def test_long_option(self):
        self.assertEqual(self.cmd_init.long_option(), "--init")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_init.success_text()), str)

    def test__create_base_dir(self):
        self.cmd_init._create_base_dir(self.project_name)
        self.assertEqual(self.writerfake.get_created_folders(), [
            join(self.project_name, 'include'),
            join(self.project_name, 'src'),
            join(self.project_name, 'build')
        ])
