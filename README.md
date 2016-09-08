# HoneyFill
Multi-account & multi-location generator in python.
Generate .sh file to start [PokemonGo-Map](https://github.com/PokemonGoMap/PokemonGo-Map) with given coordinates.

Currently work in progress.


## Requirements

* Python 2.7

## Usage

    usage: generate.py [-h] -a ACCOUNTS -c COORDS -n ACCOUNTNUMBERS [-o OUTPUT]
                   [-st STEPS]

    Generating a PokemonGo-Map starting script with using given coords and
    accounts from CSV Files

    optional arguments:
      -h, --help            show this help message and exit
      -a ACCOUNTS, --accounts ACCOUNTS
                            Path to the account file. Stored in CVS format:
                            <account type>,<username>,<password>
      -c COORDS, --coords COORDS
                            Path to the file that stores the coords in CSV format:
                        <long>,<lat>
      -n ACCOUNTNUMBERS, --accountnumbers ACCOUNTNUMBERS
                            Number accounts per leaps.
      -o OUTPUT, --output OUTPUT
                        Place to store the output file.
      -st STEPS, --steps STEPS
                            Step size to use.
