''''chromosome model
''''

class Chromosome:
    __slots__ = ('genes', 'fitness')
    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness
