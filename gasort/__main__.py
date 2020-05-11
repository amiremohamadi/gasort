"""
    ----------------------------------------------------
      sorting bunch of numbers using genetic algorithm
    ----------------------------------------------------

    - version 0.1
    - changelog:
"""

import argparse


if __name__ == '__main__':
    # argument parser stuffs
    parser = argparse.ArgumentParser(description='sorting numbers using GA')
    input = parser.add_mutually_exclusive_group(required=True)
    input.add_argument('-f', '--file', action='store', type=str, help='read from file')
    input.add_argument('nums', action='store', type=int, nargs='*', default=[], help='list of numbers')

    args = parser.parse_args()
    # check the mode (file / IO)
    if args.file is not None:
        print('reading from file and the file is', args.file)
    elif args.nums:
        print('normal I/O and the numbers are', args.nums)

