class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def work(self):
        print(f"{self.name} is working as a {self.position}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} with ID {self.student_id} is studying")


class University:
    def __init__(self):
        self.employees = []
        self.students = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_employee(self, name_or_id):
        for employee in self.employees:
            if employee.name == name_or_id or employee.position == name_or_id:
                self.employees.remove(employee)
    
    def remove_student(self, name_or_id):
        for student in self.students:
            if student.name == name_or_id or student.student_id == name_or_id:
                self.students.remove(student)
    
    def find_person(self, name_or_id):
        for employee in self.employees:
            if employee.name == name_or_id or employee.position == name_or_id:
                return employee
        for student in self.students:
            if student.name == name_or_id or student.student_id == name_or_id:
                return student
        return None
    
    def show_info(self):
        print("Employees:")
        for employee in self.employees:
            employee.introduce()
            employee.work()
        print("\nStudents:")
        for student in self.students:
            student.introduce()
            student.study()



employee1 = Employee("John", 30, "Professor")
employee2 = Employee("Alice", 25, "Assistant")
student1 = Student("Bob", 20, "S12345")
student2 = Student("Emma", 22, "S67890")

university = University()
university.add_employee(employee1)
university.add_employee(employee2)
university.add_student(student1)
university.add_student(student2)

university.show_info()

print("\nRemoving employee Alice:")
university.remove_employee("Alice")

print("\nRemoving student with ID S67890:")
university.remove_student("S67890")

print("\nAfter removal:")
university.show_info()

print("\nFinding person by name or ID:")
found_person = university.find_person("John")
if found_person:
    print("Found:", found_person.name)
else:
    print("Person not found")
