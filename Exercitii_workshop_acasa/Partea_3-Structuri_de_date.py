# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# Afișeaz-o.
print(note_muzicale)
# Inversează ordinea folosind slicing și suprascrie această listă.
note_muzicale = note_muzicale[::-1]
# Printează varianta actuală (inversată).
print(note_muzicale)
# Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
note_muzicale.reverse()
# Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
print(note_muzicale)
print('-'*40)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))
print('-'*40)

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.
#Varianta 1
l3 = l1 + l2
print(l3)
#Varianta 2
l4 = l1.copy()
l4.extend(l2)
print(l4)
print('-'*40)

# 4.Sortează și afișează lista generată la exercițiul anterior.
l4.sort()
print(l4)
print('-'*40)
# Șterge numărul 0 folosind o funcție.
l4.remove(0)
# Afișaza iar lista.
print(l4)
print('-'*40)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.
if len(l4) != 0:
    print("Lista nu este goală.")
else:
    print("Lista este goală.")
print('-'*40)

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
l4.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if len(l4) != 0:
    print("Lista nu este goală.")
else:
    print("Lista este goală.")
print('-'*40)

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for elev in dict1.keys():
    print(elev)
print('-'*40)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
for e in dict1:
    print(f"{e} a luat nota {dict1[e]}")
print('-'*40)

# 10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
dict1['Dorel'] = 6
# Printează nota după modificare
print(dict1)
print('-'*40)

# 11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
dict1.pop('Gigel')
print(dict1)
# Vine un coleg nou. Adaugă Ionică, cu nota 9
dict1['Ionica'] = 9
# Printează noii elevi
print(dict1)
print('-'*40)

# 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# Declară o Listă cu 5 jucători
lj = ['j1', 'j2', 'j3', 'j4', 'j5']
# Schimbari_efectuate = te joci tu cu valori diferite
schimbari_efectuate = 0
# Schimbari_max = 3
schimbari_max = 3
#
jnou = 'j8'
jteren = 'j5'
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
if lj.count(jteren) and schimbari_max != 0:
    # Efectuează schimbarea
    # Șterge jucătorul scos din listă
    # Adaugă jucătorul intrat
    lj[lj.index(jteren)] = jnou
    schimbari_efectuate +=1
    schimbari_max -= 1
    # Afișază a intrat x, a ieșit y, mai ai z schimbări
    print(f"A intrat {jnou}, a iesit {jteren}, mai ai {schimbari_max} schimbari!")
    print(lj)
#
# Dacă jucătorul nu e în teren:
elif lj.count(jteren) == False:
    print(f"Nu se poate deoarece juc {jteren} nu e in teren!")
    print(f"Mai ai {schimbari_max} schimbari!")
# Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# Afișază ‘mai ai z schimbări’
print("-"*40)
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item is în list python”

#Acelasi script din nou
jnou = 'j9'
jteren = 'j2'
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
if lj.count(jteren) and schimbari_max != 0:
    # Efectuează schimbarea
    # Șterge jucătorul scos din listă
    # Adaugă jucătorul intrat
    lj[lj.index(jteren)] = jnou
    schimbari_efectuate +=1
    schimbari_max -= 1
    # Afișază a intrat x, a ieșit y, mai ai z schimbări
    print(f"A intrat {jnou}, a iesit {jteren}, mai ai {schimbari_max} schimbari!")
    print(lj)
#
# Dacă jucătorul nu e în teren:
elif lj.count(jteren) == False:
    print(f"Nu se poate deoarece juc {jteren} nu e in teren!")
    print(f"Mai ai {schimbari_max} schimbari!")
print("-"*40)

#Acelasi script
jnou = 'j10'
jteren = 'j7'
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
if lj.count(jteren) and schimbari_max != 0:
    # Efectuează schimbarea
    # Șterge jucătorul scos din listă
    # Adaugă jucătorul intrat
    lj[lj.index(jteren)] = jnou
    schimbari_efectuate +=1
    schimbari_max -= 1
    # Afișază a intrat x, a ieșit y, mai ai z schimbări
    print(f"A intrat {jnou}, a iesit {jteren}, mai ai {schimbari_max} schimbari!")
    print(lj)
#
# Dacă jucătorul nu e în teren:
elif lj.count(jteren) == False:
    print(f"Nu se poate deoarece juc {jteren} nu e in teren!")
    print(f"Mai ai {schimbari_max} schimbari!")
print("-"*40)

# 13.Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
zile_sapt.add('luni')
# Afișează zile_sapt
print(zile_sapt)
print("-"*40)

# 14.Folosește un if și verifică dacă:
if zile_sapt.issubset(weekend):
    print("Weekend este un subset al zilelor din săptămânii.")
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")
print("-"*40)

# 15. Afișează diferențele dintre aceste 2 seturi.
# diferenta = zile_sapt - weekend
print(zile_sapt.difference(weekend))
print("-"*40)

# 16. Afișează intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))