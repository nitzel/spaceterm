import platform
import os

class Renderer:
  """This objects manages the rendering phase of the game"""

  def __init__(self):
    super(Renderer, self).__init__()
    self.screenBuffer = ''
  
  def render(self):
    self.updater()
    print(self.screenBuffer)

  def updater(self):
    """Updates the buffer with current game status"""
    if platform.system() == 'Windows':
      os.system('cls')
    else:
      os.system('clear')

    # TODO Space/Galaxy/Sector rendering
    # TODO Player position
    # TODO Entities position
    self.screenBuffer = '@'