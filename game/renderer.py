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

        # Hide the cursor
        curses.curs_set(0)

    def render(self, matrix):
        # Some type checking
        if not isinstance(matrix, Matrix):
            raise TypeError

        m = matrix.get()
        self.clearScreen()

        for y, rows in enumerate(m):
            for x, layers in enumerate(rows):
                self.galaxyView.addch(
                    y, x,
                    ord(str(layers[Player.getCoordinates().getZ()]))
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
