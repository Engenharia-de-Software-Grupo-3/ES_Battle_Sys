init python:
    class Status_condition(object):
        """
                Args:
                    Name
                    Activation_time {
                        1. Turn start
                        2. Before hit
                        3. After hit
                        4. Turn End
                        5. Turn Start
                        6. Battle Start
                        7. Item usage
                        8. Enemy change
                        9. Always
                    }
                    Effect

        """
        def __init__(self, name, activation_time, effect, duration = 3) :
            self.name = name
            self.activation_time = activation_time
            self.effect = effect
            self.duration = duration