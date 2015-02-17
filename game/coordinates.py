class Coordinates:
  """Represents the game coordinates"""
  def __init__(self, x, y, z):
    super(Coordinates, self).__init__()
    self.x = x
    self.y = y
    self.z = z

  def get(self):
    return (self.x, self.y, self.z)

  def set(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def getX(self):
    return x

  def setX(self, x):
    self.x = x

  def getY(self):
    return y

  def setY(self, y):
    self.y = y

  def getZ(self):
    return z

  def setZ(self, z):
    self.z = z