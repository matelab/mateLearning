class Question:
    #Constructor
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questionPrompts = [
    "¿De que color son las manzanas?\n(a) Rojas/Verdes\n(b) Violetas\n(c) Naranjas\n\n",
    "¿De que color son las bananas?\n(a) Verde Azulado\n(b) Magenta\n(c) Amarillo\n\n",
    "¿De que color son las Frutillas?\n(a) Amarillo\n(b) Red\n(c) Azul\n\n"
    ]

questions = {
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b")
}
def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"Respuestas Correctas: {str(score)}  / Preguntas: {str(len(questions))}")


runTest(questions)