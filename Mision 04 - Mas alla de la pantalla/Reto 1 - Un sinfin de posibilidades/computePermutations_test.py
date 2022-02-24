from os.path import dirname, join
from re import findall
import computePermutations_solved as solution


def test_examples():
    with open(join(dirname(__file__), "Ejemplo.txt"), "r") as examples:
        io_pairs = [ i.split("\n")[:2] for i in findall( r".+\n.+", examples.read()) ]
        for i, o in io_pairs:
            assert solution.get_solution_string(i) == o
