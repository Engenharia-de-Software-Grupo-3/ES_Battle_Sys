label battle_menu:
    while (True):
        menu player_battle_menu_choice:
            "Fight":
                $ battlePhase = Battle_phase()
                call battle_skill_menu
                if (skill_i != -1):
                    call start_battle_phase
                    return
            "Item":
                $ nada = None
                #call battle_item_menu
            "Change enemy":
                call battle_change_menu
            "Run": 
                narrator "No! There's no running from a Amongus battle!"
                # exit?

label battle_skill_menu:
    $ skills = battleState.player_skill_set
    menu player_attack_choice:
        "[skills[0].name]" if skills[0] is not None:
            $ skill_i = 0
        "[skills[1].name]" if skills[1] is not None:
            $ skill_i = 1
        "[skills[2].name]" if skills[2] is not None:
            $ skill_i = 2
        "[skills[3].name]" if skills[3] is not None:
            $ skill_i = 3
        "Return":
            $ skill_i = -1
    return

label start_battle_phase:
    python:
        player_speed = battleState.player_luck
        player_skill_choice = (battleState.player_skill_set)[skill_i]
        enemy_speed = ((battleState.enemy_team_current_stats)[0]).enemy_luck
        skill_i = ((battleState.enemy_team_current_stats)[0]).enemy_attack_pattern(battleState)
        enemy_skill_choice = (((battleState.enemy_team_current_stats)[0]).enemy_skill_set)[skill_i]
        battlePhase.attack_order(player_speed, player_skill_choice, enemy_speed, enemy_skill_choice)
    # call battle_turn_1st_attack
    if (battlePhase.fst_attacker.upper() == 'PLAYER'):
        call bp_player_turn
    else:
        call bp_enemy_turn
    $ eHead_hp = (battleState.enemy_team_current_stats[0]).enemy_hp
    if eHead_hp == 0:
        $ enemy_name = ((battleState.enemy_team_current_stats)[0]).enemy_name
        narrator "[enemy_name] fainted!"
    $ battleState.status_condition_downgrade(battleState.player_name)
    return

label battle_change_menu:
    python:
        enemy1 = battleState.enemy_team_current_stats[1]
        enemy2 = battleState.enemy_team_current_stats[2]
        enemy3 = battleState.enemy_team_current_stats[3]
        enemy4 = battleState.enemy_team_current_stats[4]
        enemy5 = battleState.enemy_team_current_stats[5]
    menu player_enemy_choice:
        "[enemy1.enemy_name]" if enemy1 is not None and enemy1.enemy_hp > 0:
            $ i = 1
        "[enemy2.enemy_name]" if enemy2 is not None and enemy2.enemy_hp > 0:
            $ i = 2
        "[enemy3.enemy_name]" if enemy3 is not None and enemy3.enemy_hp > 0:
            $ i = 3
        "[enemy4.enemy_name]" if enemy4 is not None and enemy4.enemy_hp > 0:
            $ i = 4
        "[enemy5.enemy_name]" if enemy5 is not None and enemy5.enemy_hp > 0:
            $ i = 5
        "Return":
            return
    $ esi_name = (battleState.enemy_team_current_stats[0]).enemy_sprite_info.name
    $ battleState.swap_enemy_head(i)
    call enemy_change
    return