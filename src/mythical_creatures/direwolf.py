class Direwolf:
    def __init__(self, name, home = 'Beyond the Wall', size = 'Massive'):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = []

    def protects(self, person):
        if self.home == person.location:
            self.starks_to_protect.append(person)


class Stark:
    def __init__(self, name, location = 'Winterfell', home = 'Winterfell'):
        self.name = name
        self.location = location
        self.home = home