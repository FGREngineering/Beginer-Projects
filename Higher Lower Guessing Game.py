import random
start = input("Enter H/L Game (Y/N):")

while start == "Y":
    c_selction = random.randint(1,100)

    h_selection = int(input("Enter your numerical guess (Y/N):"))
    while h_selection != c_selction:
        if h_selection > c_selction:
            print("Lower!")
        else:
            print("Higher!")
        h_selection = int(input("Enter your numerical guess (Y/N):"))

    print("Correct!")
    start = input("Play Again? (Y/N):")