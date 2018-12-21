# coding=utf-8
"""Advent of Code 2018, Day 12"""

import collections


with open("puzzle_input") as f:
    lines = f.read().split("\n")


def part_one(num_generations):
    """Solution to Part 1"""
    initial_state = lines[0].split()[-1]
    plants = collections.defaultdict(lambda: ".")
    plants.update({plant: initial_state[plant] for plant in range(len(initial_state))})
    rules = {line.split(" => ")[0]: line.split(" => ")[1] for line in lines[2:]}
    for n in range(num_generations):
        new_plants = plants.copy()
        for p in range(min(plants.keys()) - 2, max(plants.keys()) + 2):
            plant_group = plants[p-2] + plants[p-1] + plants[p] + plants[p+1] + plants[p+2]
            new_plants[p] = rules[plant_group]
        plants = new_plants
    return sum([p for p in plants if plants[p] == "#"])
