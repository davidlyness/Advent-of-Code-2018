# coding=utf-8
"""Advent of Code 2018, Day 11"""


with open("puzzle_input") as f:
    grid_serial_number = int(f.read())

cells = [[int(str((((i + 1) + 10) * (j + 1) + grid_serial_number) * ((i + 1) + 10))[-3]) - 5
          for j in range(300)]
         for i in range(300)]


def calculate_square_value(x, y, size):
    """Calculate power value of a square, given an (x, y) top-left coordinate and square size."""
    return sum(cells[x + dx][y + dy] for dy in range(size) for dx in range(size))


def part_one():
    """Solution to Part 1"""
    power_squares = {(i+1, j+1): calculate_square_value(i, j, 3)
                     for j in range(297) for i in range(297)}
    return max(power_squares, key=power_squares.get)


def part_two():
    """Solution to Part 2. Not intended to run to completion.
    Keep an eye on the printed output and attempt a solution submission when it seems stable.
    Examples on https://adventofcode.com/2018/day/11 seem to stabilise between size 10 and size 20."""
    power_squares = {}
    max_square = None
    for size in range(1, 301):
        power_squares.update({(i+1, j+1, size): calculate_square_value(i, j, size)
                             for j in range(300 - size) for i in range(300 - size)})
        max_square = max(power_squares, key=power_squares.get)
        print(max_square)
    return max_square
