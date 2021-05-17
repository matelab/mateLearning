# Juego de preguntas
# Se mantiene el puntaje
# Vamos a usar clases, if y otras cosas

question_prompt = [
    "¿De que color son las manzanas?\n(a) Rojas/Verdes\n(b) Violetas\n(c) Naranjas\n\n",
    "¿De que color son las babnanas?\n(a) Azules\n(b) Amarillas\n(c) Dinosaurio\n\n",
    "¿Quien se ha tomado todo el vino?\n(a) Rodrigo\n(b) La mona\n(c) Oh oh oh oh oh oh\n\n"
]
 
class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = {
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")
}

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Conseguiste " + str(score) + "/" + str(len(questions)) + " respuestas correctas.")

run_test(questions)
        