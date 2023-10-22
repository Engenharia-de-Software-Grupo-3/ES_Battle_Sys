from game.battle_phase import Battle_phase

def test_attack_order():
    bp = Battle_phase()
    bp.attack_order(10, "player_skill", 5, "enemy_skill")
    assert bp.fst_attacker == "player"
    assert bp.snd_attacker == "enemy"

    bp.attack_order(5, "player_skill", 10, "enemy_skill")
    assert bp.fst_attacker == "enemy"
    assert bp.snd_attacker == "player"

    bp.attack_order(5, "player_skill", 5, "enemy_skill")
    assert bp.fst_attacker == "player"
    assert bp.snd_attacker == "enemy"

def test_check_passive_time():
    bp = Battle_phase()
    bp.current_stage = "Battle_start"
    assert bp.check_passive_time("passive") == True

    bp.current_stage = "Turn_start"
    assert bp.check_passive_time("passive") == False

def test_check_statusCondition_time():
    bp = Battle_phase()
    bp.current_stage = "Battle_start"
    status_condition_dictionare = {"status1": "value1", "status2": "value2"}
    assert bp.check_statusCondition_time(status_condition_dictionare) == ["status1", "status2"]

    bp.current_stage = "Turn_start"
    assert bp.check_statusCondition_time(status_condition_dictionare) == []

def test_is_player_turn():
    bp = Battle_phase()
    bp.fst_attacker = "player"
    bp.snd_attacker = "enemy"
    bp.phase = 1
    assert bp.is_player_turn() == True

    bp.fst_attacker = "enemy"
    bp.snd_attacker = "player"
    bp.phase = 2
    assert bp.is_player_turn() == False

def test_is_enemy_turn():
    bp = Battle_phase()
    bp.fst_attacker = "player"
    bp.snd_attacker = "enemy"
    bp.phase = 1
    assert bp.is_enemy_turn() == False

    bp.fst_attacker = "enemy"
    bp.snd_attacker = "player"
    bp.phase = 2
    assert bp.is_enemy_turn() == True