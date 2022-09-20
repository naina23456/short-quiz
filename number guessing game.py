import random

top_of_range = input("Type a number upto which you want to generate : ")

#chceking if user has enter an integer or not
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if(top_of_range<=0):
        print("Please enter a number larger than 0 next time :")
        quit()
else:
    print("Please enter a number next time :")
    quit()
    
random_number = random.randint(0,top_of_range)


while True:
    user_guess = input("Make a guess : ")
    
    #checking if user has guessed an integer or not
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if(user_guess<=0):
            print("Please enter a number larger than 0 next time :")
            continue
    else:
        print("Please enter a number next time :")
        continue
    
    if(user_guess == random_number):
        print("Hurray ! Correct ")
        break;
    else:
        if(user_guess > random_number):
            print("The correct answer is below your guess")
        else:
            print("The correct answer is above your guess")
           
    
