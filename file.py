import os


class file:
    location = None
    filename = None

    def __init__(self, location, filename):
        self.location = location
        self.filename = filename


def getfilelocation():
    return file.location


def setfilelocation(loc):
    file.location = loc


def getfilename():
    return file.filename


def setfilename(name):
    path = os.path.basename(name)
    (fname, ext) = os.path.splitext(path)
    file.filename = fname
