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
    return self.x

  def setX(self, x):
    self.x = x

  def getY(self):
    return self.y

  def setY(self, y):
    self.y = y

  def getZ(self):
    return self.z

  def setZ(self, z):
    self.z = z

  def addX(self, x):
    self.x = self.x + x

  def addY(self, y):
    self.y = self.y + y

  def addZ(self, z):
    self.z = self.z + z