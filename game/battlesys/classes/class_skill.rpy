init python:

    class Skill(object):
        """
             Name
             Effect_sequence {
                - Sequential -> Segundo efeito acontece se o primeiro acertar
                - Inverted -> Segundo efeito acontece se o primeiro errar
             }
             Type
             Speed [-1..2]
             Effect_list
             Class                         
        """
        def __init__(self, name, effect_sequence, type, effect_list, speed, pic_sprite) :
            self.name = name
            self.type = type
            self.effect_list = effect_list
            self.effect_sequence = effect_sequence
            self.speed = speed
            self.pic_sprite = pic_sprite