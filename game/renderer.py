import curses
from game.matrix import Matrix
from entities.player import Player


class Renderer:

    """This objects manages the rendering phase of the game"""

    def __init__(self, screen):
        # This is the main screen which holds all the subwindows
        self.screen = screen
        screenSize = screen.getmaxyx()
        self.screenH = screenSize[0]
        self.screenW = screenSize[1]

        # In galaxyView draw the galaxy map
        self.galaxyView = screen.subwin(self.screenH - 1, self.screenW, 0, 0)

        # In statusScreen draw the status text.
        # It sits on the bottom of the main window
        self.statusScreen = screen.subwin(self.screenH - 2, 0)
        self.statusMsg = ''

    def render(self, matrix):
        # Some type checking
        if not isinstance(matrix, Matrix):
            raise TypeError

        self.clearScreen()

        for coords, cell in matrix.cells2d(
            matrix.player.getCoordinates().getZ()
        ):
            obj = None

            if matrix.player.getCoordinates().get() == coords:
                obj = matrix.player
            else:
                obj = cell

            self.galaxyView.addch(
                coords[1], coords[0],
                ord(str(obj))
            )

        self.updater()

    def updater(self):
        """Updates the buffer with current game status"""
        self.statusScreen.addstr(self.statusMsg)
        self.galaxyView.refresh()
        self.statusScreen.refresh()

    def clearScreen(self):
        self.galaxyView.erase()
        self.statusScreen.erase()

    def setStatusMsg(self, msg):
        """Set the status message to be shown on the bottom"""
        self.statusMsg = msg
