class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hi, I am {self.name}, I am {self.role}")

m = Person("Rahul", "Groom")
f = Person("Priya", "Bride")

m.introduce()
f.introduce()

class Marrige:
    relation = ["parents", "siblings", "cousins", "friends", "colleagues"]

    def __init__(self, f, m, budget):
        self.f = f
        self.m = m
        self.__budget = budget

    def show_budget(self, relation):
        if relation in Marrige.relation:
            print(f"Budget is {self.__budget}")
        else:
            print("You'r not Access the Budget")

m = Marrige(f, m, 100000)

m.show_budget("parents")
# relative = input("Enter your Relation:")
# m.show_budget(relative)
