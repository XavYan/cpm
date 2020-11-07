#!/usr/bin/python3

from decouple import config

from os import listdir, getenv
from os.path import isfile, isdir, join, splitext
import argparse as argp

from commands import *

commands = [
  CommandInstall(),
  CommandAdd()
]

parser = argp.ArgumentParser(prog="cpm")

for command in commands:
  parser.add_argument(command.short_option(), command.long_option(), help=command.help(), metavar=command.argument_name())

args = parser.parse_args()

for arg, value in vars(args).items():
  if value:
    print(arg, value)