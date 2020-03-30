ALLERGENS = 'eggs peanuts shellfish strawberries tomatoes chocolate pollen cats'.split()


class Allergies:
    def __init__(self, score):
        self.allergies = [ALLERGENS[i] for i in range(8) if (score >> i) & 1 != 0]

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
