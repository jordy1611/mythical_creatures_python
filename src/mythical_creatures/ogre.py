class Ogre:
    def __init__(self, name, home='swamp'):
        self.name = name
        self.home = home
        self.encounter_counter = 0

    def encounter(self, human):
        self.encounter_counter += 1
        human.encounter()

    def swing(self, human):
        human.knocks_out()
        return True if self.encounter_counter >= 3 else False

    def apologize(self, human):
        human.wakes_up()


class Human:
    def __init__(self, name):
        self.name = name
        self.encounter_counter = 0
        self.knocked_out = False

    def encounter(self):
        self.encounter_counter += 1

    def knocks_out(self):
        self.knocked_out = True

    def wakes_up(self):
        self.knocked_out = False
