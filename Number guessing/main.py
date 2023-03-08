import art
import random


print(art.logo)
name = (input("Welcome to Number Guessing Game. What is your name?\n")).capitalize()
restart = True

while restart:
  number = random.randint(1,100)
  attempt = {1:15, 2:10, 3:5}
  level = int(input(f"{name}, please choose the difficulty level of the game:\n1. Easy\n2. Medium\n3. Difficult\n"))
  attempts = attempt[level]
  print(f"You will have {attempts} attempts")
  winner = False
  while attempts != 0:
    guessed_number = int(input("Guess the number from 1 to 100\n"))
    if guessed_number == number:
      print(f"{name}, you guessed!")
      print(art.hurray)
      attempts = 0
      winner = True
    elif guessed_number > number:
      attempts -= 1
      print(f"Too higher. You have {attempts} attempts left")
    else:
      attempts -= 1
      print(f"Too lower. You have {attempts} attempts left")
  if not winner:
    print(f"You don't have any more attempts left. {name}, you couldn't guess. The number was: {number}.")
  restart = (input("Do you want to try again? 'Y' or 'N'\n")).lower()
  if restart == "n":
    restart = False
  
