define c = Character("Christine")

default location = "bedroom"
default oldLocation = "bedroom"
default clickType = ""
default notification = False
default tt = Tooltip("")
default chapter = 1
default sequence = 0
default nav_menu = False

define slowDissolve = Dissolve(5.0)

default tip_screen = False
default tip_text = "This is the tip screen.\nThanks..." 

default StartEvents = ""


default CLICKIES = []
default locations = []
default NPCS = []
default computerMenu = []

label Init_Variables:

    $ computerMenu.append(("Nothing...","end"))

    $ NPCS.append(NPC("laura","Laura","kitchen",True))

    $ locations.append(Place("kitchen","Kitchen", True,True))
    $ locations.append(Place("bus","Bus Stop", True,True))
    $ locations.append(Place("garden","Garden", True,True))
    $ locations.append(Place("hotel","Hotel", True,True))

    $ CLICKIES.append(CLICKIE("bus_stop_sit","bus_stop_sit","bus","item", True, "Esperar o onibus")) #0
    return