#!/usr/bin/env python3
from entities.player import Player
from game.renderer import Renderer
from game.input import Input

renderer = Renderer()
inputProcessor = Input()
runGame = True

# Initialize input and screen
inputProcessor.toggleInputEcho(False)
renderer.clearScreen()

while (runGame):
  userInput = inputProcessor.getPlayerInput()

  if userInput != "q":
    renderer.render()
  else:
    runGame = False

# Some cleanup before exiting..
renderer.clearScreen()
inputProcessor.toggleInputEcho(True)