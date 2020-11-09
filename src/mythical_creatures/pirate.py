class Pirate:
    def __init__(self, name, job = 'scallywag'):
        self.name = name
        self.job = job
        self.booty = 0
        self.heinous_acts = 0

    def robs_ship(self):
        self.booty += 100

    def is_cursed(self):
        return True if self.heinous_acts >= 3 else False

    def commit_heinous_act(self):
        self.heinous_acts += 1