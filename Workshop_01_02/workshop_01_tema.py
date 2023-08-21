"""
Partea 1 - Setup, Variabile, Tipuri de date

13. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.

"""

"""
#citeste string de la tastatura
stringul_meu = input("Scrie aici cuvantul sau combinatia de cuvinte: ")

#declara o variabila si stocheaza primul caracter din string
primul_caracter = stringul_meu[0]
print("Primul caracter este: " + primul_caracter)

#declara o variabila si stocheaza ultimul caracter din string
ultimul_caracter = stringul_meu[-1]
print("Ultimul caracter este: " + ultimul_caracter)

#declara o variabila si stocheaza majoritatea stringului
restul_stringului = stringul_meu[1: -1]
print("Majoritatea stringului este: " + restul_stringului)

#declara o lista noua si initializeaza fara nici o valoare
sir_nou = []
print("Values of sir_nou:", sir_nou)
print("Type of sir_nou:", type(sir_nou))
print("Size of sir_nou:", len(sir_nou))

#declara o variabila care va servi la parcurgerea stringului
#caracter cu caracter
counter = 0
print("Counter-ul initial are valoarea de: ", str(counter))

#declara o variabila care va stoca lungimea stringului fara
#primul si ultimul caracter
lungime_restul_stringului = len(restul_stringului)
print("Lungimea initiala a stringului fara primul si ultimul "
      "caracter este: ", str(lungime_restul_stringului))

print("-"*40)

#ma folosesc de lungimea stringului pentru a parcurge
#si a accesa fiecare caracter in parte
while lungime_restul_stringului > 0:
    #verific daca caracterul curent este identic cu primul caracter
    if restul_stringului[counter] == primul_caracter:
        print("Caracterul este identic si anume: " + restul_stringului[counter])
        sir_nou.append(restul_stringului[counter].upper())
        print("Noul sir are adaugat urmatorul caracter: " + str(sir_nou))
    else:
        print("Caracterul nu este identic si acesta este: " + restul_stringului[counter])
        sir_nou.append(restul_stringului[counter])
        print("Noul sir are adaugat urmatorul caracter: " + str(sir_nou))

    #dupa ce se incheie iteratia se incrementeaza counter-ul pentru
    #a accesa urmatorul caracter
    counter+= 1
    print("Counter-ul din loop este: " + str(counter))

    #in acelasi timp se decrementeaza numarul corespunzator
    #lungimii stringului din moment ce primul caracter a fost accesat
    lungime_restul_stringului-= 1
    print("Lungimea updatata a stringului este: " + str(lungime_restul_stringului))

#printam rezultatul
print("Noul string este " + primul_caracter + ''.join(sir_nou) + ultimul_caracter)
"""

"""
Partea 2 - Operatori, condiționale

9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu.

"""

"""
# declara o variabila care va stoca litera de la tastatura
let = input("Litera este: ")

# initializeaza o lista care sa contina doar vocale
lista_vocale = ["a", "ă", "î", "e", "o", "u", "i"]

# initializeaza o lista care sa contina doar consoane
lista_consoane = ["b", "c", "k", "d", "f", "g", "ğ", "g", "h", "j", "l",
                  "m", "n", "p", "r", "s", "ș", "t", "ț", "v", "z"]

# verifica daca litera este vocala din moment ce sunt mai putine
# vocale decat consoane
if let in lista_vocale:
    print("Litera aleasa este vocala!")
elif let in lista_consoane:
    print("Litera aleasa este consoana!")
else:
    print("Ce ai ales nu este o litera valida!")
"""

