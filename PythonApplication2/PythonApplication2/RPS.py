from random import randint
while True:
    choice = raw_input("Do you choose rock, paper or scissors? (press Q to quit) \n")
    computer = randint(0, 2)
    if computer == 0:
        print ("The computer chooses scissors\n")
        x = "scissors"
    elif computer == 1:
        print ("The computer chooses rock\n")
        x = "rock"
    else:
        print ("The computer chooses paper\n")
        x = "paper"

    if choice == "rock":
        y = "rock"
    elif choice =="paper":
        y = "paper"
    else:
        y = "scissors"

    if (choice == "q") or (choice == "Q"):
        break
    
    if (choice == "rock" and computer == 0) or (choice == "scissors" and computer == 2) or (choice == "paper" and computer == 1):
        print(y + " beats " + x  + ", you win!\n")
    elif (choice == "rock" and computer == 1) or (choice == "scissors" and computer == 0) or (choice == "paper" and computer == 2):
        print(x + " ties with " + y + ", it's a tie\n")
    else:
        print(x + " beats " + y + ", you lose\n")


    
    
    
    

    
    
    
    
        



