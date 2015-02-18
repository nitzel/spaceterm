from entities.player import Player
from game.renderer import Renderer
from game.input import Input
from game.matrix import Matrix
from game.coordinates import Coordinates

class Game:
  """The game controller"""
  def __init__(self, screen):
    super(Game, self).__init__()
    self.renderer = None
    self.inputProcessor = None
    self.gameMatrix = None
    self.screen = screen
    self.runGame = True

  def initialize(self, playerName):
    # Initialize Player
    Player.setName(playerName)

    # Initialize I/O
    self.renderer = Renderer(self.screen)
    self.inputProcessor = Input()
    self.gameMatrix = Matrix(80, 24, 10)
    self.renderer.clearScreen()

    # Bind keys to actions
    self.inputProcessor.onKey('q', self.quit)
    self.inputProcessor.onKeys('h', Player.moveToLeft)
    self.inputProcessor.onKeys('k', Player.moveToTop)
    self.inputProcessor.onKeys('j', Player.moveToBottom)
    self.inputProcessor.onKeys('l', Player.moveToRight)
    self.inputProcessor.onKeys('y', Player.moveToTopLeft)
    self.inputProcessor.onKeys('u', Player.moveToTopRight)
    self.inputProcessor.onKeys('b', Player.moveToBottomLeft)
    self.inputProcessor.onKeys('n', Player.moveToBottomRight)

  def loop(self):
    self.gameMatrix.updateLevel()
    self.gameMatrix.positionPlayer()
    self.renderer.render(self.gameMatrix)

    while (self.runGame):
      self.inputProcessor.getPlayerInput(self.screen)
      self.gameMatrix.updateLevel()
      self.gameMatrix.positionPlayer()
      self.renderer.render(self.gameMatrix)

  def quit(self):
    """Quits the game"""
    self.runGame = False

    # Some cleanup before exiting..
    self.renderer.clearScreen()
