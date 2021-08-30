# a game of rock, paper, scissors with a CPU
from random import randint

# making a table of choices 
t = ["Rock", "Paper", "Scissors"]

#assign a random play
computer = t[randint(0,2)] 

#set player to False at first
player = False

while player == False:
  # set player to true because they're making a choice 
  player = input("Rock, Paper, or Scissors? ")

  # 3 possible outcomes, tie, win, lose
  if player == computer:
    print("Tie!")

  elif player == "Rock":
    if computer == "Paper":
      print("You lose!", computer, "covers", player)
    else:
      print("You win!", player, "smashes", computer )
  
  elif player == "Paper":
    if computer == "Scissors":
      print("You lose!", computer, "cuts", player)
    else:
      print("You win!", player, "covers", computer)
    
  elif player == "Scissors":
    if computer == "Rock":
      print("You lose!", computer, "smashes", player)
    else:
      print("You win!", player, "cuts", computer)

  #if the input is invalid, change the value of the player to keep the loop again
  else:
    print("That's not a valid play. Check your spelling!")
  player = False
  computer = t[randint(0,2)]