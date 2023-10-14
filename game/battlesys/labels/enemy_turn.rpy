label bp_enemy_turn:
    # Start--------------------------------------------------------------------------------------
    $ battlePhase.current_stage = 'Turn_start'
    $ battlePhase.phase += 1
    # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
    call check_passive_time
    if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
        return
    # CHECK NEG_STATS 
    call check_status_condition
    if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
        return
    # Effect_calculator
    python:
        player_type = battleState.player_type
        # Get skill info
        skill = battlePhase.enemy_skill
        superEffective = 1
        if skill.type in player_type.disadvantages:
            superEffective = superEffective * 2
        if skill.type in enemy.enemy_type.advantages:
            superEffective = superEffective * 0.5
        effect_list = skill.effect_list
        effect_list_size = len(effect_list)
        is_sequential = (skill.effect_sequence.upper() == 'SEQUENTIAL')
        i = 0
        inLoop = True
        enemy_name = ((battleState.enemy_team_current_stats)[0]).enemy_name
    narrator 'Enemy [enemy_name] used [skill.name].'
    while (inLoop):
        $ effect = effect_list[i]
        $ battlePhase.enemy_attack_hit = False
        # Effect_calculate------------------------------------------------------------
        $ battlePhase.current_stage = 'Effect_calculate'
        call enemy_calculate_manager
        # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
        call check_passive_time
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # CHECK NEG_STATS
        call check_status_condition
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # Effect_hit-----------------------------------------------------------------
        $ battlePhase.current_stage = 'Effect_hit'
        call enemy_hit_manager
        # CHECK PASSIVES, HP = 0, ENEMY_HP = 0
        call check_passive_time
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # CHECK NEG_STATS
        call check_status_condition
        if (battleState.player_hp == 0 or ((battleState.enemy_team_current_stats)[0]).enemy_hp == 0):
            return
        # Check in loop
        $ i += 1
        if (i == effect_list_size):
            $ inLoop = False
        elif (((not battlePhase.enemy_attack_hit) and is_sequential) or (battlePhase.enemy_attack_hit and (not is_sequential))):
            $ inLoop = False
        else:
            $ inLoop = True
    # End turn -----------------------------------------------------------------------------------
    if battlePhase.phase == 2:
        $ battlePhase.current_stage = 'Battle_end'
        # CHECK PASSIVES
        call check_passive_time
        # CHECK NEG_STATS
        call check_status_condition
        return
    else:
        call bp_player_turn

    return
        

label enemy_calculate_manager:
    python:
        # [target, stats, operator, value]
        hit = (renpy.random.randint(1, 100) <= (effect.accurace + ((battleState.enemy_team_current_stats)[0]).accurace_boost))
        battlePhase.enemy_attack_hit = hit
        if (hit):
            enemy_effect_dict = {0: 'enemy', 1: 'player'}
            battlePhase.enemy_last_effect_used = copy.copy(effect)
            # Alvo verdadeiro
            battlePhase.enemy_last_effect_used.target = enemy_effect_dict[effect.target]
            if effect.class_name == 'Status_effect':
                # if deals demage to hero -> calcular total damage 
                if (effect.target == 1 and effect.target_status.upper() == 'HP' and effect.operator == '-'):
                    inicial_damage = effect.value
                    enemy_attack = ((battleState.enemy_team_current_stats)[0]).enemy_atk
                    player_defense = battleState.player_res
                    enemy_type_boost = battleState.get_enemyHead_typeBoost(skill.type)
                    player_type_boost = battleState.get_player_typeBoost(skill.type)
                    resistance_value = min(2, max(0.1, 1 + ((enemy_type_boost - player_type_boost) * 0.25)))
                    crit = (renpy.random.randint(0, 500) < (((battleState.enemy_team_current_stats)[0]).enemy_luck))
                    if crit:
                        crit_value = 2
                    else:
                        crit_value = 1
                    final_damage = inicial_damage * (enemy_attack / player_defense) * superEffective * crit_value * resistance_value
                    battlePhase.enemy_last_effect_used.value = final_damage

    return

label enemy_hit_manager:
    if (not hit):
        narrator "It missed."
    else: 
        python:
            effect = battlePhase.enemy_last_effect_used
            player_name = battleState.player_name
            enemy_name = ((battleState.enemy_team_current_stats)[0]).enemy_name
            if effect.class_name == 'Status_effect':
                if (effect.target == 'player' and effect.target_status.upper() == 'HP' and effect.operator == '-'):
                    renpy.call('damage_scene')
                else:
                    s = effect.target_status.lower()
                    renpy.call(s + "_effect_scene")
            elif effect.class_name == 'Type_effect':
                renpy.call('type_effect_scene')
            elif effect.class_name == 'Status_condition_effect':
                renpy.call('status_condition_effect_scene')
    return