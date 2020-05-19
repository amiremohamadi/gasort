'''core of the project
   all the algorithmic stuffs handled here
'''

import random
from chromosome import Chromosome


def ginsert(child, population):
    '''insert child to the population, if child fitness is more than any
       item in the population list
       @params: child: Chromosome, population: List<Chromosome>
       @return: bool
    '''
    maximum1, maximum2 = None, None

    if len(population) > 0:
        maximum1 = population[0]
    if len(population) > 1:
        maximum2 = population[1]

    if maximum2 and child.fitness < maximum2.fitness:
        return False
    
    if not maximum1 or child.fitness > maximum1.fitness:
        # insert to the first of the list
        population.insert(0, child)
        return True
    
    if not maximum2 or child.fitness > maximum2.fitness:
        population.insert(1, child)
        return True

    return False

def gpopulation(geneset, size):
    '''generate random population, len(population) is at 'MOST' equal to size
       @params: geneset: List<int>, size: int
       @return: List<Chromosome>
    '''
    population = []
    n = len(geneset)

    for i in range(size):
        # make population by permuting geneset items
        chrom = Chromosome(random.sample(geneset, n))
        ginsert(chrom, population)

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
    maxim, second_maxim = population[:2]
    return [maxim, second_maxim]

def gsolve(geneset):
    '''use other functions to solve the problem'''

    # generate population
    population = gpopulation(geneset, 10)

    while True:
        # selection
        chrom1, chrom2 = gselect(population)

        print(chrom1.genes, chrom1.fitness)
        # repeat until reach the goal (1e9 fitness)
        if chrom1.fitness == 1e9:
            break

        # crossover (ordered)
        chrom3 = gcrossover(chrom1, chrom2)
        ginsert(chrom3, population)
        
        # UNCOMMENT THIS IF YOU WANT IGNORE MUTATION UNDER A RANDOM PROBABLITY
        # if random.randrange(10) % 2:
        #     continue

        # mutation
        chrom4 = gmutation(chrom1, geneset)
        ginsert(chrom4, population)

    return population

