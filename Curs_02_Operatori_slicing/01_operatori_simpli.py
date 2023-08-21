# OPERATORI SIMPLI

# OPERATORI DE ASIGNARE - e semnul de egal "=" - se atribuie valori
a = 5

# OPERATORI DE ADUNARE : operator aritmetic si operator de string
a, b = "alpha", "beta"
c = a+b
print(c)

# +, -, *, /   - operatori aritmetici (adunare, scadere, inmultire, impartire)

# RIDICARE LA PUTERE  - de doua ori "**"
baza = 2
exponent = 4
x = baza**exponent
print(x)

# MODULO  - "%"  - echivalent cu restul impartirii: 10 (mod 3) = 1
# ne ajuta daca un numar este divizibil cu alt numar mai mic
numar = 10
modulo = 3
rest = numar % modulo
print(rest)

print("-"*30)

y = 20  # este divizibil cu 2?
print("verificam daca este divizibil cu 2: ", y %2)  # daca am "0" ca si output - este divizibil


# IMPARTIRE INTREAGA  - de cate ori intra deimpartitul la impartitor
z = 37
a = 5
print("verificam de cate ori a intra in z:", z // a)  # "cat-ul" fara rest

print("-"*40)

print(z//a, z%a)  # "cat-ul" este 7 , "rest" este 2


