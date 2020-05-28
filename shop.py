from utils import *
def shop(money, damage, health):
  
  clear()
  while True: 
    print(Green + "Welcome to the shop!")
    Shop = int(input("What would you like to buy? \n 1: Damage \n 2: Health \n 3: Return to menu\n"))
    if(Shop == 3):
      return damage, money, health
    elif(Shop == 1):
      clear()
      print("Ahh, I see. Here is our fine damage upgrades.")
      weapon = int(input("1: Noob Stick, 10 moneyz, Damage + 1 \n 2: Ehhhh stick, 20 moneyz, Damage + 2 \n 3: Good stick, 40 moneyz, Damage + 3 \n 4: God stick, Damage + 4, 50 moneyz\n"))
      if(weapon == 1):
        if(money >= 10):
          clear()
          print(Green + "You bought the noob stick. - 10 moneyz.")
          damage = 3
          money = money - 10
        
        else:
          print(Red + "Dont try and cheat the shop!")
      if(weapon == 2):
        if(money >= 20):
          clear()
          print(Green + "You bought the Ehhhhh stick. - 20 moneyz.")
          damage = 4
          money = money - 20
        
        else:
          print(Red + "Dont try and cheat the shop!")
      if(weapon == 3):
        if(money >= 40):
          clear()
          print(Green + "You bought the good stick. - 40 moneyz.")
          damage = 4
          money = money - 40
        
        else:
          print(Red + "Dont try and cheat the shop!")
      if(weapon == 4):
        if(money >= 50):
          clear()
          print(Green + "You bought the God stick. - 50 moneyz.")
          damage = 5
          money = money - 50
        
        else:
          print(Red + "Dont try and cheat the shop!")
      else:
        print("Thats not an option, silly!")
    elif(Shop == 2):
      clear()
      print("Ahh, I see. Here is our fine health upgrades.")
      helth = int(input("1: Band-Aid, 10 moneyz, 13 Health \n 2: Potion, 20 moneyz, 16 Health \n 3: Super Heal, 40 moneyz, 20 Health \n"))
      if(helth == 1):
        if(money >= 10):
          clear()
          print("You bought the Band-Aid. -10 moneyz.")
          money = money - 10
          health = 13
        else:
          clear()
          print("Dont try to cheat the shop!")
      elif(helth == 2):
        if(money >= 20):
          clear()
          print("You bought the Potion. -20 moneyz.")
          money = money - 20
          health = 16
          
        else:
          clear()
          print("Dont try to cheat the shop!")
      elif(helth == 3):
        if(money >= 40):
          clear()
          print("You bought the Super Heal. -40 moneyz.")
          money = money - 40
          health = 20
          
        else:
          clear()
          print("Dont try to cheat the shop!")
      else:
        print("Thats not even an option!")
    else:
      print("Thats not an option....")