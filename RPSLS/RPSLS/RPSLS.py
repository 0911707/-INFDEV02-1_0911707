from random import randint
while True:
    choice = raw_input("Do you choose rock, paper, scissors, lizard or spock? (press Q to quit)\n")
    computer = randint(0, 4)

    if (choice == "q") or (choice == "Q"):
        break

    if computer == 0:
        print ("The computer chooses scissors\n")
        x = "scissors"
    elif computer == 1:
        print ("The computer chooses rock\n")
        x = "rock"
    elif computer == 2:
        print ("The computer chooses paper\n")
        x = "paper"
    elif computer == 3:
        print ("The computer chooses lizard\n")
        x = "lizard"
    else:
        print ("The computer chooses Spock\n")
        x = "Spock"

    if choice == "rock":
        y = "rock"
    elif choice =="paper":
        y = "paper"
    elif choice =="scissors":
        y = "scissors"
    elif choice == "lizard":
        y = "lizard"
    elif choice == "Spock":
        y = "Spock"
    elif (choice == "q") or (choice == "Q"):
        break
    else:
        y = choice
    
    if (choice == "rock" and computer == 0) or (choice == "scissors" and computer == 2) or (choice == "paper" and computer == 1) or (choice == "rock" and computer == 3) or (choice == "scissors" and computer == 3) or (choice == "paper" and computer == 4) or (choice == "lizard" and computer == 2) or (choice == "lizard" and computer == 4) or (choice =="spock" and computer == 0) or (choice == "spock" and computer == 1):
        print(y + " beats " + x  + ", you win!\n")
    elif (choice == "rock" and computer == 1) or (choice == "scissors" and computer == 0) or (choice == "paper" and computer == 2) or (choice =="lizard" and computer == 3) or (choice == "spock" and computer == 4):
        print(x + " ties with " + y + ", it's a tie\n")
    elif (choice == "rock" and computer == 2) or (choice == "rock" and computer == 4) or (choice == "scissors" and computer == 1) or (choice == "scissors" and computer == 4) or (choice == "paper" and computer == 0) or (choice == "paper" and computer == lizard) or (choice == "lizard" and computer == 0) or (choice == "lizard" and computer == 1) or (choice == "spock" and computer == 2) or (choice == "spock" and computer == 3):
        print(x + " beats " + y + ", you lose\n")
    else:
        print(y + " is not valid, please try again")















      