'''core of the project
   all the algorithmic stuffs handled here
'''

import random
from chromosome import Chromosome


def gpopulation(geneset, goal, size):
    '''generate random population
       @params: geneset: List<int>, goal: Chromosome, size: int
       @return: List<Chromosome>
    '''
    population = []
    for i in range(size):
        chrom = Chromosome(random.sample(geneset, len(geneset)), goal=goal)
        population.append(chrom)

    return population


def gmutation(chrom, geneset):
    '''mutate a chromosome
       @params: chrom: Chromosome, geneset: List<int>
       @return: Chromosome
    '''
    new_chrom = Chromosome(chrom.genes[:], goal=chrom.goal) # copy of the chrom

    # change a random element
    index = random.randrange(0, len(chrom.genes))
    while new_chrom.genes[index] == chrom.genes[index]:
        new_gene = random.choice(geneset)
        new_chrom.genes[index] = new_gene

    return new_chrom

def gcrossover(chrom1, chrom2):
    '''uniform crossover, chrom1 concidered as the one with higher fitness
       so it has more chance
       @params: chrom1, chrom2: Chromosome
       @return: Chromosome
    '''
    # two parents must have same len
    if len(chrom1.genes) != len(chrom2.genes):
        raise ValueError('chrom1 and chrom2 must have same len')

    # two parents must have same goal
    if chrom1.goal.genes != chrom2.goal.genes:
        raise ValueError('chrom1 and chrom2 must have same goal genes')

    # generate new gen by crossovering the parents genes
    # NOTE that first parent (chrom1) has more chance
    n = len(chrom1.genes)
    genes = [chrom1.genes[i] if (random.randrange(0, 3) < 2) else chrom2.genes[i] for i in range(n)] 

    return Chromosome(genes, goal=chrom1.goal)
