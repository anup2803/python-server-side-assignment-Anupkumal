# Implement a program to store student records (name, roll, marks,contact number) using a 
# dictionary.
# a. Provide menu options to add, search, and display students.



students={}



#Add the students in the studnets dictionarys
def add_students():
   roll_number=int(input("Enter a roll number:"))
   if roll_number in students:
      print("Roll number is aleready exits in students dictionary")
      return
   else:
       name=input("Enter a name of the student")
       marks=input("Enter a marks number")
       contact=input("Enter a contact number")
       students[roll_number] = {'name': name, 'marks': marks, 'contact_number': contact}
       print("Sucessfuly Stored")
   print("\n")

 




#Search the students records from the dictionary

def search_students():
    roll_number = int(input("Enter roll number to search: "))
    if roll_number in students:
        print("\n Student Details:")
        print("Name:", students[roll_number]['name'])
        print("Marks:", students[roll_number]['marks'])
        print("Contact Number:", students[roll_number]['contact_number'])   
    else:
        print("Student not found")

    print("\n")






#display the students records from the dictionary
def display_students():
    if not students:
        print("No student records available.\n")
        return
    print("\n All Student Records:")
    for roll_number, info in students.items():
        print(f"Roll Number: {roll_number}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Contact Number: {info['contact_number']}\n")




#main functions to call the another functions
def main():

      while True:
         print("Student Records Options")
         print("1. Add Students")
         print("2. Search Students")
         print("3. Display Studnets")
         print("4. Exit")
         choice=input("Enter your choice(1-4)")

         if choice=='1':
            add_students()

         elif choice=='2':
            search_students()
         
         elif choice=='3':
            display_students()

         elif choice=='4':
            print("Existing the program")
            break
         else:
            print("Invalid choice! Please try again \n0")




#calling the main  functions
main()

