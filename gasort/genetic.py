'''core of the project
   all the algorithmic stuffs handled here
'''

import random
from .chromosome import Chromosome


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
