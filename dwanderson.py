#!/usr/bin/python3

## python module
import collections
from datetime import timedelta as td
import functools
import itertools
import math
import os
import sys
import select
import termios
import time
import tty

##############################################################################
## reading in my basic text files
playground = os.path.dirname(os.path.realpath(__file__)) + "/"
text_dir = playground + "text/"
texts = [text_dir + f for f in os.listdir(text_dir)]

words = set()
for fname in [f for f in texts if f.endswith(".dict")]:
    with open(fname) as fh:
        _w = str(fh.read()).replace("\r","\n").replace("\n\n","\n")
        _w = _w.upper().split("\n")
        words.update(_w)


##############################################################################
class Color(object):
    """ Simple accessors for linux(xterm?/ANSI?) color sequences and printing
        things in those colors. I may amend over time, but allows user to add
        a color if they know the ANSI code.
    """
    def __init__(self):
        pass

    prefix = '\033['
    NONE = prefix + "0m"
    RED = prefix + "91m"
    GREEN = prefix + "92m"
    BLUE = prefix + "94m"
    GRAY = prefix + "97m"

    _colors = collections.defaultdict(lambda: Color._colors["NONE"])
    _colors.update(NONE=NONE, RED=RED, GREEN=GREEN, BLUE=BLUE, GRAY=GRAY)

    def colorize(string, color):
        color = color.upper()
        return Color._colors[color] + string + Color._colors["NONE"]

    def addColor(name, number):
        name = name.upper()
        setattr(Color, name, Color.prefix + str(number) + "m")
        Color._colors.update({name : getattr(Color, name)})


##############################################################################
def time_me(func):
    """ Wraps an arbitrary function with a timer, so it will print out how long
        the function took to complete
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            timer = kwargs.pop("time_me")
        except KeyError as e:
            timer = True
        start = time.time()
        response = func(*args, **kwargs)
        if timer:
            print("Took ~{:0.06} seconds".format(time.time() - start))
        return response
    return wrapper


##############################################################################
def get_terminal_size():
    """ Return the tuple containing width, height, in line count.
        I think I got this from StackOverflow?
    """
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ),
                    '1234')
        except:
            return None
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return cr[1], cr[0]


##############################################################################
def print_list(some_list, npline=None):
    """ Print a list (or set) to the terminal, wrapped approriately as per
        the width of the terminal
    """
    if isinstance(some_list, set):
        some_list = list(some_list)
    if not some_list:
        print()
        return
    some_list = sorted(some_list)
    width, _h = get_terminal_size()  # ignore height, _h
    max_width = len(max(some_list, key=len)) + 1  # for space separator
    if npline is None:  ## number-per-line
        npline = width // max_width
    for line in range(math.ceil(len(some_list) / npline)):
        nelts = min(npline, len(some_list[line * npline:]))
        for idx in range(nelts):
            elt = some_list[line * npline + idx]
            print("{: <{}}".format(elt, max_width), end="")
        print()
    return


##############################################################################
def is_written_to(sec=0):
    """ Pause for @sec seconds, check if there was (new?) input at the terminal
    """
    return select.select([sys.stdin], [], [], sec) == ([sys.stdin], [], [])

def check_for_input(sec=0):
    """ Simple wrapper, to make sure the tty stays sensible when checking for
        user input via @is_written_to
    """
    old_tty = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        if is_written_to(sec):
            return sys.stdin.read(1)
    finally:
        termios.tcsetatr(sys.stdin, termios.TCSADRAIN, old_tty)
    return ''

