# Write Python code to read from a CSV file of student marks and calculate average marks.

import csv



# def write_students_csv(filename):
#     students=[
#         {"Name":"Anup","Roll Number":5,"marks":95},
#         {"Name":"sandip","Roll Number":25,"marks":75},
#         {"Name":"Susan","Roll Number":15,"marks":29},
#         {"Name":"Mainsh","Roll Number":55,"marks":60}
#     ]


    
#     with open(filename,"w",newline='') as f:
#      filedname=["Name","Roll Number","marks"]
#      obj = csv.DictWriter(f, fieldnames= filedname)

     

#      obj.writeheader()
#      obj.writerows(students)
     


#     print("Successfuly witeen into the csv file")


# write_students_csv('studnets.csv')











#to read the marks from the csv file and calculate average marks.

def calculateaverage(filename):
    total_marks=0
    student_count=0

    with open(filename,'r')as f:
      obj=csv.DictReader(f)

      for row in obj:
         try:
            marks= float(row['marks'])
            total_marks += marks
            student_count += 1
         except ValueError:
            print("Invalid marks found")

    if student_count == 0:
        print("no students record found")

    else:
        average=total_marks/student_count
        print(f"Total average of {student_count} is {average}")


calculateaverage('students.csv')





