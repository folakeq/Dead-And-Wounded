# Dead-And-Wounded
I love playing this game with my friends, but they're all busy so I created this python program to play against.
The regular name for this game is "Cows and Bulls", but my friends and I have always called it "Dead and Wounded". It's basically like hangman but with numbers.
The game I created has two different modes: "Solo Guessing" where you have 20 tries to guess a random 4-digit number, and "Guesser vs Player" where the player and the program 
each choose a random 4-digit number and take turns trying to guess their respective numbers.
This repository has three python files and three identical jupyter notebook files:

## dead_and_wounded_1_0
This program is basically the "Solo Guessing" mode of the game. A random number is generated and the player has 20 tries to guess it. With every guess you're given hints.
Wounded means one or more of the digits is right but its in the wrong spot.
Dead means one or more of the digits is right and its in the right position.
The aim is to get all "4 Dead and 0 Wounded"

## dead_and_wounded_2_0
In this program, the player gives the "Guesser" a random 4-digit number and it tries to guess what it is within a specified number of tries.
The "Guesser" gets the same hints, Wounded meaning its right but in the wrong place and Dead meaning its right and in the right place, and uses these to make its next guess.

## dead_and_wounded_game
This combines the first two programs into a game with the two modes described above. Same rules and hints apply but the game only ends when either the player or Guesser wins.

I'm open to any criticism and suggestions to make this game better. Have fun playing!
