# Importing necessary library
import random
random.seed(43)

# Generating a random 4-digit number
guess_string = ""
while len(guess_string)<4:
    X = random.randint(1,9)
    if str(X) not in list(guess_string):
        guess_string+=str(X)

# Player's Input
players_guess = ''
for i in range(20):
    while players_guess != guess_string:
        players_guess = input("Guess what four numbers I chose?\n")
        try:
            int(players_guess)
            if len(players_guess) != 4:
                print("Nice try. I asked for 4 numbers")
            elif len(players_guess) == 4:
                dead = 0
                wounded = 0
                for i in range(4):
                    if players_guess[i] in list(guess_string):
                        wounded+=1
                        if players_guess[i] == list(guess_string)[i]:
                            dead+=1
                            wounded-=1
                print(f"{dead} Dead, {wounded} Wounded")
                if dead == 4:
                    print("YOU WIN!!!!")
        except:
            print("Those aren't numbers!")
print(f"The number was {guess_string}")