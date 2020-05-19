'''core of the project
   all the algorithmic stuffs handled here
'''

import random
from chromosome import Chromosome


def gpopulation(geneset, size):
    '''generate random population
       @params: geneset: List<int>, size: int
       @return: List<Chromosome>
    '''
    population = []
    n = len(geneset)

    for i in range(size):
        # make population by permuting geneset items
        chrom = Chromosome(random.sample(geneset, n))
        population.append(chrom)

    return population


def gmutation(chrom, geneset):
    '''mutate a chromosome
       @params: chrom: Chromosome, geneset: List<int>
       @return: Chromosome
    '''
    _chrom = Chromosome(chrom.genes[:]) # make a copy
    n = len(_chrom.genes)

    # swap random element
    i1, i2 = random.sample(range(n), 2)
    _chrom.genes[i1], _chrom.genes[i2] = _chrom.genes[i2] ,_chrom.genes[i1]

    return _chrom

def gcrossover(chrom1, chrom2):
    '''order1 crossover (OX), for more information check this out:
       http://mat.uab.cat/~alseda/MasterOpt/GeneticOperations.pdf
       @params: chrom1, chrom2: Chromosome
       @return: Chromosome
    '''

    # two parents must have same len
    if len(chrom1.genes) != len(chrom2.genes):
        raise ValueError('chrom1 and chrom2 must have same len')


    # make copy of two genes to keep them immutable
    parent1 = Chromosome(chrom1.genes[:])
    parent2 = Chromosome(chrom2.genes[:])

    # generate new gen by crossovering the parents genes
    n = len(parent1.genes)

    # step 1: Select a random swath of consecutive alleles from parent 1
    # step 2: Drop the swath down to Child 1 and mark out these alleles in Parent 2
    # step 3: Starting on the right side of the swath, grab alleles from parent 2
    # and insert them in Child 1 at the right edge of the swath.
    i1, i2 = random.sample(range(n), 2)

    # i2 must be greater than i1
    if i2 < i1:
        i1, i2 = i2, i1

    # remove range(i1, i2) elements from parent 2
    i1toi2 = parent1.genes[i1:i2+1]
    cycle = []
    for i in range(n):
        if parent2.genes[i] not in i1toi2:
            cycle.append(parent2.genes[i])

    # make the child, step2 and step3
    child = Chromosome(parent1.genes[:])
    # walk through cycle and replace child genes (start right after i2)
    index = (i2 + 1) % n
    for ele in cycle:
        child.genes[index] = ele
        index = (index + 1) % n

    return child 

def gselect(population):
    '''select max and second-max from the population
       @params: population: List<Chromosome>
       @return: List<Chromsome>
    '''
    # len must be at least 1
    if len(population) < 1:
        raise ValueError('len(population) must be at least 1')

    # start with first element
    maxim, second_maxim = population[0], population[0]
    # iterate and find max and second_max
    for chrom in population:
        if chrom.fitness > maxim.fitness:
            second_maxim, maxim = maxim, chrom

    return [maxim, second_maxim]
