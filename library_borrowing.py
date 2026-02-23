
print("=== Library System ===")

student_name = input("Enter student name: ")
book_title = input("Enter book title: ")
days_borrowed = int(input("Enter number of days borrowed: "))

allowed_days = 7
fine_per_day = 10

if days_borrowed > allowed_days:
    late_days = days_borrowed - allowed_days
    fine = late_days * fine_per_day
else:
    fine = 0

print("\n--- BORROWING SUMMARY ---")
print("Student:", student_name)
print("Book:", book_title)
print("Days Borrowed:", days_borrowed)
print("Fine:", fine)