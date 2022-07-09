screen TooTipScreen():
    if tt.value <> "":
        frame:
            xalign 0.5
            ypos 85
            vbox:
                text "{font=gui/fonts/Montserrat.ttf}[tt.value]" color "#FFF" outlines[(0, "#000", 0,0)] size 18 bold False
    