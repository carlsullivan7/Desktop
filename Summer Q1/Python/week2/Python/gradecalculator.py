numberGrade = input("Enter your number grade (1-100): ")
letterGrade = ""
numberGrade = int(numberGrade)
if numberGrade >= 90:
    letterGrade = "A"
elif numberGrade >= 80:
    letterGrade = "B"
elif numberGrade >= 70:
    letterGrade = "C"
elif numberGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print("You got a " + letterGrade)