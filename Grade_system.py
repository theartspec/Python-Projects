#Result management system
student={}
name=input("Enter your name: ")
student ["name"]= name
student["Maths"]=int(input("Enter mark obtained for Maths:"))
student["Accountancy"]=int(input("Enter mark obtained for Accountancy:"))
student["Economics"]=int(input("Enter mark obtained for Economics:"))
total=student["Maths"]+ student["Accountancy"]+ student["Economics"]
percentage=total/3
if percentage >=90:
    print("Grade A")
elif percentage >=80:
    print("Grade B")
elif percentage >=70:
    print("Grade C")
elif percentage >=60:
    print("Grade D")
else:
    print("Grade F")
print("Student Name:", student["name"])
print("Total marks obtained:", total)
print("Percentage:", percentage,"%")