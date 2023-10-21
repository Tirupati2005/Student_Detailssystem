# Menu Driven Prog for Student Management System using Dict and class.
db = {}
class Student(object):
     def __init__(self , name , marks , roll_num):
         self.name = name
         self.marks = marks
         self.roll_num = roll_num
     
     def save(self):
         db[self.name] = self
         
     def display(self):
         print(f'Student Name is {self.name} Student marks are {self.marks} and roll number is {self.roll_num}')

     @classmethod
     def show_all_students(cls):
             for x in db:
                 obj = db.get(x)
                 obj.display()
                 print('--'*50)
     
     @classmethod
     def get_student_data(cls , name):
         if name in db:
             obj = db.get(name) 
             print(obj)
             obj.display()
         else:
             print(f'Student {name} object is not found')
     
     @classmethod
     def delete_student(cls , name):
         if name in db:
             del db[name]
         else:
             print(f"student {name} is not fount to delete")
     
     @classmethod
     def update_student_data(cls , name):
         if name in db:
             obj = db.get(name)
             obj.name = input("Enter Updated Student Name: ")
             obj.marks = input("Enter Updated Student marks: ")
             obj.roll_num = input("Enter Updated Student roll number: ")
             obj.save()
         else:
             print(f"student {name} is not fount to update")
 

while True:
     print("""
     1) List of Student
     2) Add Student
     3) Update Student
     4) Delete Student
     """)
     choice = input("Enter your choice: ")
     if choice == '1':
         Student.show_all_students()
     elif choice == '2':
         name = input("Enter Student Name: ")
         marks = eval(input("Enter Student marks: "))
         roll_num = eval(input("Enter Student roll number: "))
         obj = Student(name , marks , roll_num)
         obj.save() 
     elif choice == '3':
         name = input("Enter Student Name To Update: ")
         Student.update_student_data(name)
     elif choice == '4':
         name = input("Enter Student Name To Delete: ")
         Student.delete_student(name)
     ch = input("Do you want to continue the prog [y / n]: ")
     if ch.lower() == 'n':
      break
