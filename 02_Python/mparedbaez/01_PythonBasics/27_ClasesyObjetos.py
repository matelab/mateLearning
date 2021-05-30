
class Student:
    #Constructor
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation


student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.name)
print(student1.gpa)

print(student2.name)
print(student2.gpa)