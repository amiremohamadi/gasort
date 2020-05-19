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
from genetic import gmutation, gpopulation, gcrossover, gselect


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

    # generate population
    population = gpopulation(geneset, 10)

    while True:
        # selection
        chrom1, chrom2 = gselect(population)

        print(chrom1.genes, chrom1.fitness)
        # repeat until reach the goal
        if chrom1.genes == goal.genes:
            break

        # crossover (uniform)
        chrom3 = gcrossover(chrom1, chrom2)
        population.append(chrom3)
        
        # # ignore mutation (under a random probablity)
        if random.randrange(10) % 2:
            continue

        # do mutation
        chrom4 = gmutation(chrom1, geneset)
        population.append(chrom4)

