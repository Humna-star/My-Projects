import random #Importing modules
playing = True #Intialise
number = str(random.randint(0,9)) #Random in built Function

print("I'll generate a number from 0 to 9, and you have to guess the numer one digit at a time.")
print("The game end when you get one hero")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
     print("You win the game")
     print("The number was", number)
     break
    else:
     print("Your guess isn't quite right, Try again. \n")