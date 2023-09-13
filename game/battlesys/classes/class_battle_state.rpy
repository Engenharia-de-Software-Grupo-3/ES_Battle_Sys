init python:

    class Enemy_current_stats(object):
        def __init__(self, enemy) :
            self.enemy_name = enemy.name
            self.enemy_type = enemy.type
            self.enemy_hp = enemy.hp
            self.enemy_atk = enemy.atk
            self.enemy_res = enemy.res
            self.enemy_luck = enemy.luck
            self.enemy_skill_set = enemy.skill_set
            self.enemy_sprite_info = enemy.sprite_info
            self.enemy_attack_pattern = enemy.attack_pattern

            self.alive = True
            self.accurace_boost = 0
            self.type_boost_list = []
            self.type_resistance_list = []
            self.status_condition_dictionare = {}


    def create_current_stats(enemy_team):
        saida = []
        for e in enemy_team.enemy_list:
            if e is None:
                saida.append(None)
            else:
                saida.append(Enemy_current_stats(e))
        return saida


    # Battle State Class
    class Battle_state(object):
        
        def __init__(self, player, enemy_team) :
            # Field
            self.turn = 0

            # Player current stats
            self.original_player = player
            self.player_name = player.name
            self.player_type = player.type
            self.player_hp = player.hp
            self.player_atk = player.atk
            self.player_res = player.res
            self.player_luck = player.luck
            self.player_passive = player.passive
            self.player_skill_set = player.skill_set
            self.player_sprite_info = player.sprite_info

            self.accurace_boost = 0
            self.type_boost_list = []
            self.type_resistance_list = []
            self.status_condition_dictionare = {}

            # Enemy team current stats
            self.original_enemy_team = enemy_team
            self.enemy_team_current_stats = create_current_stats(enemy_team)

        def swap_enemy_head(self, i):
            aux = self.enemy_team_current_stats[0]
            self.enemy_team_current_stats[0] = self.enemy_team_current_stats[i]
            self.enemy_team_current_stats[i] = aux