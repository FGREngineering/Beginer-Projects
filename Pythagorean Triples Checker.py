#Triples Checker


start = input("Enter Triples Checker (Y/N):")

while start == "Y":
    s1 = input("Enter side one:")
    s2 = input("Enter side two:")
    s3 = input("Enter side three:")

    a = int(s1) ** 2
    b = int(s2) ** 2
    c = int(s3) ** 2

    if a + b == c:
        answer = 'True'
    elif a + c == b:
        answer = 'True'
    elif b + c == b:
        answer = 'True'
    elif b + c == a:
        answer = 'True'
    else:
        answer = 'False'

    print(answer)
    start = input("Enter Triples Checker (Y/N):")
