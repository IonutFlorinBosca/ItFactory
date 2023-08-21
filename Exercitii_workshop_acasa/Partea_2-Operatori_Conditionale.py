# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
#'Daca' verifica si valideaza o cerinta si in urma acesteia
#voi face o actiune daca e posibil, 'altfel' o voi lua pe alta ruta
#'Daca' afara ploua si lucrez ca si curier:
#daca ploua usor imi iau pelerina si fac o tura scurta
#altfel stau in casa!

# 2. Verifică și afișează dacă x este număr natural sau nu.
# x = 13
# if x >= 0:
#     print(f"Numarul {x} este natural!")
# else:
#     print(f"Numarul {x} nu este natural!")
s = "-"*40
# print(s)

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# if x == 0:
#     print(f"Numarul {x} este neutru!")
# elif x < 0:
#     print(f"Numarul {x} este negativ!")
# else:
#     print(f"Numarul {x} este pozitiv!")
# print(s)

# 4. Verifică și afișează dacă x este între -2 și 13.
# if x >= -2 and x <= 13:
#     print(f"Numarul {x} este intre -2 si 13")
# else:
#     print(f"Numarul {x} NU este intre -2 si 13")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x = 13
# y = 11
# diferenta = x - y
# if diferenta < 5:
#     print(f"Diferenta {diferenta} este mai mica decat 5")
# else:
#     print(f"Diferenta {diferenta} NU este mai mica decat 5")

# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# x = -22
# y = -22
# dif = x - y
# if not dif >= 5 and dif <= 27:
#     print(f"Diferenta {dif} NU este intre 5 si 27")
# else:
#     print(f"Diferenta {dif} este intre 5 si 27")
# print(s)

# 7.x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# if x == y:
#     print(f"{x} si {y} sunt egale!")
# elif x > y:
#     print(f"{x} este mai mare decat {y}")
# else:
#     print(f"{y} este mai mare decat {x}")

# 8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# x = 3
# y = 3
# z = 3
# if x == y == z:
#     print("Triunghi echilateral!")
# elif x == y or x == z or y == z:
#     print("Triughi isoscel!")
# else:
#     print("Triunghi oarecare!")

# 9. Citește o literă de la tastatură.
#     Verifică și afișează dacă este vocală sau nu.
# x = input("Tasteaza litera: ").lower()
# if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#     print("Ai tastat o vocala!")
# else:
#     print("Nu ai tastat o vocala!")

# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
# x = int(input("Ce nota ai luat? "))
# x = abs(x)
# if x <= 4 and x > 0:
#     print("F")
# elif x <= 6:
#     print("E")
# elif x <= 7:
#     print("D")
# elif x <= 8:
#     print("C")
# elif x <= 9:
#     print("B")
# elif x <= 10:
#     print("A")
# else:
#     print("Nota invalida!")

# 11.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = int(input("Tasteaza 4 cifre: "))
# if not len(str(x)) == 4:
#     print("Nu ai tastat 4 cifre!")
# else:
#     print("Bravo! Ai tastat 4 cifre!")
# print(s)

# 12.Verifică dacă x are exact 6 cifre.
# if len(str(x)) == 6:
#     print(f"{x} are 6 cifre!")
# print(s)

# 13.Verifică dacă x este număr par sau impar (x e int).
# par_sau_impar = x % 2
# print(par_sau_impar)
# if par_sau_impar == 0:
#     print(f"{x} este numar par!")
# else:
#     print(f"{x} este numar impar!")

# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?
# x, y, z = 15, 22, 40
# if x > y and x > z:
#     print(f"x este {x} si este cel mai mare!")
# elif y > z and y > x:
#     print(f"y este {y} si este cel mai mare!")
# else:
#     print(f"z este {z} si este cel mai mare!")

# 15. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
# x, y, z = 60, 60, 61
# if x == y == z:
#     print(f"Ai un triunghi echilateral valid!")
# else:
#     print("Triunghiul este invalid")

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
str = 'Coral is either the stupidest animal or the smartest rock'
# i = int(input("Tasteaza un numar: "))
# diff = len(str) - i
# print(str[:diff])

# 17. Același string. Declară un string nou care să
# fie format din primele 5 caractere + ultimele 5.
# str_nou = str[:5] + str[-5:]
# print(f"Noul string format din primele 5 si ultimele 5 char este: {str_nou}")

# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'
# index_rock = str.index('rock')
# print(f"Stringul pana la index este: {str[:index_rock]}")

# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
# import random
# numar_ghicit = int(input("Ghiceste un numar intre 1 si 6: "))
# print(numar_ghicit)
# dice_roll = random.randint(1, 6)
# print(f"After rolling the dice the number is: {dice_roll}")
# if numar_ghicit == dice_roll:
#     print(f"Ai ghicit. Felicitări! Ai ales {numar_ghicit} si zarul a fost {dice_roll}.")
# elif numar_ghicit > dice_roll:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
# else:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
#

# 20.  Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
# my_str = input("Tasteaza string: ")
# assert  my_str[0].lower() == my_str[-1].lower()

# 21. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)
str = '0123456789'
nr_pare = slice(0, 10, 2)
nr_impare = slice(1, 10, 2)
print(str[nr_pare])
print(str[nr_impare])

