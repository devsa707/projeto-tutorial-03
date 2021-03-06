init python:
    persistent._clear()
    config.use_cpickle = True
    renpy.music.register_channel("one",mixer="music", loop=None, stop_on_mute=True,tight=False,file_prefix='', file_suffix='',buffer_queue=True)
    renpy.music.register_channel("two",mixer="sound", loop=None, stop_on_mute=True,tight=False,file_prefix='', file_suffix='',buffer_queue=True)
    _preferences.set_volume('sound',0.5)
    _preferences.set_volume('music',0.2)

    def BGstr_chap():
        global location
        global chapter
        global sequence
        outputStr = "backgrounds/{}_{}_{}.jpg".format(location,chapter,sequence)
        if renpy.loadable(outputStr):
            return outputStr
        outputStr = "backgrounds/{}_{}.jpg".format(location,chapter)
        if renpy.loadable(outputStr):
            return outputStr
        outputStr = "backgrounds/{}.jpg".format(location)
        if renpy.loadable(outputStr):
            return outputStr
        return "backgrounds/background.jpg"
        
    def Unlock(place):
        global locations
        for q in locations:
            if q.name == place:
                q.unlocked = True

    def Next():
        global sequence
        sequence += 1

    def GoTo(self,num):
        global locations
        self.location = locations[num].name
        renpy.retain_after_load()