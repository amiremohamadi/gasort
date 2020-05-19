import unittest
import sys
import pathlib
import random

# append parent directory to PATH
module = (pathlib.Path(__file__).resolve().parents[0]) / pathlib.Path('gasort')
sys.path.append(str(module))

from gasort.chromosome import Chromosome
from gasort.genetic import gmutation, gcrossover, gpopulation, gselect


class TestChromosome(unittest.TestCase):
    def test_ftness_calculate(self):
        ch1 = Chromosome([1, 2, 3, 4])
        self.assertEqual(ch1.fitness, 1e9)

        ch2 = Chromosome([1, 2, 4, 3])
        self.assertEqual(ch2.fitness, 1e9 - 1)

class TestGenetic(unittest.TestCase):
    def test_mutation(self):
        geneset = [1, 2, 3, 4]
        ch = Chromosome([1, 3, 2, 4])
        mutated = gmutation(ch, geneset)
        self.assertNotEqual(mutated.genes, ch.genes)

    def test_crossover(self):
        ch1 = Chromosome([2, 1, 3, 4, 5])
        ch2 = Chromosome([1, 3, 2, 4, 5])

        random.seed(901)
        crossovered = gcrossover(ch1, ch2)
        self.assertEqual(crossovered.genes, [2, 5, 3, 4, 1])

    def test_population(self):
        numbers = [1, 2, 3, 4]
        population = gpopulation(numbers, 10)
        self.assertTrue(hasattr(population[0], 'fitness'))

    def test_gselect(self):
        population = [Chromosome([3, 2, 1]),
                      Chromosome([1, 2, 3]),
                      Chromosome([2, 3, 1])
                ]

        maxim, secondmaxim = gselect(population)
        self.assertEqual(maxim.genes, Chromosome([3, 2, 1]).genes)
        self.assertEqual(secondmaxim.genes, Chromosome([1, 2, 3]).genes)


if __name__ == '__main__':
    unittest.main()
