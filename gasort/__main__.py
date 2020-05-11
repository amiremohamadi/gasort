"""
    ----------------------------------------------------
      sorting bunch of numbers using genetic algorithm
    ----------------------------------------------------

    - version 0.1
    - changelog:
"""

import argparse
from chromosome import Chromosome
from genetic import gmutation


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

    # main genetic
    # calculate goal state fitness and geneset
    goal = Chromosome(sorted(numbers))
    geneset = numbers[:]


    parent = Chromosome(numbers[:], goal=goal)
    while parent.fitness != goal.fitness:
        child = gmutation(parent, geneset)

        if child.fitness > parent.fitness:
            parent = child
            print(child.genes)

