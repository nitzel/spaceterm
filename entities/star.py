from entities.base import Base


class Star(Base):

    """The Star objects represents a star"""

    def __init__(self, uid, name):
        super(Star, self).__init__(uid, name)
