import csv

with open("student_data.csv","r",encoding="utf-8")as myfile:
    data= csv.reader(myfile)
    students=[]
    top_scorer=None
    highest_marks=-1
    next(data)
    

    for row in data:
         if len(row)<4:
             continue
        
         name=row[0]
         maths=int(row[1])
         science=int(row[2])
         english=int(row[3])

         total=maths+science+english
         average=total/3

         students.append([name,maths,science,english,total,average])
         if total>highest_marks:
            highest_marks=total
            top_scorer=name
    
    for student in students:
        print(f"for {student[0]}")
        print(f"maths:{student[1]},science:{student[2]},english:{student[3]} and the total score is {student[4]} whereas the average of all 3 is {student[5]}")
    print(f"highest scorer is {top_scorer} with marks {highest_marks}")
