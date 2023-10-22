from class_battle_state import Battle_state, Enemy_current_stats

def test_create_current_stats():
    class Enemy(object):
        def __init__(self, name, type, hp, atk, res, luck, skill_set, sprite_info, attack_pattern):
            self.name = name
            self.type = type
            self.hp = hp
            self.atk = atk
            self.res = res
            self.luck = luck
            self.skill_set = skill_set
            self.sprite_info = sprite_info
            self.attack_pattern = attack_pattern

    class Enemy_team(object):
        def __init__(self, name, enemy_list, passive):
            self.name = name
            self.enemy_list = enemy_list
            self.passive = passive

    enemy1 = Enemy("Enemy1", "type1", 100, 10, 5, 5, [], [], [])
    enemy2 = Enemy("Enemy2", "type2", 200, 20, 10, 10, [], [], [])
    enemy3 = Enemy("Enemy3", "type3", 300, 30, 15, 15, [], [], [])
    enemy_team = Enemy_team("Enemy Team", [enemy1, enemy2, enemy3], [])

    bs = Battle_state(None, enemy_team)
    current_stats = bs.create_current_stats(enemy_team)

    assert len(current_stats) == 3
    assert current_stats[0].enemy_name == "Enemy1"
    assert current_stats[1].enemy_type == "type2"
    assert current_stats[2].enemy_hp == 300

def test_swap_enemy_head():
    class Enemy(object):
        def __init__(self, name, type, hp, atk, res, luck, skill_set, sprite_info, attack_pattern):
            self.name = name
            self.type = type
            self.hp = hp
            self.atk = atk
            self.res = res
            self.luck = luck
            self.skill_set = skill_set
            self.sprite_info = sprite_info
            self.attack_pattern = attack_pattern

    class Enemy_team(object):
        def __init__(self, name, enemy_list, passive):
            self.name = name
            self.enemy_list = enemy_list
            self.passive = passive

    enemy1 = Enemy("Enemy1", "type1", 100, 10, 5, 5, [], [], [])
    enemy2 = Enemy("Enemy2", "type2", 200, 20, 10, 10, [], [], [])
    enemy3 = Enemy("Enemy3", "type3", 300, 30, 15, 15, [], [], [])
    enemy_team = Enemy_team("Enemy Team", [enemy1, enemy2, enemy3], [])

    bs = Battle_state(None, enemy_team)
    current_stats = bs.create_current_stats(enemy_team)

    bs.swap_enemy_head(2)

    assert current_stats[0].enemy_name == "Enemy3"
    assert current_stats[2].enemy_name == "Enemy1"

def test_get_player_typeBoost():
    bs = Battle_state(None, None)
    bs.type_boost_dictionare = {"type1": 2, "type2": 3}

    assert bs.get_player_typeBoost("type1") == 2
    assert bs.get_player_typeBoost("type2") == 3
    assert bs.get_player_typeBoost("type3") == 0

def test_get_enemyHead_typeBoost():
    class Enemy(object):
        def __init__(self, name, type, hp, atk, res, luck, skill_set, sprite_info, attack_pattern):
            self.name = name
            self.type = type
            self.hp = hp
            self.atk = atk
            self.res = res
            self.luck = luck
            self.skill_set = skill_set
            self.sprite_info = sprite_info
            self.attack_pattern = attack_pattern

    enemy = Enemy("Enemy", "type1", 100, 10, 5, 5, [], [], [])
    ecs = Enemy_current_stats(enemy)
    ecs.type_boost_dictionare = {"type1": 2, "type2": 3}

    bs = Battle_state(None, None)
    bs.enemy_team_current_stats = [ecs]

    assert bs.get_enemyHead_typeBoost("type1") == 2
    assert bs.get_enemyHead_typeBoost("type2") == 3
    assert bs.get_enemyHead_typeBoost("type3") == 0

def test_status_condition_downgrade():
    bs = Battle_state(None, None)
    bs.player_status_condition_dictionare = {"status1": 2, "status2": 3}

    bs.status_condition_downgrade("Player")

    assert bs.player_status_condition_dictionare == {"status1": 1, "status2": 2}

    bs.status_condition_downgrade("Player")

    assert bs.player_status_condition_dictionare == {"status1": 0, "status2": 1}

    bs.status_condition_downgrade("Player")

    assert bs.player_status_condition_dictionare == {"status2": 0}