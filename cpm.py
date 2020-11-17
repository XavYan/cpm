#!/usr/bin/python3

import argparse as argp
from sys import argv, exc_info
import commands

options = [
    'add',
    'tadd',
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

parser.add_argument('-g', '--global', action='store_true', help="Use global methods instead", dest="gl")

args = parser.parse_args()

if not args.gl and len(argv) > 3:
    print("You can only use one option")
    exit(1)

try:
    for arg, value in vars(args).items():
        if value and arg != 'gl':
            cms[arg].execute(value, args.gl)
            print(cms[arg].success_text())
except:
    print('Han error has occurred:', exc_info())
    exit(1)
