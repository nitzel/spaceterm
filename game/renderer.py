import curses
from game.matrix import Matrix
import game.constants


class Renderer:

    """This objects manages the rendering phase of the game"""

    def __init__(self, screen):
        # This is the root screen which holds all the subwindows
        # it doesn't actually hold any content, it's just here
        # because of curses.wrapper()
        self.screen = screen
        screenSize = screen.getmaxyx()
        self.screenH = screenSize[0]
        self.screenW = screenSize[1]

        # This is the main window that will hold all the game views
        self.mainScreen = screen.subwin(self.screenH, self.screenW, 0, 0)
        # In galaxyView draw the galaxy map
        self.galaxyView = self.mainScreen.subwin(
            game.constants.MATRIX_H + 2, game.constants.MATRIX_W + 2, 0, 0)

        # In statusScreen draw the status text.
        # It sits on the bottom of the main window
        self.statusScreen = self.mainScreen.subwin(self.screenH - 2, 1)
        self.statusMsg = ''

        curses.init_pair(
            1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(
            2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(
            3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(
            4, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(
            5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(
            6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(
            7, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def render(self, matrix):
        # Some type checking
        if not isinstance(matrix, Matrix):
            raise TypeError

        self.clearScreen()

        for coords, cell in matrix.cells2d(
            matrix.player.getCoordinates().getZ()
        ):
            obj = None
            style = curses.A_DIM
            colorPair = game.constants.COLOR_WK  # Default white on black

            if matrix.player.getCoordinates().get() == coords:
                obj = matrix.player
            else:
                obj = cell

            if obj.style == game.constants.STYLE_BOLD:
                style = curses.A_BOLD
            elif obj.style == game.constants.STYLE_DIM:
                style = curses.A_DIM
            elif obj.style == game.constants.STYLE_STANDOUT:
                style = curses.A_STANDOUT
            elif obj.style == game.constants.STYLE_REVERSE:
                style = curses.A_REVERSE
            elif obj.style == game.constants.STYLE_BLINK:
                style = curses.A_BLINK

            colorPair = obj.color

            try:
                self.galaxyView.addch(
                    coords[1] + 1, coords[0] + 1,
                    ord(str(obj)),
                    style | curses.color_pair(colorPair)
                )
            except:
                self.statusMsg += ' OB' + str(coords[1]) + ':' + str(coords[0])

        self.updater()

    def updater(self):
        """Updates the buffer with current game status"""
        self.statusScreen.addstr(self.statusMsg)
        self.galaxyView.border('|', '|', '-', '-', '+', '+', '+', '+')
        self.mainScreen.refresh()
        self.galaxyView.refresh()
        self.statusScreen.refresh()

    def clearScreen(self):
        self.galaxyView.erase()
        self.statusScreen.erase()

    def setStatusMsg(self, msg):
        """Set the status message to be shown on the bottom"""
        self.statusMsg = msg
