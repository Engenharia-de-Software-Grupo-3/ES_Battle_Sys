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

        # Skills
        heatVision = Skill('Heat Vision', 'Sequencial', fire, [dmg50], 0, None)
        frostBreath = Skill('Frost Breath', 'Sequencial', water, [dmg50], 0, None)
        sunCharge = Skill('Praise the Sun', 'Sequencial', grass, [fire_boost], -1, None)
        megaPunch = Skill("Serious Punch", 'Inverted', normal, [hitkill, selfDmg50], 1, None)

        punch = Skill('Punch', 'Sequencial', normal, [dmg50], 0, None)
        gun = Skill('Gun', 'Sequencial', fire, [dmg50], 1, None)
        burrito = Skill('Burrito', 'Sequencial', grass, [dmg50], 0, None)

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
        player = Pc("Superman", normal, 1000, 100, 100, 150, underSun, pxy, [heatVision, frostBreath, sunCharge, megaPunch])
        
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
    call turn_start