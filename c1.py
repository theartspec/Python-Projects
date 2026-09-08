#Marksystem 
mark = int(input("Enter your marks: "))
if mark>=100 and mark<=90:
    print("Grade: A+")
elif mark>=80 and mark<90:
    print("Grade: A")
elif mark>=70 and mark<80:
    print("Grade: B+")
elif mark>=60 and mark<70:
    print("Grade: B")
elif mark>=50 and mark<60:
    print("Grade: C+")
elif mark>=40 and mark<50:
    print("Grade: C")
elif mark>=25 and mark<40:
    print("Grade: D")
else:
    print("Fail")