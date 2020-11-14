class Centaur():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.cranky_counter = 0
        self.cranky = self.cranky_counter >= 2
        self.standing = True

    def shoot(self):
        self.cranky_counter += 1
        self.cranky = self.cranky_counter >= 2
        print('count', self.cranky_counter, 'cranky', self.cranky)
        return ('Twang!!!', 'NO!')[self.cranky]
        # return 'Twang!!'

    def run(self):
        self.cranky_counter += 1
        self.cranky = self.cranky_counter >= 2
        return ('Clop clop clop clop!!!', 'NO!')[self.cranky]
        # return 'Clop clop clop clop!!!'

    def is_cranky(self):
        return self.cranky

    def is_standing(self):
        return self.standing

    def is_laying(self):
        return not self.standing

    def sleep(self):
        print('standing', self.standing)
        if self.standing:
            return 'NO!'
        else:
            return 'OK!'

    def lay_down(self):
        self.standing = False