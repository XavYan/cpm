#!/usr/bin/python3

"""
    This program is designed for better C++ programming. It supports creating both projects and
    class, with Makefile configuration automated included!
"""

import argparse as argp
import sys
import commands
from commands.command_interface import CommandInterface


def add_option(pars, command: CommandInterface):
    """
    This functions works to add a determined option to the command line parser
    :param pars: Commandline parser
    :param command: A command instance
    """
    if command.short_option():
        if command.action() in ("store_true", "store_false"):
            pars.add_argument(command.long_option(), command.short_option(), help=command.help(),
                              action=command.action())
        else:
            pars.add_argument(command.long_option(), command.short_option(), help=command.help(),
                              metavar=command.argument_name(), action=command.action())
    else:
        if command.action() in ("store_true", "store_false"):
            pars.add_argument(command.long_option(), help=command.help(), action=command.action())
        else:
            pars.add_argument(command.long_option(), help=command.help(),
                              metavar=command.argument_name(), action=command.action())


options = commands.command_list()

cms = {}

parser = argp.ArgumentParser(prog="cpm")

for option in options:
    cms[option] = commands.initialize_command(option)

    add_option(parser, cms[option])

parser.add_argument('--global', '-g', action='store_true',
                    help="Use global methods instead", dest="gl")

args = parser.parse_args()

if not args.gl and len(sys.argv) > 3:
    print("You can only use one option")
    sys.exit(1)

try:
    for arg, value in vars(args).items():
        if value and arg != 'gl':
            cms[arg].set_global(args.gl)
            if cms[arg].action() == "store":
                cms[arg].execute(value)
            else:
                cms[arg].execute()
            print(cms[arg].success_text())
except OSError:
    print('Han error has occurred:', sys.exc_info())
    sys.exit(1)
