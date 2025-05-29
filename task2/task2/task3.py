import csv

name=input("enter your name")
maths=input("enter marks for maths")
science=input("enter marks for science")
english=input("enter marks for english")

maths=int(maths)
science=int(science)
english=int(english)

with open("student_data.csv","a",encoding="utf-8")as newfile:
    new=csv.writer(newfile)
    new.writerow([name,maths,science,english])

