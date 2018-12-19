# coding=utf-8
"""Advent of Code 2018, Day 10"""

import re

with open("puzzle_input") as f:
    data = [[int(i) for i in re.findall("-?\d+", line)] for line in f.read().split("\n")]


def find_message():
    """Draw the constellation of stars which are enclosed by the smallest bounding region."""
    region_sizes = {i: max(x + i * dx for (x, y, dx, dy) in data) - min(x + i * dx for (x, y, dx, dy) in data) +
                    max(y + i * dy for (x, y, dx, dy) in data) - min(y + i * dy for (x, y, dx, dy) in data)
                    for i in range(15000)}
    min_distance = min(region_sizes, key=region_sizes.get)
    sky = [[" "] * 150 for _ in range(500)]
    for (x, y, dx, dy) in data:
        sky[y + min_distance * dy][x + min_distance * dx - 250] = "#"
    for row in sky:
        if not all(c == " " for c in row):
            print("".join(row))
    print(min_distance)


find_message()
