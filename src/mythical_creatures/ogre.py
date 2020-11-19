class Ogre:
    def __init__(self, name, home = 'swamp'):
        self.name = name
        self.home = home
        self.encounter_counter = 0

    def encounter(self, human):
        self.encounter_counter += 1

    def swing(self, human):
        if self.encounter_counter >= 3:
            human.knocked_out = True
            return True
        else:
            return False

    def apologize(self, human):
        human.knocked_out = False

class Human:
    def __init__(self, name):
        self.name = name
        self.knocked_out = False