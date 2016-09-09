#!/usr/bin/env python2.7

__author__ = ['[bergjnl]']
__date__ = '2016.09.7'

import sys
import os
import argparse

parser = argparse.ArgumentParser(
        description='''Generating a PokemonGo-Map starting script with using
        given coords and accounts from CSV Files'''
        )
parser.add_argument(
        '-a','--accounts', 
        required=True,
        type=str,
        help='''Path to the account file. Stored in CVS format:
            <account type>,<username>,<password>''')
parser.add_argument(
        '-c','--coords',
        required=True,
        type=str,
        help='''Path to the file that stores the coords in CSV format:
            <long>,<lat>''')
parser.add_argument(
        '-n','--accountnumbers',
        required=True,
        type=int,
        help='''Number accounts per leaps.''')
parser.add_argument(
        '-o','--output',
        default="startworkers.sh",
        type=str,
        help='''Place to store the output file.''')
parser.add_argument(
        '-st','--steps',
        default="5",
        type=int,
        help='''Step size to use.''')
args = parser.parse_args()

server_template = "nohup python runserver.py -os -l '{lat}, {lon}' &\n" #Server template for linux
worker_template = "sleep 0.2; nohup python runserver.py -ns -l '{lat}, {lon}' -st {steps} {auth}&\n" # Worker template
auth_template = "-a {} -u {} -p '{}' "  # For threading reasons whitespace after ' before ""
coords_template = "-l '{}, {}' "  # Template for location

coordpath = args.coords 
accpath = args.accounts

if os.path.isfile(accpath):
    if os.path.splitext(accpath)[1] != ".csv":
        print("account file isn't a csv file: {}".format(accpath))
        exit()
    else:
        print("Reading from coordinate file: \"{}\".".format(accpath))
        account_fh = open(accpath)
        account_fields = [line.split(",") for line in account_fg]
        accounts = [auth_template.format(line[1].strip(), line[1].strip(), line[1].strip()) for line in account_fields]

else:
    print("Account file doesn't exist: {}".format(accpath))
    exit()

if os.path.isfile(coordpath):
    if os.path.splitext(coordpath)[1] != ".csv":
        print("coordinate file isn't a csv file: {}".format(coordpath))
        exit()
    else:
        print("Reading from account file:    \"{}\".".format(coordpath))
        coord_fh = open(coordpath)
        coord_fields = [line.split(",") for line in coord_fg]
        coords = [coord_template.format(line[1].strip(), line[1].strip()) for line in coord_fields]

else:
    print("coordinate file doesn't exist: {}".format(coordpath))
    exit()

print("Generating script to:         \"{}\".".format(args.output))
#output_fh = file(args.output, "wb")
#os.chmod(args.output, 0o755)
