import json
import random

f = open("data.json")

data = json.load(f)
city_dict = {}
for i in data:
    city_dict[i['pop2023']] = [i['country'], i['city']]  
f.close()

def comparison(a, b, score):
    max_population = max(a, b)
    if (max_population == a and choise == "a") or (max_population == b and choise == "b"):
        print("It's true.\n")
        score += 1
    else:
        print("Sorry, it's wrong.\n")
    return score

score = 0
game = True
while game:
    information = random.choice(list(city_dict.items()))
    a, country, citya = information[0], information[1][0], information[1][1]
    print(f"Compare cities\nA: {citya} in {country}\n")
    information = random.choice(list(city_dict.items()))
    b, country, cityb = information[0], information[1][0], information[1][1]
    print(f"Against city\nB: {cityb} in {country}.\n")
    choise = (input("Which city has more population in 2023? Type 'A' or 'B'\n")).lower()
    score = comparison(a, b, score)
    score
    print(f"The population of the city of {citya} in 2023 is {a}, and the city of {cityb} is {b}.\nYour score is {score}.\n")
    continuation = (input("Do you want to continue the game? 'Y' or 'N'\n")).lower()
    if continuation == 'n':
        game = False
        print(f"Your final score is {score}.\nBye-bye!")
    
    

      

