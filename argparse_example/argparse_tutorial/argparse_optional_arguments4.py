import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity") 
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
	
	
'''

# Description
- If 'default' optional argument isn’t specified, it gets the None value, 
and that cannot be compared to an int value (hence the TypeError exception).


# Execution

$ python argparse_optional_arguments4.py 4
16

$ python argparse_optional_arguments4.py 4 -vvvvv
the square of 4 equals 16

# python argparse_optional_arguments4.py 4 -v
4^2 == 16

'''