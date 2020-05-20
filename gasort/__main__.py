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
import matplotlib.pyplot as plt
from chromosome import Chromosome
from genetic import gsolve 


if __name__ == '__main__':
    # argument parser stuffs
    parser = argparse.ArgumentParser(description='sorting numbers using GA')
    # input can be file / normal user stdin
    # only one of them can be used
    input = parser.add_mutually_exclusive_group(required=True)
    # file argument parser
    input.add_argument('-f', '--file', action='store', type=str,
            help='read from file')
    # default stdin argument parser
    input.add_argument('nums', action='store', type=int, nargs='*',
            default=[], help='list of numbers')

    args = parser.parse_args()
    
    # read numbers (file mode / stdin)
    numbers = args.nums
    if args.file is not None:
        file = open(args.file, 'r')
        # file must be in this format:
        # Eg. 1 2 3 4 5 6
        numbers = list(map(int, file.readline().split()))

    # solve the problem, implemention of main functions related to GA
    # are located in genetic.py
    generations = gsolve(numbers)

    plt.plot([x.fitness for x in reversed(generations)])
    plt.title('Fitness Evolution Diagram')
    plt.show()

