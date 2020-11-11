class Unicorn:
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def is_white(self):
        # return self.color == 'white'
        is_it_white = (False, True)[self.color == 'white']
        return is_it_white
        # if self.color == 'white':
        #     return True
        # else:
        #     return False

    def say(self, text):
        return f"**;* {text} *;**"