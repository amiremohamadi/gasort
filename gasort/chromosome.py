'''chromosome model
'''
from functools import lru_cache


class Chromosome:
    __slots__ = ('genes', 'goal')

    def __init__(self, genes, goal=None):
        self.genes = genes
        self.goal = goal

    @property
    @lru_cache(maxsize=None)
    def fitness(self):
        '''calculate fitness value
           count number of items at the correct position
        '''

        # special case (the chromosome itself is the goal)
        if self.goal.genes == None:
            return len(self.genes)

        # invalid case
        if len(self.genes) != len(self.goal.genes):
            raise ValueError('goal and chromosome must have same len')

        # merge chromosomes and make gene pairs
        pair = zip(self.genes, self.goal.genes)
        # number of items in the correct position
        score = sum([1 for (g1, g2) in pair if g1 == g2])

        return score
