class Direwolf:

    def __init__(self, name, home = 'Beyond the Wall', size = 'Massive'):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = []
        self.hunts_white_walkers = True

    def protects(self, stark):
        if stark.location == self.home:
            stark.protected()
            self.starks_to_protect.append(stark)

    def leaves(self, stark):
        if self.starks_to_protect
            self.starks_to_protect.remove(stark)


class Stark:
    def __init__(self, name, location = 'Winterfell'):
        self.name = name
        self.location = location
        self.safe = False
        self.house_words = 'Winter is Coming'

    def is_safe(self):
        return self.safe

    def protected(self):
        self.safe = True
