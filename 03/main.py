# coding=utf-8
"""Advent of Code 2018, Day 3"""

import numpy
import re

with open("puzzle_input") as f:
    claims = [{
        "id": int(match.group("id")),
        "left": int(match.group("left")),
        "top": int(match.group("top")),
        "width": int(match.group("width")),
        "height": int(match.group("height")),
    } for line in f.read().split("\n")
      for match in [re.search("#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)", line)]]
grid = numpy.zeros((
    max([c['left'] + c['width'] for c in claims]),
    max([c['top'] + c['height'] for c in claims])
))
for claim in claims:
    grid[claim['left']:claim['left']+claim['width'], claim['top']:claim['top']+claim['height']] += 1


def part_one():
    """Solution to Part 1"""
    return len(numpy.where(grid > 1)[0])


def part_two():
    """Solution to Part 2"""
    return [c['id'] for c in claims
            if grid[c['left']:c['left']+c['width'], c['top']:c['top']+c['height']].max() == 1][0]
