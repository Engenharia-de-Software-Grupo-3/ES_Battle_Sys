label prepare_battle:
    python:
        # Types
        normal = Type("Normal")
        fire = Type("Fire")
        water = Type("Water", [fire])
        grass = Type("Grass", [water], [fire])

        fire.advantages.append(grass)
        fire.disadvantages.append(water)
        water.disadvantages.append(grass)

        # Create Effects
        dmg50 = Status_effect(1, 'hp', '-', 50, 100)
        selfDmg50 = Status_effect(0, 'hp', '-', 50, 100)
        selfdmg25 = Status_effect(0, 'hp', '-', 25, 100)
        heal50 = Status_effect(0, 'hp', '+', 50, 100)
        hitkill = Status_effect(1, 'hp', '*', 0, 25)
        fire_boost = Type_effect(0, fire, '+', 100)

        # Skill
        heatVision = Skill('Throw Objects', 'Sequential', fire, [dmg50, dmg50, dmg50], 0, None)
        frostBreath = Skill('High level coffee', 'Sequential', water, [dmg50], 0, None)
        sunCharge = Skill('Compile', 'Sequential', grass, [fire_boost], -1, None)
        megaPunch = Skill("Dynamic Punch", 'Inverted', normal, [hitkill, selfDmg50], 1, None)

        punch = Skill('Punch', 'Sequential', normal, [dmg50], 0, None)
        gun = Skill('Gun', 'Sequential', fire, [dmg50, dmg50], 1, None)
        burrito = Skill('Burrito', 'Sequential', grass, [dmg50], 0, None)

        # Status_conditions
        def poison_effect(afflicted, battleState, battlePhase):
            if afflicted == 'player':
                battleState.player_hp -= 25
                renpy.say('', '[battleState.player_name] is hurt by poison!')
            elif afflicted == 'enemy':
                ((battleState.enemy_team_current_stats)[0]).enemy_hp -= 25
                renpy.say('', '[((battleState.enemy_team_current_stats)[0]).enemy_name] is hurt by poison!')

        poison = Status_condition('Poison', 'Battle_End', poison_effect, 3)
        podre = Status_condition_effect(1, '+', poison, 100)
        burrito.effect_list.append(podre)

        # Passives
        def regen(battleState, y):
            battleState.player_hp = min(battleState.original_player.hp, battleState.player_hp + 67)
            renpy.say('', "[battleState.player_name]'s HP was restored by [battleState.player_passive.name]")

        def backstab(battleState, y):
            battleState.player_hp = max(0, battleState.player_hp - 69)
            renpy.say('', 'Enemy [battleState.enemy_team_passive.name] damaged [battleState.player_name]')

        underSun = Passive('Under the Sun', 'Battle_End', regen)
        backstab = Passive('Backstab', 'Battle_End', backstab)

        # Player
        pxy = Sprite_info("java_battle", 0.5, 1.0, "java_attack", "java_dmg")
        player = Pc("Java", normal, 1000, 100, 100, 100, underSun, pxy, [heatVision, frostBreath, sunCharge, megaPunch])
        
        # Enemys
        e1xy = Sprite_info("redamongus", 0.78, 0.45, "atkamongus", "dmgamongus")
        e2xy = Sprite_info("mexigus", 0.78, 0.45, "atkamongus", "dmgamongus")
        e3xy = Sprite_info("amonguns", 0.74, 0.45, "atkamongus", "dmgamongus")

        def attackPattern(state):
            return 0

        red = Enemy('Redongus', normal, 500, 50, 50, 100, [punch], e1xy, attackPattern)
        yellow = Enemy('Mexicongus', grass, 500, 50, 50, 100, [burrito], e2xy, attackPattern)
        blue = Enemy('Amonguns', fire, 500, 50, 50, 100, [gun], e3xy, attackPattern)

        # Enemy_team
        enemyTeam = Enemy_team("The Skeld", backstab, [red, yellow, blue, None, None, None], None)

        # Battle_state
        battleState = Battle_state(player, enemyTeam)

    show player_box
    show enemy_box
    call show_fighters
    show screen hp_bars_1v1 onlayer master
    call turn_start
    return