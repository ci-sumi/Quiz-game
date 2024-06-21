print("Welcome to the quiz:")
play=input("Do you want to play the quiz:yes/no?").lower()
score =0
if play !="yes":
    quit()
else:
    answer =input("Who was the first President of the Palestine?").title()
    if(answer=="Mahmoud Abbas"):
        print("Correct")
        score+=1
    else:
        print("its in correct")
    answer =input('Who wrote the play "Romeo and Juliet":?').title()
    if(answer=="William Shakespeare"):
        print("Correct")
        score+=1
    else:
        print("its in correct")
    answer =int(input('How many players are there in a soccer team on the field?'))
    if(answer==11):
        print("Correct")
        score+=1
    else:
        print("its in correct")
        
    answer =input('What does CPU stand for in computing?')
    if(answer=="Central Processing Unit"):
        print("Correct")
        score+=1
    else:
        print("its in correct")
    
print(f"your total score is:{(score/4)*100}%")
if(score>=4):
    print("Congratulations")
else:
    print("keep trying!!")
    
    