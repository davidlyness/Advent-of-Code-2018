# coding=utf-8
"""Advent of Code 2018, Day 20"""

import collections


positions = []
distances = collections.defaultdict(int)
x, y = 0, 0
previous_x, previous_y = None, None
for c in open("puzzle_input").read()[1:-1]:
    if c == "(":
        positions.append((x, y))
    elif c == ")":
        x, y = positions.pop()
    elif c == "|":
        x, y = positions[-1]
    else:
        if c == "N":
            y += 1
        elif c == "E":
            x += 1
        elif c == "S":
            y -= 1
        else:
            x -= 1
        if distances[(x, y)]:
            distances[(x, y)] = min(distances[(x, y)], distances[(previous_x, previous_y)] + 1)
        else:
            distances[(x, y)] = distances[(previous_x, previous_y)] + 1
    previous_x, previous_y = x, y


def part_one():
    """Solution to Part 1"""
    return max(distances.values())


def part_two():
    """Solution to Part 2"""
    return len([d for d in distances.values() if d >= 1000])
