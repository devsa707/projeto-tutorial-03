define c = Character("Christine")

default location = "bedroom"
default chapter = 1
default sequence = 0
default CLICKIES = []
default locations = []

default tip_screen = False
default tip_text = "This is the tip screen. Tanks..." 

label Init_Variables:

    $ location.append(Place("kitchen","Kitchen", True,True))
    $ location.append(Place("living_room","Living Room", True,True))
    $ location.append(Place("bedroom","Bedroom", True,True))
    $ location.append(Place("pool","Pool", True,True))
    $ location.append(Place("bathroom","Bathroom", True,True))

    $ CLICKIES.append(CLICKIE("living_room_sofa","living_room_sofa","living_room","item", True, "Um Sofá Confortável")) #0
    return