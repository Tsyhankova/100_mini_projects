alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '?', ',', ':', ';', '@', '%', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > len(alphabet):
    shift = shift % len(alphabet)
    
  new_alphabet = alphabet[shift:] + alphabet[0:shift]
  #print(new_alphabet)
  
  def caesar(text, shift, direction):
    _text = ""
    for letter in text:
      if letter in alphabet:
        if direction == "encode":
          new_letter = new_alphabet[alphabet.index(letter)]
        else:
          new_letter = alphabet[new_alphabet.index(letter)]
      else:
       new_letter = letter 
      _text += new_letter
    print(f"The {direction}d text is {_text}")  
  caesar(text, shift, direction)
  restart_program = (input("Do you want to start again? Y/N ")).lower()
  if restart_program == "n":
    print("Have a good day!")
    restart = False
  
