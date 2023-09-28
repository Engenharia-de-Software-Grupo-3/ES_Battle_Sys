init python:
    class Sprite_info(object):
        def __init__(self, name, x_position, y_position, atk_sprite = None, dmg_sprite = None) :
            self.name = name
            self.x_position = x_position
            self.y_position = y_position
            self.atk_sprite = atk_sprite
            self.dmg_sprite = dmg_sprite

    