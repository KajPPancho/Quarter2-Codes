students = int(input("Enter the number of students: "))
subjects = int(input("Enter the number of subjects: "))
class_avr = 0
for i in range(1, students+1):
    print("Student" ,i)
    score_tot = 0
    for j in range(1, subjects+1):
        score = int(input("Enter score:"))
        score_tot += score
    avr = score_tot/subjects
    class_avr += avr
    print("The average score for student" ,i, "is" ,avr,)
print("The class average is" ,class_avr/students)
    
