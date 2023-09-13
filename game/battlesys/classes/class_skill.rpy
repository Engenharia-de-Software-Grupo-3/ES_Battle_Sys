init python:

    class Skill(object):
        """
             Name
             Effect_sequence {
                - Inverted
                - Individual
                - Sequencial
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
            self.speed = speed
            self.pic_sprite = pic_sprite