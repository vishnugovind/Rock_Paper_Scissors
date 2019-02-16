def rps():
    print("Ready to Play.....")
    time.sleep(1)
    print ("Rock!")
    time.sleep(1)
    print ("Paper!")
    time.sleep(1)
    print ("Scissors!")
    time.sleep(1)
    name = input("What is your name?:")
    print("Thanks " + name + ". Now lets get ready to play")

    def game():
        wins = 0
        losses = 0
        ties = 0
        while True:
            while True:
                print ("")
                print ("Wins: %s    Losses: %s    Ties: %s   " % (wins, losses, ties))
                turn = input("Enter (R) for Rock, (P) for Paper, (S) for Scissors, or (Q) to quit")
                turn = turn.upper()
                if turn == "Q":
                    return
                elif turn == "R" or turn == "P" or turn == "S":
                    break
            if turn == "R":
                turn = "Rock"
            elif turn == "P":
                turn = "Paper"
            elif turn == "S":
                turn = "Scissors"
            print("You chose " + turn)
            time.sleep(1)
            comp = random.randint(1, 3)
            if comp == 1:
                comp = "Rock"
            elif comp == 2:
                comp = "Paper"
            elif comp == 3:
                comp = "Scissors"
            print("The computer chose " + comp)

            if turn == comp:
                print ("TIE")
            elif turn == "Rock" and comp == "Paper":
                print (name + ", you lost this round :(")
                losses = losses + 1
                time.sleep(1)
            elif turn == "Rock" and comp == "Scissors":
                print (name + ", you won this round!")
                wins = wins + 1
                time.sleep(1)
            elif turn == "Paper" and comp == "Rock":
                print (name + ", you won this round!")
                wins = wins + 1
                time.sleep(1)
            elif turn == "Paper" and comp == "Scissors":
                print (name + ", you lost this round :(")
                losses = losses + 1
                time.sleep(1)
            elif turn == "Scissors" and comp == "Rock":
                print(name + ", you lost this round :(")
                losses = losses + 1
                time.sleep(1)
            elif turn == "Scissors" and comp == "Paper":
                print(name + ", you won this round!")
                wins = wins + 1
                time.sleep(1)

    game()






rps()
