student_result = int(input("Please Enter your result no " ))

if student_result >101:
    print("Please try again ")
    exit()
if student_result >= 90:
    grade = "A"
if student_result >= 80:
    grade = "B"
if student_result >= 70:
    grade = "C"
if student_result >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade is", grade)