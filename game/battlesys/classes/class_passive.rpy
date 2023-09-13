init python:
    class Passive(object):
        """
                Args:
                    • Name
                    • activation_time {
                         1. Turn start
                         2. Battle start
                         2. Before hit
                         3. After hit
                         4. Turn End
                         5. Turn Start
                         6. Battle Start
                         7. Item usage
                         8. Enemy change
                         9. Always
                    }
                    • Trigger
                    • Effect

        """
        def __init__(self, name, activation_time, trigger, effect) :
            self.name = name
            self.activation_time = activation_time
            self.trigger = trigger
            self.effect = effect

        def trigger_on(self, battle_state):
            return self.trigger(battle_state)