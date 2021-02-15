#!/usr/bin/env python
import sys


def read_integers(file_name):
    with open(file_name) as f:
        return [int(x) for x in f]


file = sys.argv[1]

line = read_integers(file)

line_index = int(sys.argv[2]) - 1

if line[line_index] <= 1000:
    print(0)
    sys.exit(0)
if line[line_index] <= 1500:
    print(1)
    sys.exit(0)
if line[line_index] <= 2000:
    print(2)
    sys.exit(0)
if line[line_index] > 2000:
    print(3)
    sys.exit(0)
