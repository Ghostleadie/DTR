class folder:

    folderlocation = None

    def __init__(self, folderlocation):
        self.folderlocation = folderlocation


def getfolderlocation():
    return folder.folderlocation


def setfolderlocation(location):
    folder.folderlocation = location