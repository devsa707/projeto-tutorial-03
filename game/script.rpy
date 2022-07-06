label start:
    call Init_Variables
    $ Playing = True
    while Playing:
        menu:
            c "Hi"
            "hi":
                pass
            "Bye":
                $ Playing = False
        call screen tutScreen("teste de tela \n isso é uma nova linha")
    return
