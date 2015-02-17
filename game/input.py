import os
import platform

class Input:
  """Manages player input"""
  def __init__(self):
    super(Input, self).__init__()

    try:
      from msvcrt import getch # For Windows
      self.getch = getch
    except ImportError: # For Linux and MacOS
      self.getch = self.__getch

  def getPlayerInput(self):
    """Standardized method to get player input"""
    ch = self.getch()
    return ch

  def __getch(self):
    """Custom getch for Linux and MacOS"""
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

  def toggleInputEcho(self, v):
    """Disables input echo. Notice: currently not working on Windows, search for a better solution?"""
    if platform.system() != 'Windows':
      if v:
        os.system('stty echo')
      else:
        os.system('stty -echo')