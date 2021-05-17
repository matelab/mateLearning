# Con clases y objetos podemos crear los tipos de datos o conjuntos de 
# distintas características

# Ejemplo: Vamos a modelar un estudiante

class Student:
    # acá definimos el modelo de clase
    def __init__(self, name, age, major, avg_score, is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.avg_score = avg_score
        self.is_on_probation = is_on_probation
    
    # creamos una instancia de objeto

student1 = Student("Phill", 19, "Programming", 8.5, False)
student2 = Student("Donnie", 21, "Music", 7.9, False)

print(student1.name)


