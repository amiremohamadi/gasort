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

    def test_crossover(self):
        goal = Chromosome([1, 2, 3, 4, 5])
        ch1 = Chromosome([1, 2, 2, 4, 4], goal=goal)
        ch2 = Chromosome([1, 3, 2, 4, 5], goal=goal)

        random.seed(900)
        crossovered = gcrossover(ch1, ch2)
        self.assertEqual(crossovered.genes, [1, 2, 2, 4, 5])
        self.assertEqual(crossovered.fitness, 4)

    def test_population(self):
        goal = Chromosome([1, 2, 3, 4])
        numbers = [1, 2, 3, 4]
        population = gpopulation(numbers, goal, 10)
        self.assertEqual(len(population), 10)
        self.assertTrue(hasattr(population[0], 'fitness'))

        # test goal
        for obj in population:
            self.assertEqual(obj.goal, goal)

    def test_gselect(self):
        goal = Chromosome([1, 2, 3])
        population = [Chromosome([3, 2, 1], goal),
                      Chromosome([1, 2, 3], goal),
                      Chromosome([2, 3, 1], goal)
                ]

        maxim, secondmaxim = gselect(population)
        self.assertEqual(maxim.genes, Chromosome([1, 2, 3], goal).genes)
        self.assertEqual(secondmaxim.genes, Chromosome([3, 2, 1], goal).genes)


if __name__ == '__main__':
    unittest.main()
