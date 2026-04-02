mark = int(input("Enter the mark : "))

if 90<=mark<=100:
    print("Grade : A")
elif 75<=mark<=89:
    print("Grade : B")
elif 60<=mark<=74:
    print("Grade : C")
elif 45<=mark<=59:
    print("Grade : D")
elif mark<=44:
    print("Grade : F")
else:
    print("Invalid marks")