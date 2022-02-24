from os.path import dirname, join
from re import findall
import solution_solved as solution


def test_examples():
    with open(join(dirname(__file__), "Examples.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall( r".+\n.+", examples.read()) ]
        for i, o in io_pairs:
            try: assert solution.get_angle(i) == o
            except AssertionError as e: print("XXX:", solution.get_angle(i), o)
test_examples()