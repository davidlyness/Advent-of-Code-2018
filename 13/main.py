# coding=utf-8
"""Advent of Code 2018, Day 13"""


class Cart:
    """Cart class."""
    def __init__(self, position, direction):
        self.has_crashed = False
        self.next_turn = "left"
        self.position = position
        self.direction = direction


def part_one():
    """Solution to Part 1"""
    tracks = {}
    carts = []
    for y, line in enumerate(open("puzzle_input")):
        for x, c in enumerate(line):
            if c in ("\\", "/", "+"):
                tracks[complex(x, y)] = c
            elif c == "^":
                carts.append(Cart(complex(x, y), -1j))
            elif c == "v":
                carts.append(Cart(complex(x, y), 1j))
            elif c == "<":
                carts.append(Cart(complex(x, y), -1))
            elif c == ">":
                carts.append(Cart(complex(x, y), 1))
    while True:
        carts.sort(key=lambda cart: (cart.position.real, cart.position.imag))
        for i, cart1 in enumerate(carts):
            cart1.position += cart1.direction
            if cart1.position in tracks:
                track = tracks[cart1.position]
                if track == "\\":
                    if cart1.direction.real:
                        cart1.direction *= 1j
                    else:
                        cart1.direction *= -1j
                elif track == "/":
                    if cart1.direction.real:
                        cart1.direction *= -1j
                    else:
                        cart1.direction *= 1j
                elif track == "+":
                    if cart1.next_turn == "left":
                        cart1.direction *= -1j
                        cart1.next_turn = "forwards"
                    elif cart1.next_turn == "forwards":
                        cart1.next_turn = "right"
                    else:
                        cart1.direction *= 1j
                        cart1.next_turn = "left"
            for j, cart2 in enumerate(carts):
                if i != j and cart1.position == cart2.position:
                    return "{},{}".format(int(cart1.position.real), int(cart1.position.imag))


def part_two():
    """Solution to Part 2"""
    tracks = {}
    carts = []
    for y, line in enumerate(open("puzzle_input")):
        for x, c in enumerate(line):
            if c in ("\\", "/", "+"):
                tracks[complex(x, y)] = c
            elif c == "^":
                carts.append(Cart(complex(x, y), -1j))
            elif c == "v":
                carts.append(Cart(complex(x, y), 1j))
            elif c == "<":
                carts.append(Cart(complex(x, y), -1))
            elif c == ">":
                carts.append(Cart(complex(x, y), 1))
    while len(carts) != 1:
        carts.sort(key=lambda cart: (cart.position.real, cart.position.imag))
        for i, cart1 in enumerate(carts):
            if not cart1.has_crashed:
                cart1.position += cart1.direction
                if cart1.position in tracks:
                    track = tracks[cart1.position]
                    if track == "\\":
                        if cart1.direction.real:
                            cart1.direction *= 1j
                        else:
                            cart1.direction *= -1j
                    elif track == "/":
                        if cart1.direction.real:
                            cart1.direction *= -1j
                        else:
                            cart1.direction *= 1j
                    elif track == "+":
                        if cart1.next_turn == "left":
                            cart1.direction *= -1j
                            cart1.next_turn = "forwards"
                        elif cart1.next_turn == "forwards":
                            cart1.next_turn = "right"
                        else:
                            cart1.direction *= 1j
                            cart1.next_turn = "left"
                for j, cart2 in enumerate(carts):
                    if i != j and cart1.position == cart2.position:
                        cart1.has_crashed = True
                        cart2.has_crashed = True
        carts = [cart for cart in carts if not cart.has_crashed]
    return "{},{}".format(int(carts[0].position.real), int(carts[0].position.imag))
