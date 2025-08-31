# Take multiple students’ names and their subjects with marks (use list of tuples).
students=[]
n=int(input("Enter number of student: "))
for i in range(n):
    name=input(f"Enter {i+1} student name: ")
    num_sub=int(input(f"How many subject for {name}: "))
    subjects=[]
    for  j in range(num_sub):
        sub_name=input(f"Enter {j+1} subject name:")
        sub_marks=int(input("Enter marks of corresponding subject: "))
        subjects.append((sub_name,sub_marks))
    students.append((name,subjects))

print("\n--- Student Records ---")
for student in students:
    print(f"\nStudent Name: {student[0]}")
    for sub,marks in student[1]:
        print(f"  {sub}: {marks}")
    

        
        


# Enter number of students: 2

# Student 1 name: Alice
# How many subjects? 3
# Enter subject and marks (e.g., Math 90):
# Math 90
# English 85
# Science 92

# Student 2 name: Bob
# How many subjects? 2
# Enter subject and marks:
# Math 78
# English 88



#example
# Student Management System

# students = {}  # Dictionary to store student data {roll_no: (name, age, course)}

# def add_student():
#     roll = input("Enter Roll No: ")
#     if roll in students:
#         print("Student already exists!")
#     else:
#         name = input("Enter Name: ")
#         age = input("Enter Age: ")
#         course = input("Enter Course: ")
#         students[roll] = (name, age, course)
#         print("Student added successfully!\n")

# def view_students():
#     if not students:
#         print("No student records found.\n")
#     else:
#         print("\n--- Student Records ---")
#         for roll, data in students.items():
#             print(f"Roll No: {roll}, Name: {data[0]}, Age: {data[1]}, Course: {data[2]}")
#         print()

# def search_student():
#     roll = input("Enter Roll No to search: ")
#     if roll in students:
#         data = students[roll]
#         print(f"Found → Roll No: {roll}, Name: {data[0]}, Age: {data[1]}, Course: {data[2]}\n")
#     else:
#         print("Student not found!\n")

# def update_student():
#     roll = input("Enter Roll No to update: ")
#     if roll in students:
#         name = input("Enter New Name: ")
#         age = input("Enter New Age: ")
#         course = input("Enter New Course: ")
#         students[roll] = (name, age, course)
#         print("Student updated successfully!\n")
#     else:
#         print("Student not found!\n")

# def delete_student():
#     roll = input("Enter Roll No to delete: ")
#     if roll in students:
#         del students[roll]
#         print("Student deleted successfully!\n")
#     else:
#         print("Student not found!\n")

# # Main Loop
# while True:
#     print("===== Student Management System =====")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == '1':
#         add_student()
#     elif choice == '2':
#         view_students()
#     elif choice == '3':
#         search_student()
#     elif choice == '4':
#         update_student()
#     elif choice == '5':
#         delete_student()
#     elif choice == '6':
#         print("Exiting Student Management System. Goodbye!")
#         break
#     else:
#         print("Invalid choice! Please try again.\n")



# Store data in a dictionary where the student’s name is the key and marks are the value.

# Use loops to enter and process multiple students.

# Use strings to display formatted report cards.

# Allow the user to search for a student’s report.