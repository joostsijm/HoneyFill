# HoneyFill
Multi-account & multi-location generator in python.
Generate .sh file to start [PokemonGo-Map](https://github.com/PokemonGoMap/PokemonGo-Map) with given coordinates.

## Requirements

* Python 2.7

## Usage

### Synopsis

	usage: generate.py [-h] -a ACCOUNTS -c COORDS [-t THREADS] [-o OUTPUT]
        	           [-st STEPS] [-ar ARGUMENT] [-m] [-tn] [-f]

	Generating a PokemonGo-Map starting script with using given coords and
	accounts from CSV Files

	optional arguments:
		-h, --help            	show this help message and exit
		-a ACCOUNTS, --accounts ACCOUNTS
	                        	Path to the account file. Stored in CVS format:
                        <account type>,<username>,<password>
		-c COORDS, --coords COORDS
        	                	Path to the file that stores the coords in CSV format:
                	        	<long>,<lat>
		-t THREADS, --threads THREADS
                        		Number accounts per leaps.
		-o OUTPUT, --output OUTPUT
                        		Place to store the output file.
		-st STEPS, --steps STEPS
                        		Step size to use.
		-ar ARGUMENT, --argument ARGUMENT
                        		Extra command line parameters.
		-m, --multyline       	Print the output to multyple lines.
		-tn, --threadname     	Give threads a unique name.
		-f, --format          	Use stepsize and number of accounts from coord CSV:
                        		<long>,<lat>,<steps>,<workers>,<accounts>

### Example

python2 generate.py -a EXAMPLEaccounts.csv -c EXAMPLElocations.csv

## File formating

### Accounts

	<account type>,<username>,<password>

account types: PTC / Google

### Coordinates

#### Normal

Standard mode.

	<long>,<lat>

#### Formating

While using the -f parameter make sure you have correct formatting in your CVS.

	<long>,<lat>,<steps>,<workers>,<accounts>

* steps: ammount of around the coordinate.
* workers: number of active scanning accounts.
* accounts: number of accounts to switch to if other fails.
