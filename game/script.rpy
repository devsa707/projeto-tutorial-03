label start:
    call Init_Variables
    $ Playing = True
    while Playing:
        window hide
        $ Notification = False  
        $ ThisChaptersHint = "hint_{}_{}".format(str(chapter),str(sequence))
        $ AutoEvent = "AutoEvent_{}_{}".format(str(chapter), str(sequence))
        $ AutoEventHappen = False
        if renpy.has_label(ThisChaptersHint):
            call expression ThisChaptersHint

        if StartEvents <> "":
            if renpy.has_label(StartEvents):
                call expression StartEvents
                $ StartEvents = ""

        if renpy.has_label(AutoEvent):
            $ AutoEventHappen = True
            call expression AutoEvent
            $ Next()
        
        if not AutoEventHappen:
            $ UIreturn = renpy.call_screen("mainUI")
            if clickType == "character":
                $ LabelToCall = "{}_{}_{}".format(UIreturn,str(chapter), str(sequence))
                $ LabelToCallFallback = "{}_blank".format(UIreturn)
                if renpy.has_label(LabelToCall):
                    call expression LabelToCall
                elif renpy.has_label(LabelToCallFallback):
                    call expression LabelToCallFallback                      

        if clickType == "item":
            $ LabelToCall = "{}_{}_{}".format(UIreturn,str(chapter), str(sequence))
            $ LabelToCallFallback = "{}_blank".format(UIreturn)
            if renpy.has_label(LabelToCall):
                call expression LabelToCall
            elif renpy.has_label(LabelToCallFallback):
                call expression LabelToCallFallback                      

        if clickType == "nav":
            python:
                for q in locations:
                    if UIreturn == q.name and q.unlocked:
                        oldLocation = location
                        location = UIreturn
                    elif UIreturn == q.name and not q.unlocked:
                        renpy.call("no_nav")

        if clickType == "Help":
            $ LabelToCall = "hint_{}_{}".format(str(chapter), str(sequence))
            if renpy.has_label(LabelToCall):
                call expression LabelToCall
    return
