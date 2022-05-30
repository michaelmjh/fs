class FitnessClass:

    def __init__(self, name, time, capacity, active = True, class_id = None):
        self.name = name
        self.time = time
        self.capacity = capacity
        self.active = active
        self.class_id = class_id