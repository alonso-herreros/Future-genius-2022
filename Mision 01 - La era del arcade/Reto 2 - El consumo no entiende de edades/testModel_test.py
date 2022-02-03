from os.path import dirname, join
from re import findall
import testModel_solved as solution


def test_test_data():
    with open(join(dirname(__file__), "Test_data.txt"), "r") as test_data:
        io_pairs = [i.split("\n") for i in findall(r"\d+\n\d+", test_data.read())]
        for i, o in io_pairs:
            assert solution.infereAge(int(i)) == int(o)
