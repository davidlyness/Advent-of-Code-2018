# coding=utf-8
"""Advent of Code 2018, Day 1"""

with open("puzzle_input") as f:
    changes = [int(n) for n in f.read().split()]


def part_one():
    """Solution to Part 1"""
    return sum(changes)


def part_two():
    """Solution to Part 2"""
    seen_values = set()
    current_position = 0
    current_value = 0
    while current_value not in seen_values:
        seen_values.add(current_value)
        current_value += changes[current_position]
        current_position = (current_position + 1) % len(changes)
    return current_value
