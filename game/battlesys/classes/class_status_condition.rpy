init python:
    class Status_condition(object):
        """
                Args:
                    Name
                    Activation_time {
                        1. Battle_Start | Turn_start | Effect_calculate | Effect_hit | Battle_End 
                        2. Item usage
                        3. Enemy change
                        4. Always
                    }
                    Effect {
                        A function F(afflicted, battleState, battlePhase)
                        afflicted -> 'player' | 'enemy'
                    }

        """
        def __init__(self, name, activation_time, effect, duration = 3) :
            self.name = name
            self.activation_time = activation_time
            self.effect = effect
            self.duration = duration