#!/usr/bin/env python3
from entities.player import Player
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix
from game.coordinates import Coordinates

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
    if userInput == "h":
      Player.moveToLeft()
    elif userInput == "k":
      Player.moveToTop()
    elif userInput == "j":
      Player.moveToBottom()
    elif userInput == "l":
      Player.moveToRight()
    elif userInput == "y":
      Player.moveToTopLeft()
    elif userInput == "u":
      Player.moveToTopRight()
    elif userInput == "n":
      Player.moveToBottomLeft()
    elif userInput == "m":
      Player.moveToBottomRight()

    gameMatrix.updateLevel()
    gameMatrix.positionPlayer()
    renderer.render(gameMatrix)
  else:
    runGame = False

# Some cleanup before exiting..
renderer.clearScreen()
inputProcessor.toggleInputEcho(True)