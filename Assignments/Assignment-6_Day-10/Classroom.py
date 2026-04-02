class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def grade(self):
        if 90<=self.marks<=100:
            print("Grade : A")
        elif 75<=self.marks<=89:
            print("Grade : B")
        elif 60<=self.marks<=74:
            print("Grade : C")
        elif 45<=self.marks<=59:
            print("Grade : D")
        elif self.marks<=44:
            print("Grade : F")
        else:
            print("Invalid marks")


class Classroom:

    def __init__(self, subject, teacher):
        self.subject  = subject
        self.teacher  = teacher
        self.students = []

    def add_student(self, student):
        self.students = student

    def class_summary(self):
        # print subject, teacher, then each student's name and grade
        print(f"SUBJECT :{self.subject}")
        print(f"TEACHER : {self.teacher}")
        for st in python_class.students:
            print(st.name, st.grade())

# Test it:
s1 = Student('Rahul', 90)
s2 = Student('Anita', 72)
s3 = Student('John',  55)

python_class = Classroom('Python', 'Ravi Sir')
python_class.add_student(s1)
python_class.add_student(s2)
python_class.add_student(s3)
python_class.class_summary()
