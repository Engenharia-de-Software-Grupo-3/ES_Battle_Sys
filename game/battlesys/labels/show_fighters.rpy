label enemy_change:
    $ renpy.hide(esi_name)
    $ fala = battleState.enemy_team_name + " sent out " + (battleState.enemy_team_current_stats[0]).enemy_name + '!'
    $ renpy.say('', fala)
    call show_fighters
    return

label define_sprite_info:
    python:
        psi = battleState.player_sprite_info
        psi_name = psi.name
        psi_x = psi.x_position
        psi_y = psi.y_position

        esi = (battleState.enemy_team_current_stats[0]).enemy_sprite_info
        esi_name = esi.name
        esi_x = esi.x_position
        esi_y = esi.y_position
    return

label show_fighters:
    call define_sprite_info
    python:

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)])

    return

screen hp_bars_1v1:
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.7
        xmaximum 200
        text battleState.player_name
        bar value battleState.player_hp range battleState.original_player.hp

    vbox:
        spacing 20
        xalign 0.05
        yalign 0.2
        xmaximum 200
        text ((battleState.enemy_team_current_stats)[0]).enemy_name
        bar value ((battleState.enemy_team_current_stats)[0]).enemy_hp range ((battleState.enemy_team_current_stats)[0]).original_enemy.hp

label show_player_atk:
    call define_sprite_info
    python:
        psi_atk = psi.atk_sprite
        esi_dmg = esi.dmg_sprite

        renpy.hide(psi_name)
        renpy.hide(esi_name)

        renpy.show(psi_atk, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_dmg, at_list=[Position(xpos=esi_x, ypos=esi_y)])

    return

label hide_player_atk:
    python:
        renpy.hide(psi_atk)
        renpy.hide(esi_dmg)

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)])
    return

label show_enemy_atk:
    call define_sprite_info
    python:
        psi_dmg = psi.dmg_sprite
        esi_atk = esi.atk_sprite

        renpy.hide(psi_name)
        renpy.hide(esi_name)

        renpy.show(psi_dmg, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_atk, at_list=[Position(xpos=esi_x, ypos=esi_y)])

    return

label hide_enemy_atk:
    python:
        renpy.hide(psi_dmg)
        renpy.hide(esi_atk)

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)])
    return
