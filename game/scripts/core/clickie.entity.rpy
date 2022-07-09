init python:

    class CLICKIE(object):
        def __init__(self, name, fileName, location, clickType, isActive, tip):
            self.name = name
            self.fileName = fileName
            self.location = location
            self.clickType = clickType
            self.isActive = isActive
            self.tip = tip
        
        @property
        def clickable(self):
            avtr = "Clickables/{}/{}.png".format(location,self.fileName)
            return avtr
        
        @property
        def effect(self):
            effectToPlay = "audio/effects/{}.mp3".format(self.fileName)
            if renpy.loadable(effectToPlay):
                return effectToPlay
            else:
                return "audio/effects/click_01.mp3"
    
