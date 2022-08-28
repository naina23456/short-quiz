name = input("Hello user . Please tell me your name :- ")
print("Welcome ", name)



def game():
    questions = ["What is the full form of CPU ? ","Where is Bangla Sahib Gurudwara ? ","Is Australia in Asia ? ","What is the capital of Telangana ? "]
    answers = ["central processing unit","new delhi","no","hyderabad"]
    i=0
    score = 0
    while(i<len(questions)):
        print("Your question no. ",i+1, "is:" , questions[i])
        ans = input("Please enter your answer : ")
        
        if(ans.lower() == answers[i]):
            print("Right answer")
            score+=1
        else:
            print("Wrong answer . The right answer is ->> ' "  , answers[i] , " ' ")
        i+=1
    
    return score
a = 2
j=0
while(a == 2):
    if(j!=0):
        print("Welcome again !")
    y_n  = input("Do you want to play ? : ")
    
    
    if(y_n.lower()== "yes"):
        print("There are  4 questions")
        sc = game()
        print("Your score is  = ", sc)
    
    else:
        print("Okay . Maybe next time")
        break
    j = 4
   
    

    
    

    