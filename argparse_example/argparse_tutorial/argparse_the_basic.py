import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

'''

$ python argparse_the_basic.py -h
usage: argparse_the_basic.py [-h]

optional arguments:
  -h, --help  show this help message and exit

$ argparse_the_basic.py --verbose
usage: argparse_the_basic.py [-h]
argparse_the_basic.py: error: unrecognized arguments: --verbose

'''