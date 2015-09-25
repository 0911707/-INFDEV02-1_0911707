from random import randint
while True:
    choice = raw_input("Do you choose rock, paper, scissors, lizard or spock? (press Q to quit) ")
    computer = randint(0, 4)
    if (choice == "q") or (choice == "Q"):
        break
        
    if (choice == "rock") and (computer == 0):
        print("")
        print("The computer chooses scissors, rock crushes scissors, you win!")
        print("")
    elif(choice =="rock") and (computer == 1):
        print("")
        print ("The computer also chooses rock, it's a tie")
        print("")
    elif(choice =="rock") and (computer == 2):
        print("")
        print ("The computer chooses paper, paper covers rock, you lost from a inanimate object, N00B!")
        print("")
    elif(choice =="rock") and (computer == 3):
        print("")
        print ("The computer chooses lizard, rock crushes lizard, you win!")
        print("")
    elif(choice =="rock") and (computer == 4):
        print("")
        print ("The computer chooses spock, spock vaporizes rock, you lost")
        print("")

    elif(choice =="scissors") and (computer == 0):
        print("")
        print ("The computer also chooses scissors, it's a tie")
        print("")
    elif(choice =="scissors") and (computer == 1):
        print("")
        print ("The computer chooses rock, rock crushes scissors, you lost from a inanimate object, N00B!")
        print("")
    elif(choice =="scissors") and (computer == 2):
        print("")
        print ("The computer chooses paper, scissors cuts paper, you win!")
        print("")
    elif(choice =="scissors") and (computer == 3):
        print("")
        print ("The computer chooses lizard, scissors decapitates lizard, you win!")
        print("")
    elif(choice =="scissors") and (computer == 4):
        print("")
        print ("The computer chooses spock, spock crushes scissors, you lost")
        print("")

    elif(choice =="paper") and (computer == 0):
        print("")
        print ("The computer chooses scissors, scissors beats paper, you lost from a inanimate object, N00B!")
        print("")
    elif(choice =="paper") and (computer == 1):
        print("")
        print ("The computer chooses rock, paper beats rock, you win!")
        print("")
    elif(choice =="paper") and (computer == 2):
        print("")
        print ("The computer chooses paper, it's a tie")
        print("")
    elif(choice =="paper") and (computer == 3):
        print("")
        print ("The computer chooses lizard, lizard eats paper, you lose")
        print("")
    elif(choice =="paper") and (computer == 4):
        print("")
        print ("The computer chooses spock, paper disproves spock, you win!")
        print("")

    elif(choice =="lizard") and (computer == 0):
        print("")
        print ("The computer chooses scissors ")
        print("")
    elif(choice =="lizard") and (computer == 1):
        print("")
        print ("The computer chooses rock ")
        print("")
    elif(choice =="lizard") and (computer == 2):
        print("")
        print ("The computer chooses paper ")
        print("")
    elif(choice =="lizard") and (computer == 3):
        print("")
        print ("The computer chooses lizard ")
        print("")
    elif(choice =="lizard") and (computer == 4):
        print("")
        print ("The computer chooses spock ")
        print("")

    elif(choice =="spock") and (computer == 0):
        print("")
        print ("The computer chooses scissors, spock crushes scissors, you win!")
        print("")
    elif(choice =="spock") and (computer == 1):
        print("")
        print ("The computer chooses rock, spock vaporizes rock, you win!")
        print("")
    elif(choice =="spock") and (computer == 2):
        print("")
        print ("The computer chooses paper, paper disproves spock, you lose")
        print("")
    elif(choice =="spock") and (computer == 3):
        print("")
        print ("The computer chooses lizard, lizard poisons spock, you lose")
        print("")
    elif(choice =="spock") and (computer == 4):
        print("")
        print ("The computer chooses spock, it's a tie ")
        print("")
    else:
        print("that is not possible, try again")
        