from random import randint
while True:
    choice = raw_input("Do you choose rock, paper or scissors? (press Q to quit) ")
    computer = randint(0, 2)
    if (choice == "q") or (choice == "Q"):
        break
        
    if (choice == "rock") and (computer == 0):
        print("")
        print("The computer chooses scissors, rock beats scissors, you win!")
        print("")
    elif(choice =="rock") and (computer == 1):
        print("")
        print ("The computer also chooses rock, it's a tie")
        print("")
    elif(choice =="rock") and (computer == 2):
        print("")
        print ("The computer chooses paper, paper beats rock, you lost from a inanimate object, N00B!")
        print("")

    elif(choice =="scissors") and (computer == 0):
        print("")
        print ("The computer also chooses scissors, it's a tie")
        print("")
    elif(choice =="scissors") and (computer == 1):
        print("")
        print ("The computer chooses rock, rock beats scissors, you lost from a inanimate object, N00B!")
        print("")
    elif(choice =="scissors") and (computer == 2):
        print("")
        print ("The computer chooses paper, scissors beats paper, you win!")
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


