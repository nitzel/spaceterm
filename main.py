#!/usr/bin/env python3
from game.game import Game
from curses import wrapper

def main(screen):
  game = Game(screen)

  # Here we should parse launch options
  game.initialize("Quill")

  # Run the game
  game.loop()

# Curses wrapper to main program (to handle screen)
wrapper(main)