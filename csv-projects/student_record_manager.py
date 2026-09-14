import csv

file = open("students.csv", "a", newline="")

writer = csv.writer(file)

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

writer.writerow([name, roll, marks])

file.close()

print("Student record saved!")
