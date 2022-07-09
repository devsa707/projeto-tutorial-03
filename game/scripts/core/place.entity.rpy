init python:

    class Place(object):
        def __init__(self,name,niceName, unlocked, map):
            self.name = name
            self.niceName = niceName
            self.unlocked = unlocked
            self.map = map

        @property
        def mapIcon(self):
            ReturnValue = "ui/map/map_{}".format(self.name)
            return ReturnValue