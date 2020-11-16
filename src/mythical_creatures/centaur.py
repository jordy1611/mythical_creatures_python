class Centaur():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.cranky_counter = 0
        self.cranky = self.cranky_counter >= 2
        self.standing = True

    def shoot(self):
        self.cranky_counter += 1
        print('cranky test before1', self.cranky_counter)
        self.cranky = self.cranky_counter > 2
        print('cranky test after1', self.cranky_counter)
        return ('NO!', 'Twang!!!')[not self.cranky and self.standing]

    def run(self):
        self.cranky_counter += 1
        print('cranky test before2', self.cranky_counter)
        self.cranky = self.cranky_counter > 2
        print('cranky test after2', self.cranky_counter)
        # print('run counter', self.cranky_counter, 'cranky', self.cranky, 'standing', self.standing)
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