#Importing other files
from Enemy import *
from utils import *
import time
import random
from shop import *
import DB
#This is the battle function!
def Battle(health, damage):
  clear()
  #Declares enemy
  enemy = Enemy()
  print(Red + "This is a battle between you and a", enemy.difficulty, "enemy. ")
  time.sleep(2)
  print(Green + "Battle...")
  time.sleep(1)
  print(Blue + "BEGIN!")
  time.sleep(1)
  #haha while true go brrrrrr
  while True:
    #win statement, returns money
    if(enemy.Health <= 0):
      print(Green + "YOU WINN!")
      return random.randint(enemy.Money - 2, enemy.Money + 2)
    #on loose yiu have a chance to loose money
    elif(health <= 0):
      chanceToLoose = random.randint(1, 5)
      if(chanceToLoose == 1):
        print(Red + "You scrambled away but lost dome cash. You lost the battle. - 2 cash.")
        return -2
      else:
        print(Red + "You looose....")
        return 0
    #Prints out status
    print(Green + "You have", health, "health")
    print(Green + "The monster has", enemy.Health, "health.")
    print(Blue)
    #Makes sure the user inputs something valid
    while True:
      try: 
        
        action = int(input(" 1: Attack\n 2: Run Away \n"))
        clear()
        break
      except:
        #Imagine not inputting a number
        clear()
        print("Please choose a number.")
    if(action == 1):
      lost = enemy.attack()
      health = health - lost
      print(Green)
      #attack messages are awesome
      attackMessages = ["Hah!", "That should teach him!", "You hit!"]
      print(attackMessages[random.randint(0, 2)], "You did", damage, "damage.")
      enemy.Health -= damage
      #enemy.runChnace in in enemy.py
      if(random.randint(0, enemy.runChance) == 1):
        print(Yellow, "The enemy is attemping to run!")
        if(enemy.run() == True):
          return 0
          #i can understand why youd want to run away 
    elif(action == 2):
      print(Yellow + "You are attempting to run away")
      chanceToRun = random.randint(1, 5)
      if(chanceToRun == 1):
        print("Ran away succesfully")
        return 0
      elif(chanceToRun == 2):
        print("You stole dome cash from the monster while running away! + 2 money")
        return 2
      else:
        print("Couldnt run!")
        damageNow = random.randint(enemy.damage - 1, enemy.damage + 2)
        print("The enemy took his chance and hit you! He dealt", damageNow)
        health = health - damageNow
print(Blue + "Welcome! ")
#variables!
money = 0
damage = 2
health = 10
score = 0
# haha more while trues go brrrrrr
while True: 
  print(Blue)
  print("You have", money, "money")
  score = damage + health
  actions = int(input("Actions: \n 0: Veiw score \n 1: Attack an enemy \n 2: Leaderboard \n 3: Save data to leaderboard \n 4: Shop \n"))
  if(actions == 1):
    money += Battle(health, damage)
  elif actions == 0:
    clear()
    print(Yellow + "Calculating score..")
    print_slow("You have: ")
    time.sleep(0.5)
    print_slow(str(score))
    time.sleep(0.5)
    print_slow(" Score.")
  elif actions == 2:
    DB.Check(False)
  elif(actions == 3):
    DB.Save(score)
  elif(actions == 4):
    damage, money, health = shop(money, damage, health)
  elif(actions == 5):
    #PLEASE DONT ENTER FIVE BECAUSE I DONT WANT PEOPLE IN THE ADMIN PANNEL!
    print_slow(Green + "Gaining admin.......")
    print(Red)
    print_slow(Red + "Admin gained.")
    print(Green + " \n Go to https://www.youtube.com/watch?v=dQw4w9WgXcQ for the admin panel.")
   