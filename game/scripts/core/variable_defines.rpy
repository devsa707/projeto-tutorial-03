define c = Character("Christine")

default location = "bedroom"
default chapter = 1
default sequence = 0
default CLICKIES = []

label Init_Variables:

    $ CLICKIES.append(CLICKIE("living_room_sofa","living_room_sofa","living_room","item", True, "Um Sofá Confortável")) #0
    return