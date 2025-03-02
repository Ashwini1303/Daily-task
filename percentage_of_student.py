'''Write a program to read the marks of 5 subjects through the keyboard Find out the
aggregate and percentage of marks obtained by the student Assume maximum marks
that can be obtained by a student in each subject as 100.'''

Total_Subject = 5
Maximum_marks = 100
Sum = 0  

for i in range(1, 6):
    marks = int(input(f"Enter marks for subject {i}: "))  
    Sum += marks  
percentage = Sum /Total_Subject
print("Total marks of all the subjects:", Sum)
print("Percentage of the student obtained:", round(percentage, 2), "%")


