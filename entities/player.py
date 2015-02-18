from game.coordinates import Coordinates

class Player:
  """The player object manages the current player"""
  name = ''
  coordinates = Coordinates(0, 0, 0)

  @staticmethod
  def setName(name):
    Player.name = name

  @staticmethod
  def getCoordinates():
    """Returns the coordinates object with player position"""
    return Player.coordinates

  @staticmethod
  def moveTo(coordinates):
    """Moves the player to new coordinates"""
    Player.coordinates = coordinates

  @staticmethod
  def moveToTop():
    Player.coordinates.addY(-1)

  @staticmethod
  def moveToTopRight():
    Player.coordinates.addY(-1)
    Player.coordinates.addX(1)

  @staticmethod
  def moveToRight():
    Player.coordinates.addX(1)

  @staticmethod
  def moveToBottomRight():
    Player.coordinates.addY(1)
    Player.coordinates.addX(1)

  @staticmethod
  def moveToBottom():
    Player.coordinates.addY(1)

  @staticmethod
  def moveToBottomLeft():
    Player.coordinates.addY(1)
    Player.coordinates.addX(-1)

  @staticmethod
  def moveToLeft():
    Player.coordinates.addX(-1)

  @staticmethod
  def moveToTopLeft():
    Player.coordinates.addY(-1)
    Player.coordinates.addX(-1)