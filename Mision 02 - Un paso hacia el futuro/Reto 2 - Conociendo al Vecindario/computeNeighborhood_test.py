from os.path import dirname, join
from re import findall
import computeNeighborhood_solved as solution

def test_examples():
    with open(join(dirname(__file__), "Examples.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall( r"\d+,\d+\n.+", examples.read()) ]
        for i, o in io_pairs:
            col, row = [int(j) for j in i.split(",")]
            if col not in range(solution.CELLS_PER_SIDE) or row not in range(solution.CELLS_PER_SIDE):
                string = 'cell index range error'
            else:
                string = ''.join([''.join(str(element).split()) for element in solution.grid[col][row].neighbors])
            assert string == o