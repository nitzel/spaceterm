#!/usr/bin/env python3
from entities.player import Player
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix

# Initialize Player
Player.setName("Quill")

# Initialize I/O
renderer = Renderer()
inputProcessor = Input()
gameMatrix = Matrix(80, 24, 10)
inputProcessor.toggleInputEcho(False)
renderer.clearScreen()

runGame = True
while (runGame):
  userInput = inputProcessor.getPlayerInput()

  if userInput != "q":
    renderer.render(gameMatrix)
  else:
    runGame = False

# Some cleanup before exiting..
renderer.clearScreen()
inputProcessor.toggleInputEcho(True)