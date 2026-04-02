class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Grade: {self.grade}")

s1 = Student('Rahul', 20, 'A')
s2 = Student('Anita', 22, 'B')
s3 = Student('John',  21, 'C')

s1.display()
s2.display()
s3.display()

# Expected output (example):
# Name: Rahul | Age: 20 | Grade: A
# Name: Anita | Age: 22 | Grade: B
# Name: John  | Age: 21 | Grade: C
