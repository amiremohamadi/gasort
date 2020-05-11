import unittest
from gasort.chromosome import Chromosome

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

if __name__ == '__main__':
    unittest.main()
