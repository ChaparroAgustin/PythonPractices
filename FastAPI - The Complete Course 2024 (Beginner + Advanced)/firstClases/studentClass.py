class Student:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        Student.numberOfStudents += 1

    school = "online class"
    numberOfStudents = 0
    @classmethod
    def set_school(cls, newSchool):
        cls.school = newSchool


    def fullnameWithMajor(self):
        return(f'{self.first_name} {self.last_name} is going to {self.school}')
    
    def greeting (self):
        return f'Hello I am {self.first_name} {self.last_name}'

class collegeStudent (Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major