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
    unicurses.keypad(screen, False)
    unicurses.endwin()


def wrapper(func):
    screen = unicurses.initscr()
    unicurses.start_color()
    unicurses.noecho()
    unicurses.cbreak()
    unicurses.keypad(screen, True)

    try:
        func(screen)
    finally:
        cleanupCurses(screen)


# Curses wrapper to main program (to handle screen)
wrapper(main)
