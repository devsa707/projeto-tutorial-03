screen buttonScreen():
    for q in CLICKIES:
        if q.location == location and q.isActive:
            imagebutton:
                idle q.clickable
                hover q.clickable
                action SetVariable("clickType",q.clickType), Return (q.name)
                focus_mask True
                hovered tt.Action(q.tip), renpy.play(q.effect, "two")