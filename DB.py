import pymongo, dns
from utils import *
from time import sleep
#cool database stuff thanks to @cooljames
def Save(money):
  clear()
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] + text[21]
  current, name = Check(True)
  client = pymongo.MongoClient("mongodb+srv://myUser:" + word + "@cluster0-vj30z.mongodb.net/test?retryWrites=true&w=majority")
  db = client.test

  data = db.test
  if(money > int(current)):
    print(Green + "Congrats! Youve made it on the leaderboard... Saving... Please wait...")
    sleep(1)
    try:
      result = db.test.replace_one({ "Score": str(current), "Name": name }, { "Score": str(money), "Name":input("Name?") }, upsert=True)
    except:
      print("Seems like somebody broke the leaderboard.")
      print("Show this error in the comments.")
      raise
  else:
    print("Not enough score to get on the leaderboard!")
    
def Check(param): 
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] + text[21]
  client = pymongo.MongoClient("mongodb+srv://myUser:" + word + "@cluster0-vj30z.mongodb.net/test?retryWrites=true&w=majority")
  db = client.test

  data = db.test
  clear()
  print(Green + "Welcome to the database!")
  for x in data.find({}, { "_id": 0, "Score": 1, "Name": 2}):
      u = 0
  x = "'" + str(x) + "'"
  import re
  y = re.sub(r'[^\w\s]','',x)
  lst = [y]
  def convert(lst): 
      return ' '.join(lst).split()
  d = convert(lst)
  score = d[1]
  name = d[3]
  score = int(score)
  if(param == True):
    return score, name
  else:
    print(Yellow + "The current highest money is held by", name, "who has", str(score) + " Score!")
    
   