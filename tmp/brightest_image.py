#!/usr/bin/env python3
import sys


def read_integers(file_name):
    with open(file_name) as f:
        return [int(x) for x in f]


file = sys.argv[1]

line = read_integers(file)
mean_brightness = []

for i in range(len(line)):
    mean_brightness.append(line[i])

for i in range(len(mean_brightness)):
    if mean_brightness[i] == max(mean_brightness):
        print(i + 1)
        sys.exit(0)
