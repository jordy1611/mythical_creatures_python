class Unicorn:
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def is_white(self):
        return self.color == 'white'

        # return (False, True)[self.color == 'white']

        # if self.color == 'white':
        #     return True
        # else:
        #     return False

    def say(self, text):
        return f"**;* {text} *;**"
        # return '**;* ' + str(text) + ' *;**'