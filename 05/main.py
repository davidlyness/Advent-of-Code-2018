# coding=utf-8
"""Advent of Code 2018, Day 5"""

import string

with open("puzzle_input") as f:
    data = f.read().strip()


def part_one(polymer=data):
    """Solution to Part 1"""
    unit_pairs = ["{}{}".format(c.upper(), c) for c in string.ascii_lowercase] +\
                 ["{}{}".format(c, c.upper()) for c in string.ascii_lowercase]
    previous_length = None
    while previous_length is None or len(polymer) != previous_length:
        previous_length = len(polymer)
        for pair in unit_pairs:
            polymer = polymer.replace(pair, "")
    return len(polymer)


def part_two():
    """Solution to Part 2"""
    min_length, min_letter = None, None
    for letter in string.ascii_lowercase:
        reduced_polymer = data.replace(letter, "").replace(letter.upper(), "")
        reduced_length = part_one(reduced_polymer)
        if min_letter is None or reduced_length < min_length:
            min_letter = letter
            min_length = reduced_length
    return min_length


print(part_two())
