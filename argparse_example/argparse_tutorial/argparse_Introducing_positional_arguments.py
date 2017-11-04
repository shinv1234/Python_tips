import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)

'''

$ python argparse_Introducing_Positional_arguments.py -h
usage: argparse_Introducing_Positional_arguments.py [-h] square

positional arguments:
  square      display a square of a given number

optional arguments:
  -h, --help  show this help message and exit

$ python argparse_Introducing_Positional_arguments.py 5
25

'''