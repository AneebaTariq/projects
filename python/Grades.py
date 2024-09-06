m = eval(input("Enter your marks : "))
if m <= 100 and m>=80:
    print("Grade : A")
elif m < 80 and m >= 70:
    print("Grade : B")
elif m < 70 and m >= 60:
    print("Grade : C")
elif m < 60 and m >= 50:
    print("Grade : D")
elif m < 50 and m >= 0:
    print("Grade : F")
else:
    print("Invalid Input")