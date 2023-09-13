init python:

    class Enemy_team(object):
        def __init__(self, name, passive, enemy_list, sprite) :
            self.name = name
            self.passive = passive
            self.enemy_list = enemy_list
            self.sprite = sprite

    class Enemy(object):
        def __init__(self, name, type, hp, atk, res, luck, skill_set, sprite_info, attack_pattern) :
            self.name = name
            self.type = type
            self.hp = hp
            self.atk = atk
            self.res = res
            self.luck = luck
            self.skill_set = skill_set
            self.sprite_info = sprite_info
            self.attack_pattern = attack_pattern

