import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
	

'''

# Description
- 'add_mutually_exclusive_group()' allows for us to specify options that conflict with each other. 

# Execution

$ python argparse_conflicting_options.py -h
usage: argparse_conflicting_options.py [-h] [-v | -q] x y

positional arguments:
  x              the base
  y              the exponent

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
  


$ python argparse_conflicting_options.py 3 4
3^4 == 81

$ python argparse_conflicting_options.py 3 4 -v
3 to the power 4 equals 81

$ python argparse_conflicting_options.py 3 4 -q
81

$ python argparse_conflicting_options.py 3 4 -v -q
usage: argparse_conflicting_options.py [-h] [-v | -q] x y
argparse_conflicting_options.py: error: argument -q/--quiet: not allowed with argument -v/--verbose

'''