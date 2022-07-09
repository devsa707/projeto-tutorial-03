init python:
    
    class NPC(object):
        def __init__(self,name,niceName,location, isActive):
            self.name = name
            self.niceName = niceName
            self.location = location
            self.isActive = isActive
        
        @property
        def avatar(self):
            global chapter
            global sequence
            global location
            avtr = "avatar/{}_{}_{}.png".format(self.name, str(chapter), location)
            avtrs = "avatar/{}_{}_{}_{}.png".format(self.name, str(chapter), str(sequence),location)
            anvtr = "avatar/animated/{}_{}_{}ani.png".format(self.name, str(chapter), location)
            anvtrs = "avatar/animated/{}_{}_{}_{}ani.png".format(self.name,str(chapter), str(sequence), location)
            if renpy.loadable(anvtrs):
                return anvtrs
            elif renpy.loadable(anvtr):
                return anvtr
            elif renpy.loadable(avtrs):
                return avtrs
            elif renpy.loadable(avtr):
                return avtr
            else:
                return "avatars/empty.png"
        
