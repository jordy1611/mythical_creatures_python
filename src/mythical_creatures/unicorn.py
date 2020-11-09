class Unicorn:
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def say(self, message):
        return f"**;* {message} **;*"
        # return "**;* " + message + " **;*"

    def is_white(self):
        if self.color == 'white':
            return True
        else:
            return False