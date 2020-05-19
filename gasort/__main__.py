"""
    ----------------------------------------------------
      sorting bunch of numbers using genetic algorithm
    ----------------------------------------------------

    - version 1.1
    - changelog:
      -- add crossover
      -- use mutation under a probablity
      -- add selection
      -- genearte population
"""

import argparse
import random
from chromosome import Chromosome
from genetic import gsolve 


if __name__ == '__main__':
    # argument parser stuffs
    parser = argparse.ArgumentParser(description='sorting numbers using GA')
    input = parser.add_mutually_exclusive_group(required=True)
    input.add_argument('-f', '--file', action='store', type=str, help='read from file')
    input.add_argument('nums', action='store', type=int, nargs='*', default=[], help='list of numbers')

    args = parser.parse_args()
    # check the mode (file / IO) and read the numbers
    numbers = args.nums
    if args.file is not None:
        file = open(args.file, 'r')
        numbers = file.readline().split()

    gsolve(numbers)
