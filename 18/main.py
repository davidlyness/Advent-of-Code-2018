# coding=utf-8
"""Advent of Code 2018, Day 18"""

import collections


def step(current_grid):
    """Step forward an iteration."""
    next_grid = []
    num_rows, num_columns = len(current_grid), len(current_grid[0])
    for row in range(num_rows):
        next_row = []
        for col in range(num_columns):
            counts = collections.defaultdict(int)
            for c in range(-1, 2):
                for r in range(-1, 2):
                    if r == 0 and c == 0:
                        continue
                    r_adj, c_adj = row + r, col + c
                    if 0 <= r_adj < num_rows and 0 <= c_adj < num_columns:
                        counts[current_grid[r_adj][c_adj]] += 1
            if current_grid[row][col] == "." and counts["|"] >= 3:
                next_row.append("|")
            elif current_grid[row][col] == "|" and counts["#"] >= 3:
                next_row.append("#")
            elif current_grid[row][col] == "#" and counts["#"] >= 1 and counts["|"] >= 1:
                next_row.append("#")
            elif current_grid[row][col] == "#":
                next_row.append(".")
            else:
                next_row.append(current_grid[row][col])
        next_grid.append(next_row)
    return next_grid


def get_grid_value(grid, num_minutes):
    """Get total value of grid after some amount of time."""
    seen_grids = {}
    values = {}
    grid_loop_start, grid_loop_end = 0, 0
    for current_minute in range(1, num_minutes + 1):
        grid = step(grid)
        grid_key = "".join("".join(row) for row in grid)
        counts = collections.Counter(grid_key)
        values[current_minute] = counts["|"] * counts["#"]
        if grid_key in seen_grids:
            grid_loop_start = seen_grids[grid_key]
            grid_loop_end = current_minute
            break
        seen_grids[grid_key] = current_minute
    period = grid_loop_end - grid_loop_start
    cycle_containing = num_minutes - grid_loop_start
    if period and cycle_containing:
        num_minutes = grid_loop_start + cycle_containing % period
    return values[num_minutes]


def part_one():
    """Solution to Part 1"""
    return get_grid_value(starting_grid, 10)


def part_two():
    """Solution to Part 2"""
    return get_grid_value(starting_grid, 1000000000)


starting_grid = [list(map(str, line.strip())) for line in open("puzzle_input").read().split("\n")]

