import os
import platform
import curses

class Input:
  """Manages player input"""
  def __init__(self):
    super(Input, self).__init__()

  def getPlayerInput(self, screen):
    """Standardized method to get player input"""
    ch = screen.get_wch()
    return ch