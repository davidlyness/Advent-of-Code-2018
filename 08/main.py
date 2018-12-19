# coding=utf-8
"""Advent of Code 2018, Day 8"""


with open("puzzle_input") as f:
    nums = [int(n) for n in f.read().split()]


def part_one(data):
    """Solution to Part 1"""
    num_children, num_metadata, data = data[0], data[1], data[2:]
    total_metadata_score = 0
    for _ in range(num_children):
        data, metadata_score = part_one(data)
        total_metadata_score += metadata_score
    total_metadata_score += sum(data[:num_metadata])
    if num_children > 0:
        return data[num_metadata:], total_metadata_score
    else:
        return data[num_metadata:], total_metadata_score


def part_two(data):
    """Solution to Part 2"""
    num_children, num_metadata, data = data[0], data[1], data[2:]
    values = []
    for _ in range(num_children):
        data, node_value = part_two(data)
        values.append(node_value)
    if num_children > 0:
        return data[num_metadata:], sum(values[i-1] for i in data[:num_metadata] if 0 < i <= len(values))
    else:
        return data[num_metadata:], sum(data[:num_metadata])
