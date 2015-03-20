from libs import unicurses
from game.matrix import Matrix
import game.constants


class Renderer:

    """This objects manages the rendering phase of the game"""

    def __init__(self, screen):
        # This is the root screen which holds all the subwindows
        # it doesn't actually hold any content, it's just here
        # because of unicurses.wrapper()
        self.screen = screen
        screenSize = unicurses.getmaxyx(screen)
        self.screenH = screenSize[0]
        self.screenW = screenSize[1]

        # This is the main window that will hold all the game views
        self.mainScreen = unicurses.subwin(screen, self.screenH, self.screenW, 0, 0)
        # In galaxyView draw the galaxy map
        self.galaxyView = unicurses.subwin(self.mainScreen,
            game.constants.MATRIX_H + 2, game.constants.MATRIX_W + 2, 0, 0)

        # In statusScreen draw the status text.
        # It sits on the bottom of the main window
        self.statusScreen = unicurses.subwin(self.mainScreen, self.screenH - 2, 1, 0, 0); # 0,0 as beginXY correct?
        self.statusMsg = ''

        unicurses.init_pair(
            1, unicurses.COLOR_RED, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            2, unicurses.COLOR_GREEN, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            3, unicurses.COLOR_YELLOW, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            4, unicurses.COLOR_BLUE, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            5, unicurses.COLOR_MAGENTA, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            6, unicurses.COLOR_CYAN, unicurses.COLOR_BLACK)
        unicurses.init_pair(
            7, unicurses.COLOR_BLACK, unicurses.COLOR_WHITE)

    def render(self, matrix):
        # Some type checking
        if not isinstance(matrix, Matrix):
            raise TypeError

        self.clearScreen()

        for coords, obj in matrix.cells2d(
            matrix.player.getCoordinates().getZ()
        ):
            style = unicurses.A_DIM
            colorPair = game.constants.COLOR_WK  # Default white on black

            if obj.style == game.constants.STYLE_BOLD:
                style = unicurses.A_BOLD
            elif obj.style == game.constants.STYLE_DIM:
                style = unicurses.A_DIM
            elif obj.style == game.constants.STYLE_STANDOUT:
                style = unicurses.A_STANDOUT
            elif obj.style == game.constants.STYLE_REVERSE:
                style = unicurses.A_REVERSE
            elif obj.style == game.constants.STYLE_BLINK:
                style = unicurses.A_BLINK

            colorPair = obj.color

            try:
                self.galaxyView.addch(
                    coords[1] + 1, coords[0] + 1,
                    ord(str(obj)),
                    style | unicurses.color_pair(colorPair)
                )
            except:
                self.statusMsg += ' OB' + str(coords[1]) + ':' + str(coords[0])

        self.updater()

    def updater(self):
        """Updates the buffer with current game status"""
        unicurses.waddstr(self.statusScreen, self.statusMsg)
        unicurses.border2(self.galaxyView, '|', '|', '-', '-', '+', '+', '+', '+')
        unicurses.refresh()
        #self.mainScreen.refresh()
        #self.galaxyView.refresh()
        #self.statusScreen.refresh()

    def clearScreen(self):
        # maybe unicurses.erase() instead?
        unicurses.wclear(self.galaxyView)
        unicurses.wclear(self.statusScreen)

    def setStatusMsg(self, msg):
        """Set the status message to be shown on the bottom"""
        self.statusMsg = msg
