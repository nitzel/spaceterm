from entities.base import Base


class Star(Base):

    """The Star objects represents a star"""

    symbol = 'O'

    def setClass(self, cl):
        """
        Sets the star class, or spectral type.
        Uses the Harvard spectral clssification only for simplicity,
        but it could be extended to include also Yerkes.

        See: http://en.wikipedia.org/wiki/Stellar_classification
        """
        self.classification = cl  # TODO: do some validation?
