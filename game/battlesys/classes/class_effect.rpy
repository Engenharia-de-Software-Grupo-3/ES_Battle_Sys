init python:
    import copy
    # target -> 0 (myself) | 1 (enemy)
    
    class Status_effect(object):
        def __init__(self, target, target_status, operator, value, accurace) :
            self.target = target
            self.target_status = target_status
            self.operator = operator
            self.value = value
            self.accurace = accurace
            self.class_name = 'Status_effect'

    # Type_boost
    class Type_effect(object):
        def __init__(self, target, target_type, operator, accurace) :
            self.target = target
            self.target_type = target_type
            self.operator = operator
            self.accurace = accurace
            self.class_name = 'Type_effect'

    class Status_condition_effect(object):
        def __init__(self, target, operator, status_condition, accurace) :
            self.target = target
            self.status_condition = status_condition
            self.operator = operator
            self.accurace = accurace
            self.class_name = 'Status_condition_effect'