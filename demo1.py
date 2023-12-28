# marks=85
# by default it is string  so here type casted
marks = int(input("enter marks you obtained  "))
if marks >= 80:
    print("You will be the part of A0 batch")
elif marks >= 60 and marks < 80:
    print("you will be the part of A1 batch")
elif marks >= 40 and marks < 60:
    print("you will be the part of A2 batch")
else:
    print("you will be the part of A3 batch")
