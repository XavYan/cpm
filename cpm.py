#!/usr/bin/python3

from os import listdir, getenv
from os.path import isfile, isdir, join, splitext
import argparse as argp

import commands

options = [
  'add',
  'install'
]

parser = argp.ArgumentParser(prog="cpm")

for option in options:
  command = commands.initializeCommand(option)
  parser.add_argument(command.short_option(), command.long_option(), help=command.help(), metavar=command.argument_name())

args = parser.parse_args()

if args.install and args.add:
  print("Cannot use install and add methods at the same time")
  exit(1)

for arg, value in vars(args).items():
  if value:
    print(arg, value)