class Coordinates:
  """Represents the game coordinates"""
  def __init__(self, x, y, z):
    super(Coordinates, self).__init__()
    self.x = x
    self.y = y
    self.z = z

  def get():
    return (x, y, z)

  def set(x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def getX():
    return x

  def setX(x):
    self.x = x

  def getY():
    return y

  def setY(y):
    self.y = y

  def getZ():
    return z

  def setZ(z):
    self.z = z