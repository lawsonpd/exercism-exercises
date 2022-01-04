import random
import string

class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        random.seed()
        self.name = ''.join(random.choices(string.ascii_letters[26:], k=2) + random.choices(string.digits, k=3))