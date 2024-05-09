# Importing necessary library
import random
random.seed(43)
# Requesting type of play
name = input("Who dares challenge The Guesser?\n")
print(f"Okay {name}, this can go two ways:\n\t 1. {name}'s Solo Guessing \n\t 2. {name} vs Guesser")
game_type = input("What would it be? 1 or 2\n")
# Checking game type and executing game
try:
    int(game_type)
except:
    print("Invalid choice. Goodbye (:")
# Game Play for Player Solo Guessing
if game_type == str(1):
    print("Hope you brought your guessing top, cause you're going down. Heres's how this works:\n"+
            "I'm going to choose a random 4-digit number. Each digit is a number between 0 and 9, inclusive, and no digit is repeated\n"+
            "You get 10 tries to guess the right number, but don't worry, I'm pretty nice, I'll give you hints :)\n"+
            "If the number you guess has some of the same digits as mine, and it's in the right position, I'll say Dead\n"+
            "and if it's not in the right position, I'll say Wounded.\nI think that's fair enough right?\nOkay. Let's play!")
    
    # Choosing a random number
    guess_string = ""
    while len(guess_string)<4:
        X = random.randint(0,9)
        if str(X) not in list(guess_string):
            guess_string+=str(X)
    
    # Player's Input
    players_guess = ''
    for i in range(10):
        if players_guess != guess_string:
            players_guess = input("Guess what four numbers I chose?\n")
            try:
                int(players_guess)
                if len(players_guess) != 4:
                    print("Nice try. I asked for 4 numbers\n")
                elif len(players_guess) == 4:
                    dead = 0
                    wounded = 0
                    for i in range(4):
                        if players_guess[i] in list(guess_string):
                            wounded+=1
                            if players_guess[i] == list(guess_string)[i]:
                                dead+=1
                                wounded-=1
                    print(f"{dead} Dead, {wounded} Wounded\n")
                    if dead == 4:
                        print("YOU WIN!!!")
            except:
                print("Those aren't numbers! Try again \n")
    if guess_string != players_guess:
        print(f"YOU LOSE! The number was {guess_string}")

# Game play for Player vs Guesser
elif game_type == str(2):
    print("Hope you brought your guessing top, cause you're going DOWN. Heres's how this works:\n"+
          "You and I are going to choose random 4-digit numbers. Each digit is a number between 0 and 9, inclusive, and no digit is repeated\n"+
          "We have to guess each other's numbers until one of us gets it right. After each guess we get a hints about our guesses\n"+
          "Dead - The number guessed has some of the same digits, and is in the right position as our target number\n"+
          "Wounded - The number guessed has some of the same digits, but it's not in the right position as our target number.\nOkay. Let's play!")
    
    # Requesting and verifying player's random number
    guessing_number = input("Give me a 4-digit number, no repitition\n")
    for i in range(5):
        if len(guessing_number)==4:
            if len(set(guessing_number))==4:
                try:
                    int(guessing_number)
                except:
                    print(f"That's not a number. You have {4-i} more chances to do this right, don't be sneaky now\n")
                    guessing_number = input("Give me a 4-digit number, no reptition\n")
            else:
                print(f"You repeated! You have {4-i} more chances to do this right\n")
                guessing_number = input("Give me a 4-digit number, no reptition\n")
        else:
            print("That's not 4-digits :(\n")
            guessing_number = input("Give me a 4-digit number, no reptition\n")
    
    # Checking player's number after the 5 trials
    players_number = ""
    if len(guessing_number)==4:
        if len(set(guessing_number))==4:
            try:
                int(guessing_number)
                players_number = guessing_number
            except:
                print("You still didn't get it right. I'm not playing with you anymore :(")
        else:
            print("You still didn't get it right. I'm not playing with you anymore :(")
    else:
        print("You still didn't get it right. I'm not playing with you anymore :(")
        
    # Choosing Lord Guesser's number
    guesser_number = ""
    while len(guesser_number)<4:
        X = random.randint(0,9)
        if str(X) not in list(guesser_number):
            guesser_number+=str(X)
   
    # Initializing guesser
    if players_number != "":
        all_guesses = []
        while len(all_guesses) != 5040:
            guess_string = ''
            while len(guess_string)<4:  
                X = random.randint(0,9)
                if str(X) not in list(guess_string):
                    guess_string+=str(X)
            if guess_string not in all_guesses:
                all_guesses.append(guess_string)
    
    # Playing starts
    players_guess = ''
    guesser_guess = ''
    guess_list = []
    outcome_list = []
    while players_guess != guesser_number and guesser_guess != players_number:
        # Collecting guessses
        guesser_guess = all_guesses[random.randint(0,len(all_guesses)-1)]
        guess_list.append(guesser_guess)
        players_guess = input("Guess what four numbers I chose? ")
        # Checking player's guess
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
                print(f"Your guess {players_guess} - {dead} Dead, {wounded} Wounded\n")
                if dead == 4:
                    print("YOU WIN!!!")
                    break
        except:
            print("Those aren't numbers!\n YOU LOSE!")
            break
    
        # Checking Lord Guesser's Guess
        if guesser_guess != players_number:
            l_dead = 0
            l_wounded = 0
            for i in range(4):
                if guesser_guess[i] in list(players_number):
                        l_wounded+=1
                        if guesser_guess[i] == list(players_number)[i]:
                            l_dead+=1
                            l_wounded-=1
            print(f"My guess {guesser_guess} - {l_dead} Dead, {l_wounded} Wounded\n\n")
            outcome = [l_dead, l_wounded]
            outcome_list.append(outcome)                            
            if l_dead == 0 and l_wounded == 0:
                for num in all_guesses:
                    lst = list(num)
                    for i in range(4):
                        if guesser_guess[i] in lst:
                            if num in all_guesses:
                                all_guesses.remove(num)
            elif l_dead == 0 and l_wounded > 0:
                for num in all_guesses:
                    lst = list(num)
                    for i in range(4):
                        if guesser_guess[i] == lst[i]:
                            if num in all_guesses:
                                all_guesses.remove(num)                                 
            elif l_dead>0 and l_wounded >= 0:
                options = []
                for num in all_guesses:
                    lst = set(num)
                    lst_g = set(guesser_guess)
                    for i in range(4):
                        if len(lst_g.intersection(lst)) == 0:
                            if num in all_guesses:
                                all_guesses.remove(num)
                if len(outcome_list) > 1:
                    for j in range(len(outcome_list)):
                        if outcome_list[j][0] > 0:
                            lst_p = set(guess_list[j])
                            lst_g = set(guesser_guess)
                            lst_d = lst_g.intersection(lst_p)
                            if len(lst_d) != 0:
                                for num in all_guesses:
                                    lst = set(num)
                                    if len(lst_d.intersection(lst))>0:
                                        if num in all_guesses:
                                            options.append(num)
        else:
            print("I WIN!!!")
            break
