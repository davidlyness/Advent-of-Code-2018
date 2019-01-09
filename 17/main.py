# coding=utf-8
"""Advent of Code 2018, Day 17"""

import collections


def find_water_overflow(water_x, water_y, step):
    """Locate bucket overflow in a given direction."""
    while True:
        next_cell = grid[water_y + 1][water_x]
        current_cell = grid[water_y][water_x]
        if current_cell == "#":
            water_x -= step
            return water_x, False
        elif next_cell == ".":
            sources.append((water_x, water_y))
            return water_x, True
        elif current_cell == "|" and next_cell == "|":
            return water_x, True
        water_x += step


scans = []
for line in open("puzzle_input").read().split("\n"):
    clay_start, clay_range = line.split(", ")
    clay_start = int(clay_start.split("=")[1])
    range1, range2 = map(int, clay_range[2:].split(".."))
    scans.append((line[0], clay_start, range1, range2))

x_min, x_max = float("inf"), float("-inf")
y_min, y_max = float("inf"), float("-inf")
for range_type, point, range_start, range_end in scans:
    if range_type == "x":
        x_min, x_max = min(point, x_min), max(point, x_max)
        y_min, y_max = min(range_start, y_min), max(range_end, y_max)
    else:
        x_min, x_max = min(range_start, x_min), max(range_end, x_max)
        y_min, y_max = min(point, y_min), max(point, y_max)
x_min -= 1
x_max += 1
grid = [["." for _ in range(x_max - x_min)] for _ in range(y_max + 1)]

for range_type, point, range_start, range_end in scans:
    for i in range(range_start, range_end + 1):
        if range_type == "x":
            x, y = point, i
        else:
            x, y = i, point
        grid[y][x - x_min] = "#"

sources = [(500 - x_min, 0)]
while sources:
    x_source, y_source = sources.pop()
    y_source += 1
    while y_source <= y_max:
        cell = grid[y_source][x_source]
        if cell == "|":
            break
        elif cell == ".":
            grid[y_source][x_source] = "|"
            y_source += 1
        elif cell in("#", "~"):
            y_source -= 1
            left_amount, left_overflow = find_water_overflow(x_source, y_source, -1)
            right_amount, right_overflow = find_water_overflow(x_source, y_source, 1)
            for x in range(left_amount, right_amount + 1):
                if left_overflow or right_overflow:
                    grid[y_source][x] = "|"
                else:
                    grid[y_source][x] = "~"

symbol_counts = collections.Counter(cell for row in grid[y_min:] for cell in row)


def part_one():
    """Solution to Part 1"""
    return symbol_counts["~"] + symbol_counts["|"]


def part_two():
    """Solution to Part 2"""
    return symbol_counts["~"]
