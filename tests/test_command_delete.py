from unittest import TestCase

from commands import CommandDelete
from tests.makefilefake import MakefileFake
from tests.writefake import WriterFake


class TestCommandDelete(TestCase):
    def setUp(self):
        self.project_name = "matrix"
        self.module = "vector"
        self.writerfake = WriterFake()
        self.makefile = MakefileFake(self.writerfake, self.project_name)
        self.cmd_delete = CommandDelete(self.makefile, self.writerfake)

    def test_str_is_delete(self):
        self.assertEqual(self.cmd_delete.__str__(), "delete")

    def test_argument_name(self):
        self.assertEqual(self.cmd_delete.argument_name(), "class")

    def test_help(self):
        self.assertEqual(type(self.cmd_delete.help()), str)

    def test_short_option(self):
        self.assertEqual(self.cmd_delete.short_option(), "-d")

    def test_long_option(self):
        self.assertEqual(self.cmd_delete.long_option(), "--delete")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_delete.success_text()), str)

    def test_execute(self):
        expected_to_be_removed = [
            "include\\{module}.h".format(module=self.module),
            "src\\{module}.cc".format(module=self.module)
        ]

        self.cmd_delete.execute(self.module)

        self.assertEqual(expected_to_be_removed, self.writerfake.get_removed_files())

    def test_execute_without_source(self):
        expected_to_be_removed = [
            "include\\{module}.h".format(module=self.module)
        ]

        self.writerfake.set_exists_file(False)

        self.cmd_delete.execute(self.module)

        self.assertEqual(expected_to_be_removed, self.writerfake.get_removed_files())
