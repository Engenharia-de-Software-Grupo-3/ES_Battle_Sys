init python:

    class Battle_fase(object):
        def __init__(self) :
            #Inicias
            self.fst_attacker = None
            self.fst_skill = None
            self.snd_attacker = None
            self.snd_skill = None

            #Field
            self.current_fase = "Battle_start"
            self.state = None

            #Abilities_change
            self.player_attack_blocked = False
            self.enemy_attack_blocked = False

            #Battle_info
            self.player_damage = 0
            self.player_cure = 0

            self.enemy_damage = 0
            self.enemy_cure = 0

        def attack_order(self, p_speed, p_skill, e_speed, e_skill):
            if p_skill.speed != e_skill.speed:
                if p_skill.speed > e_skill.speed:
                    self.attack_order_aux('player', p_skill, 'enemy', e_skill)
                else:
                    self.attack_order_aux('enemy', e_skill, 'player', p_skill)
            else:
                if p_speed >= e_speed:
                    self.attack_order_aux('player', p_skill, 'enemy', e_skill)
                else:
                    self.attack_order_aux('enemy', e_skill, 'player', p_skill)

        def attack_order_aux(self, fst_attacker, fst_skill, snd_attacker, snd_skill):
            self.fst_attacker = fst_attacker
            self.fst_skill = fst_skill
            self.snd_attacker = snd_attacker
            self.snd_skill = snd_skill


