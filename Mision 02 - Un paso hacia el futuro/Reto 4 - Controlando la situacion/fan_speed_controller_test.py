from os.path import dirname, join
from re import findall
import fan_speed_controller_solved as solution


def test_examples():
    with open(join(dirname(__file__), "Examples.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall( r"\d+\n.+", examples.read()) ]
        for i, o in io_pairs:
            assert solution.proportionalControllerStep(int(i)) == int(o.rstrip("V"))