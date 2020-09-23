import copy
import random
# Consider using the modules imported above.

class Hat(object):
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)
        random.shuffle(self.contents)

    def draw(self, number):
        drawn = []
        if number >= len(self.contents):
            drawn = copy.deepcopy(self.contents)
            random.shuffle(drawn)
            self.contents = []
        else:
            while len(drawn) < number:
                r = random.randint(0, len(self.contents) - 1)
                drawn.append(self.contents[r])
                del self.contents[r]
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass