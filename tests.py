import unittest
from gasort.chromosome import Chromosome
from gasort.genetic import gmutation

class TestChromosome(unittest.TestCase):
    def test_fitness_invalid_case(self):
        goal = Chromosome([1, 2, 3])
        ch1 = Chromosome([1, 2, 3, 4], goal=goal)
        with self.assertRaises(ValueError):
            ch1.fitness

    def test_ftness_calculate(self):
        goal = Chromosome([1, 2, 3, 4])
        ch1 = Chromosome([1, 2, 4, 3], goal=goal)
        self.assertEqual(ch1.fitness, 2)


class TestGenetic(unittest.TestCase):
    def test_mutation(self):
        geneset = [1, 2, 3, 4]
        goal = Chromosome([1, 2, 3, 4])
        ch = Chromosome([1, 3, 2, 4], goal=goal)
        mutated = gmutation(ch, geneset)
        self.assertNotEqual(mutated.genes, ch.genes)


if __name__ == '__main__':
    unittest.main()
