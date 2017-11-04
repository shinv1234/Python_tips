import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose: 
    print("verbosity turned on") 


'''

# Description

- "store_true" means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False.

- To show that the option is actually optional, there is no error when running the program without it. Note that by default, if an optional argument isn’t used, the relevant variable, in this case args.
verbosity, is given None as a value, which is the reason it fails the truth test of the if statement.



# Execution

$ python argparse_Introducing_Optional_arguments.py --help
usage: argparse_Introducing_Optional_arguments.py [-h] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity


$ python argparse_Introducing_Optional_arguments.py --verbose
verbosity turned on

$ python argparse_Introducing_Optional_arguments.py -v
verbosity turned on

'''