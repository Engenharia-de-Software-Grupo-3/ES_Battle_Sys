screen battle_main_menu:
    grid 2 2:
        xalign 0.88
        yalign 0.865
        spacing 60
        frame:
            xpadding 100
            xmaximum 300
            xminimum 300
            textbutton "Fight" at center action [SetVariable('battle_choice', 'Fight'), Return()]
        frame:
            xpadding 100
            xmaximum 300
            xminimum 300
            textbutton "Item" at center action [SetVariable('battle_choice', 'Item'), Return()]
        frame:
            xpadding 70
            xmaximum 300
            xminimum 300
            textbutton "Enemies" at center action [SetVariable('battle_choice', 'Enemies'), Return()]
        frame:
            xpadding 110
            xmaximum 300
            xminimum 300
            textbutton "Run" at center action [SetVariable('battle_choice', 'Run'), Return()]

screen battle_skill_menu:
    vbox:
        spacing 1
        xalign 0.7
        yalign 0.875
        xmaximum 400
        style_prefix 'battle'
        if skills[0] is not None:
            textbutton button0 action [SetVariable('skill_i', 0), Return()]
        if skills[1] is not None:
            textbutton button1 action [SetVariable('skill_i', 1), Return()]
        if skills[2] is not None:
            textbutton button2 action [SetVariable('skill_i', 2), Return()]
        if skills[3] is not None:
            textbutton button3 action [SetVariable('skill_i', 3), Return()]
    vbox:
        xalign 0.95
        yalign 0.95
        xmaximum 400
        style_prefix 'battle'
        textbutton '{size=*1.5}⏎{/size}' action Return() 

screen battle_enemy_menu:
    vbox:
        spacing 20
        xalign 0.67
        yalign 0.86
        xmaximum 400
        style_prefix 'battle'
        # enemy 0
        if enemy0 is not None and enemy0.enemy_hp > 0:
            textbutton button0
        # enemy 1
        if enemy1 is None:
            textbutton ''
        elif enemy1.enemy_hp <= 0:
            textbutton '{color=#a08f8f}[button1]{/color}'
        else:
            textbutton button1 action [SetVariable('i', 1), Return()]
        # enemy 2
        if enemy2 is None:
            textbutton ''
        elif enemy2.enemy_hp <= 0:
            textbutton '{color=#a08f8f}[button2]{/color}'
        else:
            textbutton button2 action [SetVariable('i', 2), Return()]
    vbox:
        spacing 20
        xalign 0.92
        yalign 0.86
        xmaximum 800
        xminimum 300
        style_prefix 'battle'
        # enemy 3
        if enemy3 is None:
            textbutton ''
        elif enemy3.enemy_hp <= 0:
            textbutton '{color=#a08f8f}[button3]{/color}'
        else:
            textbutton button3 action [SetVariable('i', 3), Return()]
        # enemy 4
        if enemy4 is None:
            textbutton ''
        elif enemy4.enemy_hp <= 0:
            textbutton '{color=#a08f8f}[button4]{/color}'
        else:
            textbutton button4 action [SetVariable('i', 4), Return()]
        # enemy 5
        if enemy5 is None:
            textbutton ''
        elif enemy5.enemy_hp <= 0:
            textbutton '{color=#a08f8f}[button5]{/color}'
        else:
            textbutton button5 action [SetVariable('i', 5), Return()]
    vbox:
        xalign 0.95
        yalign 0.95
        style_prefix 'battle'
        textbutton '{size=*1.5}⏎{/size}' action Return() 

