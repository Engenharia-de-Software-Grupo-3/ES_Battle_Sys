label enemy_change:
    $ renpy.hide(psi_name)
    $ renpy.hide(esi_name)
    call show_fighters
    return

label show_fighters:

    python:
        psi = battleState.player_sprite_info
        psi_name = psi.name
        psi_x = psi.x_position
        psi_y = psi.y_position

        esi = (battleState.enemy_team_current_stats[0]).enemy_sprite_info
        esi_name = esi.name
        esi_x = esi.x_position
        esi_y = esi.y_position

        renpy.show(psi_name, at_list=[Position(xpos=psi_x, ypos=psi_y)])
        renpy.show(esi_name, at_list=[Position(xpos=esi_x, ypos=esi_y)])

    return