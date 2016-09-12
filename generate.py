#!/usr/bin/env python2.7

__author__ = ['[bergjnl]']
__date__ = '2016.09.7'

import sys
import os
import argparse
import itertools 

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
        '-t','--threads',
        type=int,
        default="1",
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
parser.add_argument(
        '-ar','--argument',
        type=str,
        help='''Extra command line parameters.''')
args = parser.parse_args()

preamble = "#!/usr/bin/env bash"
server_template = "nohup python runserver.py -os {} &\n" #Server template for linux
worker_template = "sleep 1; nohup python runserver.py -ns {coords} -st {steps} {auth} {argsu} &\n" # Worker template
auth_template = "-a {} -u {} -p '{}'"  # For threading reasons whitespace after ' before ""
coord_template = "-l '{}, {}'"  # Template for location

coordpath = args.coords 
accpath = args.accounts

if os.path.isfile(accpath):
    if os.path.splitext(accpath)[1] != ".csv":
        print("account file isn't a csv file: {}".format(accpath))
        exit()
    else:
        print("Reading from account file:    \"{}\".".format(accpath))
        account_fh = open(args.accounts)
        account_fields = [line.split(",") for line in account_fh]
        accountform = [auth_template.format(line[0].strip(), line[1].strip(), line[2].strip()) for line in account_fields]
        count = 0
        accountformthread = []
        while count < len(accountform):
            if (len(accountform) - count < args.threads):
                break
            threadedacc = ""
            counttwo = 1
            while counttwo <= args.threads:
                counttwo = counttwo + 1
                threadedacc += (accountform[count]) + " "
                count = count + 1
            accountformthread.append(threadedacc)

else:
    print("Account file doesn't exist: {}".format(accpath))
    exit()

if os.path.isfile(coordpath):
    if os.path.splitext(coordpath)[1] != ".csv":
        print("coordinate file isn't a csv file: {}".format(coordpath))
        exit()
    else:
        print("Reading from coords file:     \"{}\".".format(coordpath))
        coord_fh = open(args.coords)
        coord_fields = [line.split(",") for line in coord_fh]
        coordform = [coord_template.format(line[0].strip(), line[1].strip()) for line in coord_fields]

else:
    print("coordinate file doesn't exist: {}".format(coordpath))
    exit()

print("Generating script to:         \"{}\".".format(args.output))
output_fh = file(args.output, "wb")
os.chmod(args.output, 0o755)
output_fh.write(preamble + "\n")
output_fh.write(server_template.format(coordform[0]))

location_and_auth = [(i, j) for i, j in itertools.izip(coordform, accountformthread)]

for i, (coords, accounts) in enumerate(location_and_auth):
    output_fh.write(worker_template.format(coords=coordform[i], steps=args.steps, auth=accounts, argsu=args.argument))
