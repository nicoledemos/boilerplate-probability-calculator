import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for i in range(0,value):
                self.contents.append(key)

    def draw(self, balls):
        removed_balls = list()
        for i in range(0,balls):
            random_ball = random.randint(0,len(self.contents)-1)
            removed_balls.append(self.contents[random_ball])
            self.contents.pop(random_ball)
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_balls_drawn >= len(hat.contents):
        return 1.0

    num_times_expected = 0
    for i in range(1,num_experiments):
        hat_copy = copy.deepcopy(hat)
        exp_result = hat_copy.draw(num_balls_drawn)
        match_count = 0
        for colour in set(exp_result):
            if expected_balls.get(colour) is not None:
                if exp_result.count(colour) >= expected_balls.get(colour):
                    match_count = match_count + 1
        if match_count == len(expected_balls):
            num_times_expected = num_times_expected + 1
    return (float(num_times_expected) / float(num_experiments))
        
