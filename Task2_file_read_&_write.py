# Create a program that takes a list of student names and stores them in a file. Then, read the file and display the contents.

student=[]
number_of_student=int(input("Enter a number "))
for i in range(number_of_student):
    name_of_students=input("enter a  name of students ")
    student.append(name_of_students) 

with open("Students.txt","w") as f:
    for name in student:
        f.write(name +"\n")
 
print("Successfuly written in file ")



print("Read the file and display ")
with open("Students.txt","r")as f:
    print(f.read())