from os.path import dirname, join
from re import findall
import computeNeighborhood_solved as solution

def test_examples():
    with open(join(dirname(__file__), "Examples_extended.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall( r"\d+,\d+\n.+", examples.read()) ]
        for i, o in io_pairs:
            assert solution.get_neighbors_as_string(i) == o
