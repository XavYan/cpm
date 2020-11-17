#!/usr/bin/python3

import argparse as argp
from sys import argv, exc_info
from os import getcwd, remove
from os.path import basename
import commands
import subprocess

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

parser.add_argument('-g', '--global', action='store_true',
                    help="Use global methods instead", dest="gl")
parser.add_argument('-b', '--build', action='store_true',
                    help="Compile and execute program. Use it in root directory")
parser.add_argument('-n', '--run', action='store_true',
                    help="Compile and execute program."
                         "It deletes the executable after executing. Use it in root directory")

args = parser.parse_args()

if args.build or args.run:
    subprocess.call('make')
    print('---------------------------------------')
    executable = './{}'.format(basename(getcwd()))
    subprocess.call(executable)
    if args.run:
        remove(executable)
    exit()

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
