# Juego de adivinar básico
# Vamos a guardar una palabra secreta y usuarix tiene que adivinar la palabra
# Hay un límite de 3 intentos antes de que el juego termine

secret_word = "girafa"
guess = ""
guess_count = 1
guess_limit = 3
out_of_guesses = False

guess = input("Intenta adivinar la palabra secreta. Tenés " + str(guess_limit) + " oportunidades. \n")

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Intenta de nuevo :) \n")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("Ganaste!")
elif out_of_guesses:
    print("Perdiste. Te quedaste sin oportunidades.")
