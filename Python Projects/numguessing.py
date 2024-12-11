import random

print("Welcome to the number guessing game :) ")

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range < 0:
        print("Please type a number which is greater than 0 Next time ")
        quit()
else:
    print("Please type a number next time")
    
random_num = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    
    guess = input("Make a guess : ")
    
    if guess.isdigit():
        guess = int(guess)
    
    else:
        print("Please type a number next time")
        continue
    
    if guess == random_num:
        print("Congrats,You got it ! ")
        break
    else:
        if guess > random_num:
            print("Your above the number")
        else:
            print("Your below the number")
        
print("YOU GOT IT IN",guesses,"GUESSES")
    
    