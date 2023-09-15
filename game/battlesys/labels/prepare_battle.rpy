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
        hitkill = Status_effect(1, 'hp', '*', 0, -1)
        fire_boost = Type_effect(0, fire, '+', 100)

        # Skill
        heatVision = Skill('Heat Vision', 'Sequential', fire, [dmg50, dmg50, dmg50], 0, None)
        frostBreath = Skill('Frost Breath', 'Sequential', water, [dmg50], 0, None)
        sunCharge = Skill('Praise the Sun', 'Sequential', grass, [fire_boost], -1, None)
        megaPunch = Skill("Serious Punch", 'Inverted', normal, [hitkill, selfDmg50], 1, None)

        punch = Skill('Punch', 'Sequential', normal, [dmg50], 0, None)
        gun = Skill('Gun', 'Sequential', fire, [dmg50], 1, None)
        burrito = Skill('Burrito', 'Sequential', grass, [dmg50], 0, None)

        # Status_conditions
        poison = Status_condition('Poison', 'Turn End', [selfdmg25])
        podre = Status_condition_effect(1, '+', poison, 50)
        burrito.effect_list.append(podre)

        # Passives
        def sunTrigger(x, y):
            return True

        underSun = Passive('Under the Sun', 'Turn End', sunTrigger, [heal50])
        backstab = Passive('Backstab', 'Turn End', sunTrigger, [dmg50])

        # Player
        pxy = Sprite_info("superman", 0.1, 0.6)
        player = Pc("Superman", normal, 1000, 100, 100, 250, underSun, pxy, [heatVision, frostBreath, sunCharge, megaPunch])
        
        # Enemys
        e1xy = Sprite_info("redamongus", 0.9, 0.6)
        e2xy = Sprite_info("mexigus", 0.9, 0.6)
        e3xy = Sprite_info("amonguns", 0.9, 0.6)

        def attackPattern(state):
            return 0

        red = Enemy('Redongus', normal, 100, 50, 50, 100, [punch], e1xy, attackPattern)
        yellow = Enemy('Mexicongus', grass, 100, 50, 50, 100, [burrito], e2xy, attackPattern)
        blue = Enemy('Amonguns', fire, 100, 50, 50, 100, [gun], e3xy, attackPattern)

        # Enemy_team
        enemyTeam = Enemy_team("Amongus", backstab, [red, yellow, blue, None, None, None], None)

        # Battle_state
        battleState = Battle_state(player, enemyTeam)

    call show_fighters
    show screen hp_bars_1v1
    call turn_start

screen hp_bars_1v1:
    vbox:
        spacing 20
        xalign (battleState.player_sprite_info.x_position - 0.05)
        yalign (battleState.player_sprite_info.y_position + 0.1)
        xmaximum 200
        text battleState.player_name
        bar value battleState.player_hp range battleState.original_player.hp

    vbox:
        spacing 20
        xalign (((battleState.enemy_team_current_stats)[0]).enemy_sprite_info.x_position + 0.05)
        yalign (((battleState.enemy_team_current_stats)[0]).enemy_sprite_info.y_position + 0.1)
        xmaximum 200
        text ((battleState.enemy_team_current_stats)[0]).enemy_name
        bar value ((battleState.enemy_team_current_stats)[0]).enemy_hp range ((battleState.enemy_team_current_stats)[0]).original_enemy.hp