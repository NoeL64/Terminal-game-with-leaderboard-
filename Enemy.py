import random
from utils import *
#the enemy
class Enemy:
  
  def __init__(self):
    
   
    difficulties = ["Easy", "Medium", "Hard", "Bulky", "Quick"]
    self.difficulty = difficulties[random.randint(0, 4)]
    if(self.difficulty == "Easy"):
      self.runChance = random.randint(1, 10)
      self.Health = random.randint(1, 5)
      self.Attack = random.randint(1, 2)
      self.Money = random.randint(1, 5)
    elif(self.difficulty == "Medium"):
      self.runChance = random.randint(1, 15)
      self.Health = random.randint(4, 10)
      self.Attack = random.randint(2, 4)
      self.Money = random.randint(3, 10)
    elif(self.difficulty == "Bulky"):
      self.runChance = random.randint(1, 40)
      self.Health = random.randint(4, 25)
      self.Attack = random.randint(1, 2)
      self.Money = random.randint(7, 7)
    elif(self.difficulty == "Quick"):
      self.runChance = random.randint(1, 2)
      self.Health = random.randint(1, 5)
      self.Attack = random.randint(1, 1)
      self.Money = random.randint(1, 12)
    else:
      self.runChance = random.randint(1, 25)
      self.Health = random.randint(6, 15)
      self.Attack = random.randint(3, 5)
      self.Money = random.randint(5, 13)
  def attack(self):
    messages = ["Slash!", "Oof!", "Bang!", "Thats got to hurt!", "Youchers!", "Youll need a bandaid for that one!"]
    print(Red + "The monster attacked!")
    print(Red + messages[random.randint(0, 5)], "You took", self.Attack, "damage.")
    return self.Attack
  def run(self):
    chanceToRun = random.randint(1, 3)
    if(chanceToRun == 3):
      runMessages = ["The enemy scrambeled away!", "The enemy dashed away as fast as he could", "The enemy ran for his life!", "Your lucky! The enemy quickly ran away."]
      print(runMessages[random.randint(0, 3)])
      return True
    else:
      print("The enemy couldn't run! ")
      return False
