from entities.player import Player

class Matrix:
  """Matrix that holds all the game entities"""
  def __init__(self, w, h, z):
    super(Matrix, self).__init__()
    self.w = w
    self.h = h
    self.z = z
    self.matrix = []
    self.player = None
    self.__initialize()
  
  def __initialize(self):
    """Initialize the matrix with empty space"""
    self.matrix = []
    
    for y in range(self.h):
      self.matrix.append([])
      for x in range(self.w):
        self.matrix[y].append([])
        for z in range(self.z):
          self.matrix[y][x].append([])
          self.matrix[y][x][z] = '.'

  def render(self):
    """Render the matrix"""
    sbuffer = ''
    for y in self.matrix:
      for yx in y:
        sbuffer = sbuffer + yx[Player.getCoordinates().getZ()]
      
      sbuffer = sbuffer + '\n'

    return sbuffer

  def updateLevel(self):
    """Updates the current level in the matrix"""
    self.__initialize() # Mockup, do actual level updating

  def positionPlayer(self):
    self.matrix[Player.getCoordinates().getY()][Player.getCoordinates().getX()][Player.getCoordinates().getZ()] = '@'