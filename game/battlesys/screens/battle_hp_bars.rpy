screen hp_bars_1v1:
    # Player Name
    vbox:
        xalign 0.89
        yalign 0.46
        text battleState.player_name.upper() at right
    # Player HP
    vbox:
        spacing 1
        xalign 0.825
        yalign 0.525
        xmaximum 400
        text "HP:"
        bar value battleState.player_hp range battleState.original_player.hp
        text (str(battleState.player_hp) + "/" + str(battleState.original_player.hp))
    # Enemy Name
    vbox:
        xalign 0.285
        yalign 0.105
        text ((battleState.enemy_team_current_stats)[0]).enemy_name.upper() at right
    # ENEMY HP
    vbox:
        spacing 1
        xalign 0.145
        yalign 0.14
        xmaximum 400
        text "HP:"
        bar value ((battleState.enemy_team_current_stats)[0]).enemy_hp range ((battleState.enemy_team_current_stats)[0]).original_enemy.hp