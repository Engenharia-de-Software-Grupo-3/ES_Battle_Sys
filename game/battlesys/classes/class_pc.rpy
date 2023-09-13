init python:
    class Pc(object):
        """
                Args:
                      • Name
                      • Class (Analitica, Matematica, Teorica, Neutro)
                        ----------------------
                      • HP (vida)
                      • Expressivity  (ataque)
                      • Typed (defesa)
                      • Level (velocidade + critico)
                        ----------------------
                      • Passive
                      • Skills (1-4)
                        ----------------------
                      • Sprite
                      • Posicion                           
        """
        def __init__(self, name, type, hp, atk, res, luck, passive, sprite_info, skill_set = [None, None, None, None]) :
            self.name = name
            self.type = type
            self.hp = hp
            self.atk = atk
            self.res = res
            self.luck = luck
            self.passive = passive
            self.skill_set = skill_set
            self.sprite_info = sprite_info