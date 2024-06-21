print("Welcome to the quiz:")
play=input("Do you want to play the quiz:yes/no?").lower()
if play !="yes":
    quit()
else:
    answer =input("Who was the first President of the Palestine?").title()
    if(answer=="Mahmoud Abbas"):
        print("Correct")
    else:
        print("its in correct")
    answer =input('Who wrote the play "Romeo and Juliet":?').title()
    if(answer=="William Shakespeare"):
        print("Correct")
    else:
        print("its in correct")
    answer =int(input('How many players are there in a soccer team on the field?'))
    if(answer==11):
        print("Correct")
    else:
        print("its in correct")
        
    answer =input('What does CPU stand for in computing?')
    if(answer=="Central Processing Unit"):
        print("Correct")
    else:
        print("its in correct")
    
    