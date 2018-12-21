# coding=utf-8
"""Advent of Code 2018, Day 16"""

import collections
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


with open("puzzle_input_a") as f:
    samples = [{
        "prev": {
            0: int(match.group("pr0")),
            1: int(match.group("pr1")),
            2: int(match.group("pr2")),
            3: int(match.group("pr3")),
        },
        "opcode": int(match.group("opcode")),
        "a": int(match.group("a")),
        "b": int(match.group("b")),
        "c": int(match.group("c")),
        "next": {
            0: int(match.group("nr0")),
            1: int(match.group("nr1")),
            2: int(match.group("nr2")),
            3: int(match.group("nr3")),
        },
    } for entry in f.read().split("\n\n")
        for match in [re.search(
            ".*\[(?P<pr0>\d+), (?P<pr1>\d+), (?P<pr2>\d+), (?P<pr3>\d+)]\n(?P<opcode>\d+) (?P<a>\d+) (?P<b>\d+) "
            "(?P<c>\d+)\n.*\[(?P<nr0>\d+), (?P<nr1>\d+), (?P<nr2>\d+), (?P<nr3>\d+)\]", entry
        )]]
with open("puzzle_input_b") as f:
    instructions = [{
        "opcode": int(match.group("opcode")),
        "a": int(match.group("a")),
        "b": int(match.group("b")),
        "c": int(match.group("c"))
    } for entry in f.read().split("\n")
        for match in [re.search("(?P<opcode>\d+) (?P<a>\d+) (?P<b>\d+) (?P<c>\d+)", entry)]
    ]


def part_one():
    """Solution to Part 1"""
    matching_samples = 0
    for s in samples:
        valid_opcodes = 0
        ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
        for op in ops:
            prev = s['prev'].copy()
            prev[s['c']] = op(prev, s['a'], s['b'])
            if prev == s['next']:
                valid_opcodes += 1
        if valid_opcodes >= 3:
            matching_samples += 1
    return matching_samples


def part_two():
    """Solution to Part 2"""
    candidates = collections.defaultdict(set)
    opcode_map = {}
    for s in samples:
        ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
        for op in ops:
            prev = s['prev'].copy()
            prev[s['c']] = op(prev, s['a'], s['b'])
            if prev == s['next']:
                candidates[s['opcode']].add(op.__name__)
    while len(opcode_map) < 16:
        for op in candidates:
            if len(candidates[op]) == 1:
                opcode_function = list(candidates[op])[0]
                opcode_map[op] = opcode_function
                for other_op in candidates:
                    if opcode_function in candidates[other_op]:
                        candidates[other_op].remove(opcode_function)
    registers = {0: 0, 1: 0, 2: 0, 3: 0}
    for instruction in instructions:
        registers[instruction['c']] = globals()[opcode_map[instruction['opcode']]](
            registers, instruction['a'], instruction['b']
        )
    return registers[0]
