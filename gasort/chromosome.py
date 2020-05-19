'''chromosome model
'''
from functools import lru_cache


class Chromosome:
    __slots__ = ('genes')

    def __init__(self, genes):
        self.genes = genes

    @property
    @lru_cache(maxsize=None)
    def fitness(self):
        '''calculate fitness value
           count number of items at the correct position
        '''
        # the idea is to compare all elements with previous ones
        # if the element is smaller than any of previous neighbours
        # we add their difference to 'score' variable
        # at the end, we'll return (10^9 - score) because we want to 
        # keep sorted chromosomes fitness, higher
        score = 0
        n = len(self.genes)
        for i in range(n):
            for j in range(i):
                if self.genes[i] <= self.genes[j]:
                    score += self.genes[j] - self.genes[i]

        return 1e9 - score
