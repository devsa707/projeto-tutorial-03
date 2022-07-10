screen top_bar_screen():
    add "ui/topbar.png"

    imagebutton:
        xpos 1860
        ypos 0
        idle "ui/icons/help.png"
        hover "ui/icons/help.png"
        action SetVariable("clickType","Help"), ToggleVariable("tip_screen"), Return ("Help")
        focus_mask True
        hovered tt.Action("Show / Hide hint")
    
    imagebutton:
        xpos 1810
        ypos 0
        idle "ui/icons/map.png"
        hover "ui/icons/map.png"
        action ToggleVariable("nav_menu"), Return("Nav")
        focus_mask True
        hovered tt.Action("toggle the Map")

    if location <> oldLocation:
        imagebutton:
            xpos 1760
            ypos 0
            idle "ui/icons/back.png"
            hover "ui/icons/back.png"
            action SetVariable("clickType","Nav"), Return(oldLocation)
            hovered tt.Action ("Go back to previous location")
