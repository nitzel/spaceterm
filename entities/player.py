from game.coordinates import Coordinates

class Player:
  """The player object manages the current player"""
  def __init__(self, name):
    super(Player, self).__init__()
    self.name = name
    self.coordinates = Coordinates(0, 0, 0)

  def getCoordinates(self):
    """Returns the coordinates object with player position"""
    return self.coordinates

  def moveTo(self, x, y, z):
    """Moves the player to new coordinates"""
    self.coordinates.set(x, y, z)