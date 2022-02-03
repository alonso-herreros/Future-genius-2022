from os.path import dirname, join
from re import findall
import damageMultiplierCalculator_solved as solution

def test_examples():
    with open(join(dirname(__file__), "Examples.txt"), "r") as examples:
        io_pairs = [ i.split("\n") for i in findall(r".+\nx\d.*", examples.read()) ]
        for i, o in io_pairs:
            assert solution.computeDamageMultiplier(*i.split(",")) == float(o.lstrip("x"))
