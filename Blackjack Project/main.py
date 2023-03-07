import random
import art


print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"""
Blackjack Project: 
Our Blackjack House Rules 
The deck is unlimited in size. 
There are no jokers. 
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""


def comparison(your_cards, dealer_cards):
  print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's cards: {dealer_cards}, current score: {sum(dealer_cards)}")
  if 21 - sum(your_cards) < abs(21 - (sum(dealer_cards))):
    print("You win!")
  elif sum(your_cards) == sum(dealer_cards):
    print("draw")
  else:
    print("You lose!")


def check_A(cards):
  for x in cards:
      if x == 11 and sum(cards) > 21:
        cards = list(map(lambda x: x if x != 11 else 1, cards))
  return cards


def dealer__cards(dealer_cards):
  dealer_cards += [random.choice(cards)]
  check_A(dealer_cards)
  while sum(dealer_cards) < 17:
    dealer_cards += [random.choice(cards)]
  return dealer_cards


game = True
while game:
  if (input("Do you want to start a game? 'Y' or 'N':\n")).lower()== "y":
    print(art.good_luck)
    print(art.cards)
    your_cards, dealer_cards = random.sample(cards,2), [random.choice(cards)]
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card: {dealer_cards}")
    
    continue_ = True
    while continue_:
      if (input("Type 'Y' to get another card, type 'N' to pass:\n")).lower() == "y":
        your_cards += [random.choice(cards)]
        check_A(your_cards)
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card: {dealer_cards}") 
        if sum(your_cards) > 21:
          continue_ = False
          print("You lose!")
      else:
        continue_ = False
        dealer__cards(dealer_cards)
        comparison(your_cards, dealer_cards)
  else:
    game = False
    print("Goob bye!")
