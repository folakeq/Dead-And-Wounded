# Importing necessary libraries
import random
random.seed(43)

# Verifying the player's number
players_number = input("Give me a 4-digit number, no repitition\n")
for i in range(5):
    if len(players_number)==4:
        if len(set(players_number))==4:
            try:
                int(players_number)
            except:
                print(f"That's not a number. You have {4-i} chances, don't be sneaky now\n")
                players_number = input("Give me a 4-digit number, no reptition\n")
        else:
            print(f"You repeated! You have {4-i} chances\n")
            players_number = input("Give me a 4-digit number, no reptition\n")
    else:
        print("That's not 4-digits :(\n")
        players_number = input("Give me a 4-digit number, no reptition\n")

# Checking player's number after the 5 trials
guessing_number = ""
if len(players_number)==4:
    if len(set(players_number))==4:
        try:
            int(players_number)
            guessing_number = players_number
        except:
            print("You still didn't get it right. I'm not playing with you anymore :(")
    else:
        print("You still didn't get it right. I'm not playing with you anymore :(")
else:
    print("You still didn't get it right. I'm not playing with you anymore :(")

# Initializing guesser
if guessing_number != "":
    all_guesses = []
    while len(all_guesses) != 5040:
        guess_string = ''
        while len(guess_string)<4:  
            X = random.randint(0,9)
            if str(X) not in list(guess_string):
                guess_string+=str(X)
        if guess_string not in all_guesses:
            all_guesses.append(guess_string)
# Guesser
guess_list = []
outcome_list = []
tries=0
for i in range(50):
    guess = all_guesses[random.randint(0,len(all_guesses)-1)]
    guess_list.append(guess)
    tries+=1
    if guess != players_number:
        dead = 0
        wounded = 0
        for i in range(4):
            if guess[i] in list(guessing_number):
                wounded += 1
                if guess[i] == list(guessing_number)[i]:
                    dead += 1
                    wounded -= 1
        print(f"{guess} {dead} Dead, {wounded} Wounded")
        outcome = [dead, wounded]
        outcome_list.append(outcome)
        
        # Criteria for new guess
        if dead == 0 and wounded == 0:
            for num in all_guesses:
                for i in range(4):
                    if guess[i] in list(num):
                        if num in all_guesses:
                            all_guesses.remove(num)
        elif dead == 0 and wounded > 0:
            for num in all_guesses:
                lst = list(num)
                for i in range(4):
                    if guess[i] == lst[i]:
                        if num in all_guesses:
                            all_guesses.remove(num)                                 
        elif dead > 0 and wounded >= 0:
            options = []
            for num in all_guesses:
                lst = set(num)
                lst_g = set(guess)
                if len(lst_g.intersection(lst)) == 0:
                    if num in all_guesses:
                        all_guesses.remove(num)
            if len(outcome_list) > 1:
                for j in range(len(outcome_list)):
                    if outcome_list[j][0] > 0:
                        lst_p = set(guess_list[j])
                        lst_g = set(guess)
                        lst_d = lst_g.intersection(lst_p)
                        if len(lst_d) != 0:
                            for num in all_guesses:
                                lst = set(num)
                                if len(lst_d.intersection(lst))>0:
                                    if num in all_guesses:
                                        options.append(num)
    else:
        print("I WIN!!!")
        print(f"Took me only {tries} tries :)")
        break