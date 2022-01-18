import random

Computer_Choice = random.randint(1,4)
Rock,Paper,Scissor = 1,2,3
User_Choice = str(input("Please enter:\nR: Rock\nP: Paper\nS: Scissor\n"))

if (Computer_Choice==Rock and User_Choice=="S") or (Computer_Choice==Paper and User_Choice=="R") or (Computer_Choice==Scissor and User_Choice=="P"):
    print ("I win")
elif (Computer_Choice==Scissor and User_Choice=="R") or (Computer_Choice==Rock and User_Choice=="P") or (Computer_Choice==Paper and User_Choice=="S"):
    print ("You win")
else:
    print ("It is a draw")