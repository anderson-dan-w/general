#!/usr/bin/python3

## python module
from datetime import timedelta as td
import itertools
import select
import sys
import termios
import time
import tty

## dwanderson modules
from dwanderson import Color


##############################################################################
basic_pomo = (((25, 'Work'), (5, 'Break')) * 3 + (25, 'Work') + (15, 'BREAK'))

## refactor...
def pomo_input(sec=1):
    old_tty = termios.tcgetattr(sys.stdin)
    paused = False
    response = None
    while True:
        try:
            tty.setcbreak(sys.stdin.fileno())
            if select.select([sys.stdin], [], [], sec) == ([sys.stdin], [], []):
                letter = sys.stdin.read(1).lower()
                if letter == 'q':
                    print('\r{:<30}'.format(Color.colorize("Quittin", "GRAY")),
                            end='')
                    response = False
                elif letter == 'n':
                    print('\r{:<15}'.format(Color.colorize("NEXT", "GRAY")),
                        end='')
                    time.sleep(1)
                    response = True
                elif letter in ('p', 'u') and paused:
                    response = 'unpause'
                elif letter == 'p' and not paused:
                    paused = True
                    print("\r{}".format(
                    Color.colorize("Press 'p' or 'u' to unpause!", "GRAY")),
                    end='')
            if response is not None or not paused:
                break
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
    return response


def countdown(t=td(minutes=0), caption=''):
    if caption:
        caption += ' - '
    if caption.startswith('Work'):
        clr = "GREEN"
    else:
        clr = "RED"
    try:
        while t > td(seconds=0):
            out = "\r{}{:<15}".format(Color.colorize(caption + str(t), clr),'')
            print(out, end='')
            t -= td(seconds=1)
            response = pomo_input()
            if response in (True, False):
                return response
        return True
    except KeyboardInterrupt as ki:
        return False
    finally:
        sys.stdout.write('\b' * (7 + len(caption)))
        sys.stdout.flush()


def pomodoro_cycle(pattern=basic_pomo):
    print("KEYS: 'q'-Quit; 'p'-Pause; 'p'/'u'-Unpause; 'n'-Next")
    pattern_cycle = itertools.cycle(pattern)
    running = True
    while running:
        mins, caption = next(pattern_cycle)
        running = countdown(td(minutes=mins), caption)
    return

##############################################################################
def main():
    pomodoro_cycle()

if __name__ == '__main__':
    main()
