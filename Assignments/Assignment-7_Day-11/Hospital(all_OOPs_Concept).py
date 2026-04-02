class Person:
    def introduce(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    
class Patient(Person):
    def get_record(authorised_by):
        pass