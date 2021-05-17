# Funciones de clase. Funcionan dentro de la clase y las clases que la hereden.

class Student:
    # acá definimos el modelo de clase
    def __init__(self, name, age, major, avg_score, is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.avg_score = avg_score
        self.is_on_probation = is_on_probation
    # Creo una función de clase
    def on_honor_roll(self):
        if self.avg_score >= 8.5:
            return True
        else: 
            return False

student1 = Student("Phill", 19, "Programming", 5.5, False)
student2 = Student("Ann", 22, "Math", 8.9, False)

print(student1.on_honor_roll())
