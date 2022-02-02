from os.path import dirname, join
from re import findall

def test_examples():
    with open(join(dirname(__file__), "results.txt"), "r") as examples:
        iro_entries = [ i.split("\n") for i in findall( r"\d+,\d+\n.+\n.+", examples.read()) ]
        for _, r, o in iro_entries:
            print(r)
            print(o)
            assert r == o
