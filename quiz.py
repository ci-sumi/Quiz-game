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
    