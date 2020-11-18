#!/usr/bin/python3

import argparse as argp
from sys import argv, exc_info
from os import getcwd, remove
from os.path import basename
import commands
import subprocess


def add_option(pars, long_option, short_option="", help_msg="", arg_name="", act=""):
    # print("action:", act, "metavar:", arg_name)
    if short_option:
        if act == "store_true" or act == "store_false":
            pars.add_argument(long_option, short_option, help=help_msg, action=act)
        else:
            pars.add_argument(long_option, short_option, help=help_msg, metavar=arg_name, action=act)
    else:
        if act == "store_true" or act == "store_false":
            pars.add_argument(long_option, help=help_msg, action=act)
        else:
            pars.add_argument(long_option, help=help_msg, metavar=arg_name, action=act)


options = [
    'add',
    'tadd',
    'install',
    'init',
    'remove',
    'run'
]

cms = {}

parser = argp.ArgumentParser(prog="cpm")

for option in options:
    cms[option] = commands.initialize_command(option)
    argname = ""
    if cms[option].argument_name():
        argname = cms[option].argument_name()
    add_option(parser, cms[option].long_option(), short_option=cms[option].short_option(), help_msg=cms[option].help(),
               arg_name=argname, act=cms[option].action())

parser.add_argument('--global', '-g', action='store_true',
                    help="Use global methods instead", dest="gl")
add_option(parser, '--build', short_option='-b', help_msg="Compile and execute program. Use it in root directory",
           act="store_true")

args = parser.parse_args()

if args.build:
    subprocess.call('make')
    print('---------------------------------------')
    executable = './{}'.format(basename(getcwd()))
    subprocess.call(executable)
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
