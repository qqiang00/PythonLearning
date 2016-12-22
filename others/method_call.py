"""这个示例演示了 __call__ 函数如何发挥作用
"""
class Animal(object):
  def __init__(self, name, leg):
    self.name = name
    self.leg = leg
    self.stomach = []
    
  def __call__(self, food):
    self.stomach.append(food)
    
  def poop(self):
    if len(self.stomach) > 0:
      return self.stomach.pop(0)
    
  def __str__(self):
    return "A animal named {}".format(self.name)
  

if __name__ == "__main__":
  cow = Animal("king",4)
  dog = Animal("flopp",4)
  
  print("We have 2 animals, a cow named {} and a dog named {}.Both have {} legs.".
        format(cow.name,dog.name,cow.leg))
  print(cow)  # here __str__ method works.
  cow("grass")  # give food to cow
  print(cow.stomach)
  
  dog("bone")
  dog("beef")
  print(dog.stomach)
  
  print(cow.poop())
  print(cow.stomach)
  
  
  