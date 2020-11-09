#!/usr/bin/python3

import argparse as argp

import commands

options = [
  'add',
  'install',
  'init'
]

cms = {}

parser = argp.ArgumentParser(prog="cpm")

for option in options:
  cms[option] = commands.initializeCommand(option)
  if cms[option].short_option():
    parser.add_argument(cms[option].short_option(), cms[option].long_option(), help=cms[option].help(), metavar=cms[option].argument_name())
  else:
    parser.add_argument(cms[option].long_option(), help=cms[option].help(), metavar=cms[option].argument_name())

args = parser.parse_args()

if args.install and args.add:
  print("Cannot use install and add methods at the same time")
  exit(1)

for arg, value in vars(args).items():
  if value:
    cms[arg].execute(value)

print("Done successfully!")