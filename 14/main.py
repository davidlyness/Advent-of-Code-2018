# coding=utf-8
"""Advent of Code 2018, Day 14"""


with open("puzzle_input") as f:
    recipe_input = f.read()


def part_one():
    """Solution to Part 1"""
    scoreboard = "37"
    elf1, elf2 = 0, 1
    while len(scoreboard) < int(recipe_input) + 10:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (1 + elf1 + int(scoreboard[elf1])) % len(scoreboard)
        elf2 = (1 + elf2 + int(scoreboard[elf2])) % len(scoreboard)
    return "".join([str(n) for n in scoreboard[-10:]])


def part_two():
    """Solution to Part 2"""
    scoreboard = "37"
    elf1, elf2 = 0, 1
    while recipe_input != scoreboard[-5:]:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (1 + elf1 + int(scoreboard[elf1])) % len(scoreboard)
        elf2 = (1 + elf2 + int(scoreboard[elf2])) % len(scoreboard)
    return len(scoreboard) - len(recipe_input)
