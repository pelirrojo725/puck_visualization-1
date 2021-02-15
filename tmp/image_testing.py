#!/usr/bin/env python
import sys


def read_integers(file_name):
    with open(file_name) as f:
        return [int(x) for x in f]


def cap_present(position_number, line, limit):
    print("\nTesting Position " + str(position_number))
    if line > limit:
        print("Position Empty")
    else:
        print("Position Correct")


file = sys.argv[1]

line = read_integers(file)

for i in range(len(line)):
    if i in (4, 12):
        cap_present(str(i + 1), line[i], 1500)
    else:
        cap_present(str(i + 1), line[i], 2000)
