#RPS
import random

wins = 0
losses = 0
draws = 0

print("Welcome to RPS")
play = input("Start game (Y/N):")

while play == "Y":
    choice = input("Rock/Paper/Scissors?:")

    cc1 = "Rock"
    cc2 = "Paper"
    cc3 = "Scissors"



    cchoice = random.randint(1,3)

    if cchoice == 1:
        answer = cc1
    elif cchoice == 2:
        answer = cc2
    elif cchoice == 3:
        answer = cc3

    if answer == cc1 and choice == "Rock":
        result = "Draw"
        draws += 1
    elif answer == cc1 and choice == "Paper":
        result = "Win"
        wins += 1
    elif answer == cc1 and choice == "Scissors":
        result = "Lose"
        losses += 1
    elif answer == cc2 and choice == "Rock":
        result = "Lose"
        losses += 1
    elif answer == cc2 and choice == "Paper":
        result = "Draw"
        draws += 1
    elif answer == cc2 and choice == "Scissors":
        result = "Win"
        wins += 1
    elif answer == cc3 and choice == "Rock":
        result = "Win"
        wins += 1
    elif answer == cc3 and choice == "Paper":
        result = "Lose"
        losses += 1
    elif answer == cc3 and choice == "Scissors":
        result = "Draw"
        draws += 1

    txt = "You chose {} and the computer chose {}. You {}! The session score is {} Wins, {} losses, and {} draws "
    input
    print(txt.format(choice, answer, result, wins, losses, draws))
    play = input("Start game (Y/N):")






