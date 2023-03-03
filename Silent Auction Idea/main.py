import os
from art import logo

print(logo)

restart = True
auction = {}
while restart:
  print("Do you want to win Lotto Ticket Basket?\nWelcome to the secret auction programm, where you will have such an opportunity.")
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  auction[name] = bid
  new_bidders = (input("Are there are any other bidders? Y or N:\n")).lower()
  if new_bidders == "n":
    restart = False
  # Clearing the Screen Linux, for Win('clr')
  os.system('clear')
winner = max(auction, key= lambda x: auction[x])
print(f"The winner is {winner} with bid ${auction[winner]}")


