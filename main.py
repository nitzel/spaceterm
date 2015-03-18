#!/usr/bin/env python3
from game.game import Game
from libs import unicurses


def main(screen):
    game = Game(screen)

    # Here we should parse launch options
    game.initialize("Quill")

    # Run the game
    game.loop()

    # Cleanup curses initialisation
    cleanupCurses(screen)


def cleanupCurses(screen):
    unicurses.nocbreak()
    unicurses.echo()
    screen.keypad(False)
    unicurses.endwin()


def wrapper(func):
    screen = unicurses.initscr()
    unicurses.start_color()
    unicurses.noecho()
    unicurses.cbreak()
    screen.keypad(True)

    try:
        func(screen)
    except:
        cleanupCurses(screen)


# Curses wrapper to main program (to handle screen)
wrapper(main)
