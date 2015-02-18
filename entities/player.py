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
  def moveTo(self, x, y, z):
    """Moves the player to new coordinates"""
    Player.coordinates.set(x, y, z)