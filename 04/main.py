# coding=utf-8
"""Advent of Code 2018, Day 4"""

import re

with open("puzzle_input") as f:
    entries = sorted(f.read().split("\n"))

guards = {}
guard, sleep_minute, wake_minute = None, None, None

for entry in entries:
    match = re.search(".*:(?P<minute>\d+)\] Guard #(?P<id>\d+) begins shift", entry)
    if match:
        guard = int(match.group("id"))
    else:
        match = re.search(".*:(?P<minute>\d+)\] falls asleep", entry)
        if match:
            sleep_minute = int(match.group("minute"))
        else:
            match = re.search(".*:(?P<minute>\d+)\] wakes up", entry)
            wake_minute = int(match.group("minute"))
            if guard not in guards:
                guards[guard] = {}
            for minute in range(sleep_minute, wake_minute):
                if minute not in guards[guard]:
                    guards[guard][minute] = 0
                guards[guard][minute] += 1


def part_one():
    """Solution to Part 1"""
    max_guard, max_guard_time_asleep, max_minute = None, None, None
    for g in guards:
        guard_time_asleep = sum(guards[g].values())
        if max_guard_time_asleep is None or guard_time_asleep > max_guard_time_asleep:
            max_guard = g
            max_guard_time_asleep = guard_time_asleep
    for m in guards[max_guard]:
        if max_minute is None or guards[max_guard][m] > guards[max_guard][max_minute]:
            max_minute = m
    return max_guard * max_minute


def part_two():
    """Solution to Part 2"""
    guard_max_minutes = {g: max(guards[g].keys(), key=guards[g].get) for g in guards}
    max_guard = max(guard_max_minutes, key=lambda g: guards[g][guard_max_minutes[g]])
    return max_guard * guard_max_minutes[max_guard]
