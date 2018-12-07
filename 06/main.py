# coding=utf-8
"""Advent of Code 2018, Day 6"""

import collections


def distance(a, b):
    """Determine Manhattan distance between tuples a and b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open("puzzle_input") as f:
    coordinates = [tuple(map(int, line.split(", "))) for line in f.read().split("\n")]
x_min, x_max = min(c[0] for c in coordinates), max(c[0] for c in coordinates)
y_min, y_max = min(c[1] for c in coordinates), max(c[1] for c in coordinates)


def part_one():
    """Solution to Part 1"""
    regions = collections.defaultdict(lambda: 0)
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            distances = {c: distance([x, y], c) for c in coordinates}
            min_distance = min(distances.values())
            min_coordinates = [c for c, d in distances.items() if d == min_distance]
            if len(min_coordinates) == 1:
                regions[min_coordinates[0]] += 1
    return max(regions.values())


def part_two():
    """Solution to Part 2"""
    return sum([
        sum(distances.values()) < 10000
        for x in range(x_min, x_max)
        for y in range(y_min, y_max)
        for distances in [{c: distance([x, y], c) for c in coordinates}]
    ])
