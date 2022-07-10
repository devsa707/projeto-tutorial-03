screen top_bar_screen():
    add "ui/topbar.png"

    imagebutton:
        xpos 1860
        ypos 0
        idle "ui/icon-help.png"
        hover "ui/icon-help.png"
        action SetVariable("clickType","Help"), ToggleVariable("tip-screen"), Return ("Help")
        focus_mask True
        hovered tt.Action("Show / Hide hint")
    
    imagebutton:
        xpos 1810
        ypos 0
        idle "ui/icon-map.png"
        hover "ui/icon-map.png"
        action ToggleVariable("nav_menu"), Return("Nav")
        focus_mask True
        hovered tt.Action("toggle the Map")

    if location <> oldlocation:
        imagebutton:
            xpos 1760
            ypos 0
            idle "ui/back.png"
            hover "ui/back.png"
            action SetVariable("clickType","Nav"), Return(oldlocation)
            hovered tt.Action ("Go back to previous location")