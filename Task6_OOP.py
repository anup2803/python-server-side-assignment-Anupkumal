#Develop a simple OOP-based Python class Student with attributes like name, roll 
#number, and marks. Implement methods to input and display details.


class Students:
    def input_details(self):
     self.name=input("Enter a name")
     self.roll_number=int(input("Enter a roll number"))
     self.marks=float(input("Enter a marks "))

    def display(self):
        print("Students detailes")
        print(f"Name {self.name}")
        print(f"Name {self.roll_number}")
        print(f"Name {self.marks}")




stu=Students()
stu.input_details()
stu.display()