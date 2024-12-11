print("Welcome to MY Quiz Game :) ")

playing = input("DO you want to play ? ")

if playing.lower() != "yes":
    quit()
else:
    print("OK Let's Play :) ")
    
score = 0
    
answer = input("What does CPU stands for ? ")
if answer.lower() == "central processing unit":
    print(" 7 Crore")
    score += 1
else:
    print("Incorrect!\n The correct answer is central processing unit")
    
answer = input("What does GPU satnds for ? ")
if answer.lower() == "graphics processing unit":
    print(" 7 Crore")
    score += 1
    
else:
    print("Incorrect!\nThe correct answer is graphics processing unit")
    
answer = input("What does RAM stands for ? ")
if answer.lower() == "random access memory":
    print(" 7 Crore")
    score += 1
else:
    print("Incorrect!\nThe correct answer is random access memory")
    
answer = input("What does ROM stands for ? ")
if answer.lower() == "read only memory":
    print(" 7 Crore")
    score += 1
else:
    print("Incorrect!\nThe correct answer is read only memory")
    
answer = input("What TIT stands for ? ")
if answer.lower() == "technocrats institute of technology":
    print(" 7 Crore")
    score += 1
else:
    print("Incorrect!\nThe correct answer is technocrats institute of technology ")
    
print("You got " + str(score) + " questions correct!")

print("Your scoring percentage is " + str((score/5) * 100) +" %")


