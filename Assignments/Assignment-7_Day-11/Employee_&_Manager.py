class Employee:

    def __init__(self, name, emp_id, salary):
        self.name   = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f'Employee: {self.name} | ID: {self.emp_id} | Salary: ₹{self.salary}')

    def give_raise(self, amount):
        self.salary += amount
        print(f'Raise given. New salary: ₹{self.salary}')


class Manager(Employee):    # inherits from Employee

    def __init__(self, name, emp_id, salary, team_size, department):
        # call the parent __init__ using super()
        super().__init__(name, emp_id, salary)
        self.team_size  = team_size
        self.department = department
        self.team       = []    # list of Employee objects

    def add_to_team(self, employee):  # takes an Employee object
        self.team.append(employee)
        print(f'{employee.name} added to {self.name}\'s team')

    def display(self):   # OVERRIDE — add manager-specific info
        super().display()   # call parent's display first
        print(f'  Dept: {self.department} | Team size: {self.team_size}')

# Test:
e1 = Employee('Rahul',  'E001', 50000)
e2 = Employee('Anita',  'E002', 55000)
m1 = Manager('Ravi', 'M001', 120000, 5, 'Engineering')

e1.display()
m1.display()          # shows both employee + manager info
m1.give_raise(10000)  # inherited from Employee
m1.add_to_team(e1)
m1.add_to_team(e2)
