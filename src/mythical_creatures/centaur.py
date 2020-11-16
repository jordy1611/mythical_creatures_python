class Centaur():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.cranky_counter = 0
        self.cranky = self.cranky_counter >= 2
        self.standing = True
        self.sick = False

    def shoot(self):
        self.cranky_counter += 1
        self.cranky = self.cranky_counter > 2
        return ('NO!', 'Twang!!!')[not self.cranky and self.standing]

    def run(self):
        self.cranky_counter += 1
        self.cranky = self.cranky_counter > 2
        return ('NO!', 'Clop clop clop clop!!!')[not self.cranky and self.standing]

    def is_cranky(self):
        return self.cranky

    def is_standing(self):
        return self.standing

    def is_laying(self):
        return not self.standing

    def sleep(self):
        if self.standing:
            return 'NO!'
        else:
            self.cranky_counter = 0
            self.cranky = False
            return 'OK!'

    def lay_down(self):
        self.standing = False

    def stand_up(self):
        self.standing = True

    def drink_potion(self):
        if self.cranky and self.standing:
            self.cranky_counter = 0
            self.cranky = False
        elif not self.cranky:
            self.sick = True

    def is_rested(self):
        return not self.cranky
    
    def is_sick(self):
        return self.sick