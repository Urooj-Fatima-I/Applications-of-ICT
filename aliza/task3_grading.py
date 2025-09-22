marks =int(input("enter your marks:"))

if marks >=80 and marks <= 90:
    grade = "A"
elif marks >= 65 and marks < 80:
    grade = "B"
elif marks >= 40 and marks < 65:
    grade = "C"
elif marks < 50 and marks >= 0:
    grade = "F" 
else:
    print("Invalid input")
print("your grade: ", grade)
