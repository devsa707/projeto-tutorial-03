screen character_screen():
    for q in NPCS:
        if q.location == location and q.isActive:
            if q.avatar[-7] != "ani.png":
                imagebutton:
                    idle q.avatar
                    hover q.avatar
                    action SetVariable("clickType","Character"), Return(q.name)
                    focus_mask True
                    hovered tt.Action(q.niceName)
            else:
                imagebutton:
                    idle anim.Filmstrip(q.avatar,(1920,1080),(4,8),0.08333,32,loop=True)
                    hover anim.Filmstrip(q.avatar,(1920,1080),(4,8),0.08333,32,loop=True)
                    focus_mask True
                    action SetVariable("clickType","Character"), Return(q.name)
                    focus_mask True
                    hovered tt.Action(q.niceName)