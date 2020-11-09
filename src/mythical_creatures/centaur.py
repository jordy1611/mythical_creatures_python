class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.action = 0
        self.standing = True
        self.sick = False

    def shoot(self):
        if not self.is_cranky() and self.standing == True:
            self.action += 1
            return 'Twang!!!'
        else:
            return 'NO!'

    def run(self):
        if not self.is_cranky() and self.standing == True:
            self.action += 1
            return "Clop clop clop clop!!!"
        else:
            return 'NO!'

    def is_cranky(self):
        return True if self.action >= 3 else False

    def is_standing(self):
        return self.standing

    def sleep(self):
        if self.standing:
            return 'NO!'
        else:
            self.action = 0
            return 'OK!'

    def lay_down(self):
        self.standing = False

    def is_laying(self):
        return not self.standing

    def stand_up(self):
        self.standing = True

    def is_rested(self):
        return True if self.action < 3 else False

    def drink_potion(self):
        if self.is_rested() == True:
            self.sick = True
        elif self.standing == True:
            self.action = 0

    def is_sick(self):
        return self.sick
