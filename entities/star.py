from entities.base import Base
import game.constants


class Star(Base):

    """The Star objects represents a star (or a blackhole!)"""

    symbol = 'O'
    decoration = game.constants.STYLE_BOLD
    color = game.constants.COLOR_WK

    def setClass(self, cl):
        """
        Sets the star class, or spectral type.
        Uses the Harvard spectral clssification only for simplicity,
        but it could be extended to include also Yerkes.

        See: http://en.wikipedia.org/wiki/Stellar_classification

        TODO Drastically reduct chance of generating a blackhole!
        """
        self.classification = cl  # TODO: do some validation?
        self.color = game.constants.STAR_COLORS[cl]
