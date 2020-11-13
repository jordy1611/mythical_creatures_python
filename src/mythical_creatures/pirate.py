class Pirate:
    def __init__(self, name, job = 'scallywag'):
        self.name = name
        self.job = job
        self.cursed = False
        self.heinous_acts = 0
        self.booty = 0
    
    def is_cursed(self):
        return self.cursed

    def commit_heinous_act(self):
        self.heinous_acts += 1
        self.cursed = self.heinous_acts == 3
        # (self.cursed = False, self.cursed = True)[self.heinous_acts == 3]

    def robs_ship(self):
        self.booty += 100