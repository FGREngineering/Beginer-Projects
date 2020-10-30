import random

ans1 = "Yes"
ans2 = "Certainly"
ans3 = "No doubt fam"
ans4 = "fam dw about it"
ans5 = "lol fosho"
ans6 = "probably"
ans7 = "deffaz"
ans8 = "what am i, a magic conch? lol jkjk yes"
ans9 = "YES"
ans10 = "idk"
ans11 = "nah fom"
ans12 = "no"
ans13 = "NO"
ans14 = "dont think so m8"
ans15 = "loll no"
ans16 = "maybe? Nahh"
ans17 = "thats a great question. wish i knew"
ans18 = "sorry what?"
ans19 = "mate whats wrong with u"
ans20 = "look, this isn't really what you want to know"




greeting = "All heil the magic CONCH"
print(greeting)
question = input("What do you have to ask the magic conch?:")

choice = random.randint(1,20)

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
elif choice == 8:
    answer = ans8
elif choice == 9:
    answer = ans9
elif choice == 10:
    answer = ans10
elif choice == 11:
    answer = ans11
elif choice == 12:
    answer = ans12
elif choice == 13:
    answer = ans13
elif choice == 14:
    answer = ans14
elif choice == 15:
    answer = ans15
elif choice == 16:
    answer = ans16
elif choice == 17:
    answer = ans17
elif choice == 18:
    answer = ans18
elif choice == 19:
    answer = ans19
elif choice == 20:
    answer = ans20
print("THINKING \nTHINKING\nTHINKING")
print("Magic 8 ball:", answer)