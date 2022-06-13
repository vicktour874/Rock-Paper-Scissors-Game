import random
while True:
    print ("This is a Rock, Paper and Scissors Game")
    print ("Enter R for Rock, P for Paper, S for Scissors")
    choices = ["r","p","s"]

    computer = random.choice(choices)
    player = input("r, p, or s?: ").lower()

    if player not in choices:
        print ("This is not a valid option")
    

    if player == computer:
        print ("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "r":
        if computer == "p":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Lose!")
        if computer == "s":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Win!")

    elif player == "p":
        if computer == "r":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Win!")
        if computer == "s":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Lose!")

    elif player == "s":
        if computer == "p":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Win!")
        if computer == "r":
            print ("computer: ",computer)
            print("player: ",player)
            print("You Lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Good-Bye!")
