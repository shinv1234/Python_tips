import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
	
'''

# Description


# Execution

$ python argparse_optional_arguments3.py 4 -v
4^2 == 16


$ python argparse_optional_arguments3.py 4 -vv
the square of 4 equals 16


$ python argparse_optional_arguments3.py 4 --verbosity --verbosity
the square of 4 equals 16


$ python argparse_optional_arguments3.py 4 -vvv
16


$ python argparse_optional_arguments3.py 4 -vvvv
16


$ python argparse_optional_arguments3.py 4
16

'''

