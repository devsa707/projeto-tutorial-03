screen nav_screen():
    frame:
        background None
        yalign 0.5
        xalign 0.5
        xsize 1200
        ysize 910
        add "ui/map/map_bg.png"
        for q in locations:
            if q.unlocked and q.map:
                imagebutton:
                    idle q.mapIcon
                    hover q.mapIcon
                    focus_mask True
                    action SetVariable("clickType","nav"), ToggleVariable("nav_menu"), Return(q.name)
                    hovered tt.Action("Go to {}".format(q.niceName))
