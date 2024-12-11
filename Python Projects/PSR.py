import random

print("Welcome to the Rock Paper Scissor Game ! ")

options = ["rock","paper",'scissor']

user_wins = 0
computer_wins = 0

while True:

    user_input = input("Type Rock/Paper/Scissor or Q for quit : ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_num = random.randint(0,2)
    
    auto_choice = options[random_num]
    
    print("Computer_picked : " + auto_choice)
    
    if user_input == 'Rock' and auto_choice == 'scissor':
        print("Congrats,You win !")
        user_wins += 1
        
    
    elif user_input == 'paper' and auto_choice == 'rock':
        print("Congrats,You win !")
        user_wins += 1
        
    
    elif user_input == 'scissor' and auto_choice == 'paper':
        print("Congrats,You win !")
        user_wins += 1
        
    
    else:
        print("You lost !")
        computer_wins += 1
        
print("YOU WON " + str(user_wins) + " TIMES")
print("COMPUTER WON " + str(computer_wins) + " TIMES")
print("GOOD BYE :)")