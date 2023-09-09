"""
Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`.
Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
"""

import string


# am importat libraria string, si voi folosi metoda string.ascii_uppercase
# pentru a stoca intr-o variabila toate caracterele alfabetului
# creez o functie care ia 1 parametru, si anume numarul fisierelor care vor fi create
def generate_text_files(numar_fisiere):
    # generez si stochez intr-o variabila caracterele alfabetului
    alphabet = string.ascii_uppercase

    # voi folosi un for loop si range;
    # pentru fiecare iterare, voi crea un nou fisier care va contine textul
    # corespunzator, si ma voi folosi de index de asemenea
    for index in range(numar_fisiere):
        print(f"Indexul curent este: {index}")
        # pentru ca denumirea fisierului o va da litera din alfabet,
        # voi stoca litera intr-o variabila ca sa fie mai clar
        litera_curenta = alphabet[index]
        print(f"Litera curenta este: {litera_curenta}")
        # o sa folosesc conditionale pentru a da sufixul cifrelor si voi
        # stoca rezultatul in variabila suffix
        suffix = ""
        if index + 1 == 1:
            suffix = "st"
        elif index + 1 == 2:
            suffix = "nd"
        elif index + 1 == 3:
            suffix = "rd"
        elif index + 1 == 21:
            suffix = "st"
        else:
            suffix = "th"
        with open(f"{litera_curenta}.txt", "w") as file:
            # acum va trebui sa scriu :
            # My name is letter X.
            # I am the 24th letter of the alphabet.
            file.writelines([f"My name is letter {litera_curenta}\n",
                             f"I am the {index + 1}{suffix} letter of the alphabet\n"])

generate_text_files(24)