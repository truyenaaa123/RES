import copy

class Champion():
    def __init__(self, name: str, traits: dict, cost: int):
        self.name = name
        self.traits = traits
        self.cost = cost
        self.star = 1

    def copy(self):
        return copy.deepcopy(self)
