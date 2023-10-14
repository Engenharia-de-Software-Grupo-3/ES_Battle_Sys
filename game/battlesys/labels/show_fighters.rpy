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
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)], behind = ['player_box'])

    return

label show_player_atk:
    call define_sprite_info
    python:
        psi_atk = psi.atk_sprite
        esi_dmg = esi.dmg_sprite

        renpy.hide(psi_name)
        renpy.hide(esi_name)

        renpy.show(psi_atk, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_dmg, at_list=[Position(xpos=esi_x, ypos=esi_y)], behind = ['player_box'])

    return

label hide_player_atk:
    python:
        renpy.hide(psi_atk)
        renpy.hide(esi_dmg)

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)], behind = ['player_box'])
    return

label show_enemy_atk:
    call define_sprite_info
    python:
        psi_dmg = psi.dmg_sprite
        esi_atk = esi.atk_sprite

        renpy.hide(psi_name)
        renpy.hide(esi_name)

        renpy.show(psi_dmg, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_atk, at_list=[Position(xpos=esi_x, ypos=esi_y)], behind = ['player_box'])

    return

label hide_enemy_atk:
    python:
        renpy.hide(psi_dmg)
        renpy.hide(esi_atk)

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)], behind = ['player_box'])
    return
