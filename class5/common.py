import pandas as pd
import sys

def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))

def print_tour(tour):
    filename = "output_" + sys.argv[1][6] + ".csv"
    pd.DataFrame({"index": tour}).to_csv(filename, index=False, encoding="utf-8")
