import copy
import random
# Consider using the modules imported above.

class Hat(object):
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)
        #random.shuffle(self.contents)

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
    desired_outcomes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        draw_dict = dict()
        
        for ball in draw:
            draw_dict[ball] = draw_dict.get(ball, 0) + 1
        
        match = True
        for key, value in expected_balls.items():
            # key = ball and value = number
            if key not in draw_dict or draw_dict[key] < value:
                match = False
                break
        if match:
            desired_outcomes += 1

    return desired_outcomes / num_experiments