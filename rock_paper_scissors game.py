import random 

user_wins = 0
computer_wins = 0 
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    
    if(user_input == "q"):
        break
    
    if user_input not in ["rock","paper","scissors"]:
        print("Please make a valid choice")
        continue
    random_number = random.randint(0,2)
    # rock :0, paper:1, scissors:2
    
    if(user_input == "rock"):
        if(random_number == 0):
            print("both chose same .It's a tie ")
        elif(random_number == 1):
            print("Computer : Paper")
            print("Computer wins")
            computer_wins+=1
        else:
            print("Computer : Scissors")
            print("Yayy ! You win this time .")
            user_wins+=1
            
    elif(user_input == "paper"):
        if(random_number == 0):
            print("Computer :Rock ")
            print("Yayy : You win")
            user_wins+=1
        elif(random_number == 1):
            print("Both chose same .It's a tie")
        else:
            print("Computer : Scissors")
            print("Computer wins")
            computer_wins+=1
    else:
        
        if(random_number == 0):
            print("Computer : Rock")
            print("Computer wins")
            computer_wins+=1
        elif(random_number == 1):
            print("Computer : Paper")
            print(" Yayy ! You win this time ")
            user_wins+=1
        else:
            print("Both chose same .It's a tie")
            
        
print(" Your Score :",user_wins)
print(" Computer Score :",computer_wins)
if(user_wins > computer_wins):
    print("Hurray ! You won")
elif(user_wins == computer_wins):
    print("Tough match ! It's a tie")
else:
    print("Computer wins. Better luck next time !!")
    
    

print("Goodbye !")
        
           
        
            
        
    
    
    

        

