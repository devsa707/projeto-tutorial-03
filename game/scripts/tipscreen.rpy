screen tipScreen(tip):
    drag:
        drag_name "Hint"
        xalign 0.5
        yalign 0.5
        drag_handle (0,0,1.0,1.0)

        frame:
            xpadding 25
            ypadding 30
            xalign 0.5
            yalign 0.5
            xmaximum 610
            ymaximum 400
            has vbox
            label "Hint" xmaximum 400
            text tip