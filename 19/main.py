# coding=utf-8
"""Advent of Code 2018, Day 19"""

import re


def addr(r, a, b):
    """addr op"""
    return r[a] + r[b]


def addi(r, a, b):
    """addi op"""
    return r[a] + b


def mulr(r, a, b):
    """mulr op"""
    return r[a] * r[b]


def muli(r, a, b):
    """muli op"""
    return r[a] * b


def banr(r, a, b):
    """banr op"""
    return r[a] & r[b]


def bani(r, a, b):
    """bani op"""
    return r[a] & b


def borr(r, a, b):
    """borr op"""
    return r[a] | r[b]


def bori(r, a, b):
    """bori op"""
    return r[a] | b


# noinspection PyUnusedLocal
def setr(r, a, b):
    """setr op"""
    return r[a]


# noinspection PyUnusedLocal
def seti(r, a, b):
    """seti op"""
    return a


def gtir(r, a, b):
    """gtir op"""
    if a > r[b]:
        return 1
    else:
        return 0


def gtri(r, a, b):
    """gtri op"""
    if r[a] > b:
        return 1
    else:
        return 0


def gtrr(r, a, b):
    """gtrr op"""
    if r[a] > r[b]:
        return 1
    else:
        return 0


def eqir(r, a, b):
    """eqir op"""
    if a == r[b]:
        return 1
    else:
        return 0


def eqri(r, a, b):
    """eqri op"""
    if r[a] == b:
        return 1
    else:
        return 0


def eqrr(r, a, b):
    """eqrr op"""
    if r[a] == r[b]:
        return 1
    else:
        return 0


registers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
with open("puzzle_input") as f:
    data = f.read().split("\n")
    instruction_pointer = int(data[0][4])
    instructions = [{
        "op": match.group("op"),
        "a": int(match.group("a")),
        "b": int(match.group("b")),
        "c": int(match.group("c"))
    } for entry in data[1:]
        for match in [re.search("(?P<op>[a-z]+) (?P<a>\d+) (?P<b>\d+) (?P<c>\d+)", entry)]
    ]


def part_one():
    """Solution to Part 1"""
    instruction_value = 0
    while instruction_value < len(instructions):
        registers[instruction_pointer] = instruction_value
        instruction = instructions[instruction_value]
        registers[instruction['c']] = globals()[instruction['op']](registers, instruction['a'], instruction['b'])
        instruction_value = registers[instruction_pointer]
        instruction_value += 1
    return registers[0]
