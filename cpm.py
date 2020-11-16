#!/usr/bin/python3

import argparse as argp
from sys import argv
import commands

options = [
    'add',
    'install',
    'init',
    'remove'
]

cms = {}

parser = argp.ArgumentParser(prog="cpm")

for option in options:
    cms[option] = commands.initialize_command(option)
    if cms[option].short_option():
        parser.add_argument(cms[option].short_option(), cms[option].long_option(), help=cms[option].help(),
                            metavar=cms[option].argument_name())
    else:
        parser.add_argument(cms[option].long_option(), help=cms[option].help(), metavar=cms[option].argument_name())

args = parser.parse_args()

if len(argv) > 3:
    print("You can only use one option")
    exit(1)

try:
    for arg, value in vars(args).items():
        if value:
            cms[arg].execute(value)
            print(cms[arg].success_text())
            exit(0)
except:
    exit(1)
