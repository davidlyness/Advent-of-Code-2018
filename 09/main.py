# coding=utf-8
"""Advent of Code 2018, Day 8"""

import collections
import re

with open("puzzle_input") as f:
    match = re.search("(?P<players>\d+) players; last marble is worth (?P<points>\d+) points", f.read())
    num_players = int(match.group("players"))
    num_points = int(match.group("points"))


def run_marble_game(players, max_points):
    """Run marble game with specified number of players and points."""
    marbles = collections.deque([0])
    scores = collections.defaultdict(int)
    for marble in range(1, max_points + 1):
        if marble % 23 > 0:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            scores[marble % players] += marble + marbles.pop()
            marbles.rotate(-1)
    return max(scores.values())


# Part One
print(run_marble_game(num_players, num_points))

# Part Two
print(run_marble_game(num_players, num_points * 100))
