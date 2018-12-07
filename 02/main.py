# coding=utf-8
"""Advent of Code 2018, Day 2"""

import collections


with open("puzzle_input") as f:
    boxes = f.read().split()


def part_one():
    """Solution to Part 1"""
    two_char_ids = [box for box in boxes if 2 in collections.Counter(box).values()]
    three_char_ids = [box for box in boxes if 3 in collections.Counter(box).values()]
    return len(two_char_ids) * len(three_char_ids)


def part_two():
    """Solution to Part 2"""
    for i in range(len(boxes)):
        for j in range(i, len(boxes)):
            same_chars = [c1 for c1, c2 in zip(boxes[i], boxes[j]) if c1 == c2]
            if len(boxes[i]) - len(same_chars) == 1:
                return "".join(same_chars)
