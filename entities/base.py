class Base:

    """This object implements all the common entities methods"""

    def __init__(self, uid, name):
        super(Base, self).__init__()
        self.uid = uid
        self.name = name

    def getUid(self):
        return self.uid

    def getName(self):
        return self.name
