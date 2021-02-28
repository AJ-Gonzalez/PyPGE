#!/usr/bin/python3
import charmap as block
from itertools import islice, chain, repeat
from os import system as cmd
from sys import argv as cliArgs
from time import sleep as slp
from glob import glob
from PIL import Image


def saveToFrame(fn, frame):
    """Build Frame:
    Does:
        Builds an array of arrays containng the characters, from an array
        of arrays with pixel values.
    Takes:
        Name:   Type:       Description:
        array   list        Nested list with integer values.
    Returns:
        List of strings.
    """
    pass


def saveToMovie(fn, frames, interval, duration):
    pass


def rowGrouper(it, size, padval=0):
    """Row Grouper:
    Does:
        Groups items in an iterable in chunks of size n.
    Takes:
        Name:   Type:       Description:
        it      iterable    Any list, tuple, etc.
        size    int         Chunk size.
        padval  any         Padding Value, defaults to None.
    Returns:
        List object with items grouped in chunks
    """
    it = chain(iter(it), repeat(padval))
    return list(iter(lambda: tuple(islice(it, size)), (padval,) * size))


def renderFrame(frame):
    """Render Frame:
    Does:
        Prints Character Art to stdout.
    Takes:
        Name:   Type:       Description:
        frame   list        Nested list with character values.
    Returns:
        None.
    """
    for y in frame:
        csr = 1
        for x in y:
            if csr == len(y):
                print(x)
            else:
                print(x, end="")
            csr += 1


def buildFrame(array):
    """Build Frame:
    Does:
        Builds an array of arrays containng the characters, from an array
        of arrays with pixel values.
    Takes:
        Name:   Type:       Description:
        array   list        Nested list with integer values.
    Returns:
        List of strings.
    """
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


def loopAnimation(frames, interval, duration):
    cmd("clear")
    frame_time = duration / (interval * len(frames))
    # print(frame_time, interval, duration)
    count = 0
    while count < frame_time:
        simpleAnimate(frames, interval)
        count += 1


def bulkFrameBuild(*args):
    ret = []
    for a in args:
        ret.append(buildFrame(a))
    return ret


def frameFromFile(filename):
    frame = []
    with open(filename) as f:
        for row in f:
            r = []
            for element in row:
                if element in ("0", "1"):
                    r.append(int(element))
            frame.append(r)
    return frame


def animationFromFolder(folder, interval, duration):
    raw_frames = glob(folder + "/*.stmf")
    raw_frames.sort()
    img_frames = glob(folder + "/*.png")
    img_frames.sort()
    if len(raw_frames) == 0:
        frames = []
        for frame in img_frames:
            frames.append(frameFromImage(frame))
        frames = bulkFrameBuild(*frames)
        loopAnimation(frames, interval, duration)
    elif len(raw_frames) != 0:
        frames = []
        for frame in raw_frames:
            frames.append(frameFromFile(frame))
        frames = bulkFrameBuild(*frames)
        loopAnimation(frames, interval, duration)


def frameFromImage(path):
    frame = []
    W = 255
    im = Image.open(path)
    pix = im.load()
    # print(im.size)  # Get the width and hight of the image for iterating over
    for j in range(im.size[0]):
        r = []
        for i in range(im.size[1]):
            if pix[i, j][0] == W and pix[i, j][1] == W and pix[i, j][2] == W:
                r.append(0)
                # print(i, j, 0)
            else:
                # print(i, j, 1)
                r.append(1)
        frame.append(r)
    return frame


def cliFn():
    """Command Line Interface:
    Does:
        Parses command line arguments and flags.
        Flags:
            Name:       Action:
            --dir, -d   Path to image or frame directory.
            --img, -i   Animate from Images (B/W only)
            --frm, -f   Animate from Plain text . frame files.
            --help, -h  Display help text and usage guide
        Flag order:
            --dir /path/ (--img/--frm)
            --help
    Takes:
        Name:   Type:       Description:
        None    None        N/A.
    Returns:
        None.
    """
    helpText="""Welcome to PyPGE:

    A simple and naive Python Pseudo-Graphics Engine.
    Built with pure python, can render ASCII pseudo-graphics
    using the Unicode block characters.

    PyPGE can be used as a module in your Python code, or as
    a CLI application.

    PyPGE CLI Flags:
    Name:       Action:
    --dir, -d   Path to image or frame directory.
    --img, -i   Animate from Images (B/W only)
    --frm, -f   Animate from Plain text . frame files.
    --help, -h  Display help text and usage guide
    """
    #print(cliArgs)
    if len(cliArgs) == 1:
        print('Use --help to see the available command line arguments')
    elif cliArgs[1] == "--dir" or cliArgs[1] == "--dir" and cliArgs[2] != "":
        print("gay")
    elif cliArgs[1] in ("-h", "--help"):
        print(helpText)
    else:
        print('Command not found')
        print('Use --help to see the available command line arguments')


if __name__ == "__main__":

    cliFn()
    # From folder
    #animationFromFolder("test_animation", 0.2, 5)
    pass
