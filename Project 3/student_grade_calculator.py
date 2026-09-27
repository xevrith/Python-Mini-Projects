student_name = input("Enter Student Name : ").title()

subject1 = int(input("Enter Subject 1 Marks : "))
subject2 = int(input("Enter Subject 2 Marks : "))
subject3 = int(input("Enter Subject 3 Marks : "))
subject4 = int(input("Enter Subject 4 Marks : "))
subject5 = int(input("Enter Subject 5 Marks : "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total_marks / 5

if percentage >= 90:
    grade = "A"

elif percentage >= 75 and percentage <= 89:
    grade = "B"

elif percentage >= 60 and percentage <= 74:
    grade = "C"

elif percentage >= 40 and percentage <= 59:
    grade = "D"
else:
    grade = "F"

if grade == "F":
    result = "Fail"

else:
    result = "Pass"

print(f"Student : {student_name}")
print(f"Total : {total_marks}/500")
print(f"Percentage : {percentage}%")
print(f"Grade : {grade}")
print(f"Result : {result}")



