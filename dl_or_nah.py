grade = float(input("Enter final grade: "))
absences = int(input("Enter absences: "))

if grade >= 90 and absences <= 5:
    print("Dean's Lister")
elif grade >= 75:
    print("Good Standing")
else:
    print("Failed")