from os.path import dirname, join
from re import findall
import crossover_solved as solution


def test_examples():
    with open(join(dirname(__file__), "Ejemplos.txt"), "r") as examples:
        io_pairs = [ i.split("\n")[:2] for i in findall( r".+\n.+\n", examples.read()) ]
        for i, o in io_pairs:
            try: assert solution.get_crossover_as_string(i) == o
            except ValueError as e: assert str(e) == o.lstrip("ValueError: ")