import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    
    for arg in kwargs:
      i = 0
      while i < kwargs[arg]:
        self.contents.append(arg)
        i = i + 1

  
  def draw(self, num):
    
    i = 0
    balls = []

    if num > len(self.contents):
        return self.contents

    while i < num:
      length = len(self.contents)
      ran_num = random.randint(0, length - 1)
      balls.append(self.contents[ran_num])
      self.contents.remove(self.contents[ran_num])
      i = i + 1

    return balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  j = 0
  m = 0

  hat_copy = copy.deepcopy(hat.contents)
  
  while j < num_experiments:
    result = []
    result = hat.draw(num_balls_drawn)
    hat.contents = copy.deepcopy(hat_copy)

    colors = {}
    for res in result:
      if res not in colors:
        colors[res] = 0
      if res in colors:
        x = colors[res]
        x = x + 1
        colors[res] = x

    y = 0
 
    for color in colors:
      for ball in expected_balls:
        if color == ball and colors[color] >= expected_balls[ball]:
            y = y + 1

    if y >= len(expected_balls):
        m = m + 1 


    j = j + 1
  
  probability = m / num_experiments

  return probability

