class Student:
    #Constructor
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def onHonorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


student1 = Student("Jim", "Business", 3.1)
student2 = Student("Pam", "Art", 3.8)


print(student2.onHonorRoll())