from os.path import dirname, join
from re import findall
import solution


def test_examples():
    with open(join(dirname(__file__), "Examples.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall( r".+\n.+", examples.read()) ]
        for i, o in io_pairs:
            assert solution.get_angle_as_string(i) == o
            #except AssertionError as e: print("XXX:", solution.get_angle_as_string(i), o)