label damage_scene:
    if effect.target == 'player':
        $ battleState.player_hp = max(0, battleState.player_hp - effect.value)
        call show_enemy_atk
        show text "" with vpunch
        pause 0.25
        call hide_enemy_atk
        pause 0.1
    elif effect.target == 'enemy':
        $ ((battleState.enemy_team_current_stats)[0]).enemy_hp =  max(0, ((battleState.enemy_team_current_stats)[0]).enemy_hp - effect.value)
        call show_player_atk
        show text "" with vpunch
        pause 0.25
        call hide_player_atk
        pause 0.1
    if crit:
        narrator "A critical hit!"
    if superEffective > 1:
        narrator "It's super effective!"
    elif superEffective < 1:
        narrator "It's not very effective..."
    return

label hp_effect_scene:
    if effect.target == 'player':
        if effect.operator == '+':
            $ battleState.player_hp = min(battleState.original_player.hp, battleState.player_hp + effect.value)
            narrator "[player_name]'s HP was restored."
        elif effect.operator == '-':
            $ battleState.player_hp = max(0, battleState.player_hp - effect.value)
            narrator "[player_name]'s is damaged by recoil." with vpunch
        elif effect.operator == '*':
            $ battleState.player_hp = min(battleState.original_player.hp, max(0, battleState.player_hp * effect.value))
            if (effect.value > 1): 
                narrator "[player_name]'s HP rose!" 
            else: 
                narrator "[player_name]'s HP fell!"
    elif effect.target == 'enemy':
        if effect.operator == '+':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_hp =  max(((battleState.enemy_team_current_stats)[0]).original_enemy.hp, ((battleState.enemy_team_current_stats)[0]).enemy_hp + effect.value)
            narrator "[enemy_name]'s HP was restored."
        elif effect.operator == '-':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_hp = min(0, ((battleState.enemy_team_current_stats)[0]).enemy_hp - effect.value)
            narrator "[enemy_name]'s is damaged by recoil." with vpunch
        elif effect.operator == '*':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_hp = min(((battleState.enemy_team_current_stats)[0]).original_enemy.hp, max(0, ((battleState.enemy_team_current_stats)[0]).enemy_hp * effect.value))
            if (effect.value > 1): 
                narrator "[enemy_name]'s HP rose!" 
            else: 
                narrator "[enemy_name]'s HP fell!"
    return

label atk_effect_scene:
    if effect.target == 'player':
        if effect.operator == '+':
            $ battleState.player_atk = min(battleState.original_player.atk * 2, battleState.player_atk + effect.value)
            narrator "[player_name]'s Attack rose!"        
        elif effect.operator == '-':
            $ battleState.player_atk = max(1, battleState.player_atk - effect.value)
            narrator "[player_name]'s Attack fell!"
        elif effect.operator == '*':
            $ battleState.player_atk = min(battleState.original_player.atk * 2, max(1, battleState.player_atk * effect.value))
            if (effect.value > 1): 
                narrator "[player_name]'s Attack rose!" 
            else: 
                narrator "[player_name]'s Attack fell!"
    elif effect.target == 'enemy':
        if effect.operator == '+':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_atk = min(((battleState.enemy_team_current_stats)[0]).original_enemy.atk * 2, ((battleState.enemy_team_current_stats)[0]).enemy_atk + effect.value)
            narrator "[enemy_name]'s Attack rose!"        
        elif effect.operator == '-':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_atk = max(1, ((battleState.enemy_team_current_stats)[0]).enemy_atk - effect.value)
            narrator "[enemy_name]'s Attack fell!"
        elif effect.operator == '*':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_atk = min(((battleState.enemy_team_current_stats)[0]).original_enemy.atk * 2, max(1, ((battleState.enemy_team_current_stats)[0]).enemy_atk * effect.value))
            if (effect.value > 1): 
                narrator "[enemy_name]'s Attack rose!" 
            else: 
                narrator "[enemy_name]'s Attack fell!"
    return
             

label res_effect_scene:
    if effect.target == 'player':
        if effect.operator == '+':
            $ battleState.player_res = min(battleState.original_player.res * 2, battleState.player_res + effect.value)
            narrator "[player_name]'s Defense rose!"        
        elif effect.operator == '-':
            $ battleState.player_res = max(1, battleState.player_res - effect.value)
            narrator "[player_name]'s Defense fell!"
        elif effect.operator == '*':
            $ battleState.player_res = min(battleState.original_player.res * 2, max(1, battleState.player_res * effect.value))
            if (effect.value > 1): 
                narrator "[player_name]'s Defense rose!" 
            else: 
                narrator "[player_name]'s Defense fell!"
    elif effect.target == 'enemy':
        if effect.operator == '+':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_res = min(((battleState.enemy_team_current_stats)[0]).original_enemy.res * 2, ((battleState.enemy_team_current_stats)[0]).enemy_res + effect.value)
            narrator "[enemy_name]'s Defense rose!"        
        elif effect.operator == '-':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_res = max(1, ((battleState.enemy_team_current_stats)[0]).enemy_res - effect.value)
            narrator "[enemy_name]'s Defense fell!"
        elif effect.operator == '*':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_res = min(((battleState.enemy_team_current_stats)[0]).original_enemy.res * 2, max(1, ((battleState.enemy_team_current_stats)[0]).enemy_res * effect.value))
            if (effect.value > 1): 
                narrator "[enemy_name]'s Defense rose!" 
            else: 
                narrator "[enemy_name]'s Defense fell!"
    return

label luck_effect_scene:
    if effect.target == 'player':
        if effect.operator == '+':
            $ battleState.player_luck = min(battleState.original_player.luck * 2, battleState.player_luck + effect.value)
            narrator "[player_name]'s Luck rose!"        
        elif effect.operator == '-':
            $ battleState.player_luck = max(1, battleState.player_luck - effect.value)
            narrator "[player_name]'s Luck fell!"
        elif effect.operator == '*':
            $ battleState.player_luck = min(battleState.original_player.luck * 2, max(1, battleState.player_luck * effect.value))
            if (effect.value > 1): 
                narrator "[player_name]'s Luck rose!" 
            else: 
                narrator "[player_name]'s Luck fell!"
    elif effect.target == 'enemy':
        if effect.operator == '+':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_luck = min(((battleState.enemy_team_current_stats)[0]).original_enemy.luck * 2, ((battleState.enemy_team_current_stats)[0]).enemy_luck + effect.value)
            narrator "[enemy_name]'s Luck rose!"        
        elif effect.operator == '-':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_luck = max(1, ((battleState.enemy_team_current_stats)[0]).enemy_luck - effect.value)
            narrator "[enemy_name]'s Luck fell!"
        elif effect.operator == '*':
            $ ((battleState.enemy_team_current_stats)[0]).enemy_luck = min(((battleState.enemy_team_current_stats)[0]).original_enemy.luck * 2, max(1, ((battleState.enemy_team_current_stats)[0]).enemy_luck * effect.value))
            if (effect.value > 1): 
                narrator "[enemy_name]'s Luck rose!" 
            else: 
                narrator "[enemy_name]'s Luck fell!"
    return

label type_effect_scene:
    #player
    $ type_name = effect.target_type.name
    if effect.target == 'player':
        $ keys = battleState.type_boost_dictionare.keys()
        if effect.operator == '+':
            python:
                if not effect.target_type in keys:
                    battleState.type_boost_dictionare[effect.target_type] = 1
                else:
                    battleState.type_boost_dictionare[effect.target_type] += 1
            narrator "[player_name]'s [type_name] efficiency increased!"        
        elif effect.operator == '-':
            python:
                if not effect.target_type in keys:
                    battleState.type_boost_dictionare[effect.target_type] = -1
                else:
                    battleState.type_boost_dictionare[effect.target_type] -= 1
            narrator "[player_name]'s [type_name] efficiency decreased!"  
    #enemy
    elif effect.target == 'enemy':
        $ keys = ((battleState.enemy_team_current_stats)[0]).type_boost_dictionare.keys()
        if effect.operator == '+':
            python:
                if not effect.target_type in keys:                    
                    ((battleState.enemy_team_current_stats)[0]).type_boost_dictionare[effect.target_type] = 1
                else:
                    ((battleState.enemy_team_current_stats)[0]).type_boost_dictionare[effect.target_type] += 1
            narrator "[enemy_name]'s [type_name] efficiency increased!"        
        elif effect.operator == '-':
            python:
                if not effect.target_type in keys:
                    ((battleState.enemy_team_current_stats)[0]).type_boost_dictionare[effect.target_type] = -1
                else:
                    ((battleState.enemy_team_current_stats)[0]).type_boost_dictionare[effect.target_type] -= 1
            narrator "[enemy_name]'s [type_name] efficiency decreased!"  
    return

label status_condition_effect_scene:
    #player
    $ condition = effect.status_condition
    if effect.target == 'player':
        if effect.operator == '+':
            $ battleState.player_status_condition_dictionare[condition] = condition.duration
            narrator "[player_name]'s was affected by [condition.name]!"        
        elif effect.operator == '-':
            python:
                keys = battleState.player_status_condition_dictionare.keys()
                if not condition in keys:
                    renpy.say('', '[player_name] is not affected by [condition.name]!')
                else:
                    battleState.player_status_condition_dictionare.pop(condition)
                    renpy.say('', '[player_name] is no longer affected by [condition.name]!')  
    #enemy
    elif effect.target == 'enemy':
        if effect.operator == '+':
            $ ((battleState.enemy_team_current_stats)[0]).status_condition_dictionare[condition] = condition.duration
            narrator "[enemy_name] was affected by [condition.name]!"        
        elif effect.operator == '-':
            python:
                keys = ((battleState.enemy_team_current_stats)[0]).status_condition_dictionare.keys()
                if not condition in keys:
                    renpy.say('', '[enemy_name] is not affected by [condition.name]!')
                else:
                    ((battleState.enemy_team_current_stats)[0]).status_condition_dictionare.pop(condition)
                    renpy.say('', '[enemy_name] is no longer affected by [condition.name]!') 
    return