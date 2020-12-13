from unittest import TestCase

from commands import CommandBuild
from tests.makefilefake import MakefileFake
from tests.writerfake import WriterFake


class TestCommandBuild(TestCase):
    def setUp(self):
        self.project_name = "matrix"
        self.writerfake = WriterFake()
        self.mkfake = MakefileFake(self.writerfake, self.project_name)
        self.cmd_build = CommandBuild(self.mkfake)

    def test_str_is_build(self):
        self.assertEqual(self.cmd_build.__str__(), "build")

    def test_help(self):
        self.assertEqual(type(self.cmd_build.help()), str)

    def test_short_option(self):
        self.assertEqual(self.cmd_build.short_option(), "-b")

    def test_long_option(self):
        self.assertEqual(self.cmd_build.long_option(), "--build")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_build.success_text()), str)

    def test__compile_project_without_utils(self):
        expected_paths = [
            './matrix'
        ]

        self.cmd_build._compile_project()

        self.assertEqual(expected_paths, self.mkfake.get_compiled_paths())
