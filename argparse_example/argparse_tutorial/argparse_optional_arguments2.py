import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
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

$ python argparse_optional_arguments2.py -h
usage: argparse_optional_arguments2.py [-h] [-v {0,1,2}] square

positional arguments:
  square                display a square of a given number

optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity
						

$ python argparse_optional_arguments2.py 4
16


$ python argparse_optional_arguments2.py 4 -v 2
the square of 4 equals 16


$ python argparse_optional_arguments2.py 4 -v 1
4^2 == 16


$ python argparse_optional_arguments2.py 4 -v 0
16

$ python argparse_optional_arguments2.py 4 -v 333
usage: argparse_optional_arguments2.py [-h] [-v {0,1,2}] square
argparse_optional_arguments2.py: error: argument -v/--verbosity: invalid choice: 333 (choose from 0, 1, 2)

'''