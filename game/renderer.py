import curses
from game.matrix import Matrix


class Renderer:

    """This objects manages the rendering phase of the game"""

    def __init__(self, screen):
        super(Renderer, self).__init__()
        self.screen = screen
        curses.curs_set(0)

    def render(self, matrix):
        # Some type checking
        if not isinstance(matrix, Matrix):
            raise TypeError

        self.updater(matrix.render())

    def updater(self, output):
        """Updates the buffer with current game status"""
        self.clearScreen()
        self.screen.addstr(output)
        self.screen.refresh()

    def clearScreen(self):
        self.screen.erase()
