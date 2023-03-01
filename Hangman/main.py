import random
import ascii_img_hangman
import words

print(ascii_img_hangman.logo[0])

lives = 6
theme = input("Select a topic: weather, family or animals.\n")
word_list = words.word_dict[theme]
chosen_word = random.choice(word_list)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

blanks_list = []
for i in range(len(chosen_word)):
  i = "_"
  blanks_list.append(i)
print(blanks_list)

game_over = False
while not game_over:
  guess = input("Guess a letter: ").lower()

  if guess in blanks_list:
    print("You have already guessed this letter. Try again.")
    
  ind = 0
  for element in chosen_word:
    if element == guess:
        blanks_list[ind] = element
    ind += 1
  print(blanks_list)
  if guess not in chosen_word:
    lives -= 1
    print(f"You have chosen {guess} this letter there is no in the word. You lost one life.")
    print(ascii_img_hangman.stages[lives])
    print(f"You have only {lives} lives left.")
    if lives == 0:
      game_over = True
      print("You lose! :(")

  if "".join(blanks_list) == chosen_word:
    game_over = True
    print("You win!")
