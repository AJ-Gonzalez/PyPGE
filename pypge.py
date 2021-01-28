#!/usr/bin/python3
import charmap as block
from itertools import islice, chain, repeat
from os import system as cmd
from time import sleep as slp


def rowGrouper(it, size, padval=None):
    it = chain(iter(it), repeat(padval))
    return list(iter(lambda: tuple(islice(it, size)), (padval,) * size))


def renderFrame(frame):
    for y in frame:
        csr = 1
        for x in y:
            if csr == len(y):
                print(x)
            else:
                print(x, end="")
            csr += 1


def buildFrame(array):
    frame = []
    grouped = rowGrouper(array, 2)
    # print(grouped)
    for y in grouped:
        row = []
        # print(y)
        for x in range(len(y[0])):
            up = y[0][x]
            down = y[1][x]
            # print(len(y) + 1, "||", up, down)
            if up == 1 and down == 1:
                row.append(block.full)
            elif up == 0 and down == 1:
                row.append(block.lowerhalf)
            elif up == 1 and down == 0:
                row.append(block.upperhalf)
            elif up == 0 and down == 0:
                row.append(block.empty)
        frame.append(row)
        # print(csr, '>>', y)

    return frame


def simpleAnimate(frames, interval):
    for frame in frames:
        renderFrame(frame)
        slp(interval)
        cmd("clear")


f = [
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
]

g = [
    [0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
]

h = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
]


f1 = buildFrame(g)
f2 = buildFrame(f)
f3 = buildFrame(h)


while True:
    simpleAnimate([f1, f2, f3], 0.3)
