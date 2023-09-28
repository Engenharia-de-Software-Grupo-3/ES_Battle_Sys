init python:
    class Passive(object):
        """
                Args:
                    • Name
                    • activation_time {
                         1. Battle_Start | Turn_start | Effect_calculate | Effect_hit | Battle_End 
                         2. Item usage
                         3. Enemy change
                         4. Always
                    }
                    • Trigger
                    • Effect

        """
        def __init__(self, name, activation_time, effect) :
            self.name = name
            self.activation_time = activation_time
            self.effect = effect