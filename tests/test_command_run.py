from os.path import join
from unittest import TestCase

from commands import CommandRun
from tests.makefilefake import MakefileFake
from tests.writerfake import WriterFake


class TestCommandRun(TestCase):
    def setUp(self):
        self.project_name = "matrix"
        self.writerfake = WriterFake()
        self.mkfake = MakefileFake(self.writerfake, self.project_name)
        self.cmd_run = CommandRun(self.mkfake, self.writerfake)

    def test_str_is_run(self):
        self.assertEqual(self.cmd_run.__str__(), "run")

    def test_help(self):
        self.assertEqual(type(self.cmd_run.help()), str)

    def test_short_option(self):
        self.assertEqual(self.cmd_run.short_option(), "-r")

    def test_long_option(self):
        self.assertEqual(self.cmd_run.long_option(), "--run")

    def test_success_text(self):
        self.assertEqual(type(self.cmd_run.success_text()), str)

    def test_execute_and_remove_executable(self):
        expected_file = join('./', self.project_name)
        expected_files_to_be_removed = [
            f'./{self.project_name}'
        ]

        self.cmd_run.execute()

        self.assertEqual(expected_file, self.mkfake.get_executed_file())
        self.assertEqual(expected_files_to_be_removed, self.writerfake.get_removed_files())
