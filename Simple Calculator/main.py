import art

#Simple Calculator
def add(n1, n2):
  return n1 + n2

def multiply(n1, n2):
  return n1 * n2

def substract(n1, n2):
  return n1 - n2

def devide(n1, n2):
  return n1 / n2

operations = {"+": add, 
             "-": substract, 
             "*": multiply, 
             "/": devide}

def calculator():
  print(art.logo)
  n1 = float(input("What is the first number?\n"))
  for oper in operations:
    print(oper)
  continue_calculating = True
  while continue_calculating:
    operation = input("Pick an operation:\n")
    n2 = float(input("What is the next number?\n"))
    if operation in operations:
      result = operations[operation](n1, n2)
      print((f"{n1} {operation} {n2} = {result}"))
    else:
      print("Invalid operation")
    continuation = input(f"To continue calculating with {result} type 'y', for restart calculating type 'n', to exit type 'exit':\n")
    if continuation == 'y':
      n1 = result
    elif continuation == 'n':
      continue_calculating = False
      calculator()
    else:
      continue_calculating = False
      print("Bye!")

calculator()
