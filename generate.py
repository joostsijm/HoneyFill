#!/usr/bin/env python2.7

__author__ = ['[bergjnl]']
__date__ = '2016.09.7'

import sys
import os
import argparse

parses = argparse.ArgumentParser(
        description='''Generating a script that starts the PokemonGo-Map using
        given coords and accounts from CSV Files'''
        )
parser.add_argument(
        '-a','--accounts', 
        action='store_true',
        dest='accounts',
        help='''Path to the account file. Stored in CVS format:
            <account type>,<username>,<password>''')
parser.add_argument(
        '-c','--accounts',
        action='store_true',
        dest='coords',
        help='''Path to the file that stores the coords in CSV format:
            <long>,<lat>''')
parser.add_argument(
        '-o','--output',
        action='store_true',
        dest='output',
        help='''Place to store the output file.''')
args = parser.parse_args()


