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
default tip_text = "This is the tip screen. Tanks..." 

default StartEvents = ""


default CLICKIES = []
default locations = []
default NPCS = []
default computerMenu = []

label Init_Variables:

    $ computerMenu.append(("Nothing...","end"))

    $ NPCS.append(NPC("laura","Laura","kitchen",True))

    $ location.append(Place("kitchen","Kitchen", True,True))
    $ location.append(Place("living_room","Living Room", True,True))
    $ location.append(Place("bedroom","Bedroom", True,True))
    $ location.append(Place("pool","Pool", True,True))
    $ location.append(Place("bathroom","Bathroom", True,True))

    $ CLICKIES.append(CLICKIE("living_room_sofa","living_room_sofa","living_room","item", True, "Um Sofá Confortável")) #0
    return