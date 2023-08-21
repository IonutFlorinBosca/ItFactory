"""
BUCLA WHILE
-este iterator de control
-are nevoie de o conditie de start si una de finnish pentru a functiona
-daca nu are conditie de start bucla while nu porneste
-inainte de startul buclei while, trebuie sa definim o variabila de initializare
-trebuie sa aiba si o conditie de terminare
-fara conditiile de initializare si finish vom avea o bucla infinita
"""

i=0  #Initializare a variabilei
while i<10:  #Conditia de rulare a buclei
    print(i)
    i+=1    #Conditia de parcurgere (incrementare)

print("-"*40)

"""
# while true - daca nu stiu conditia trebuie sa ii pun break
x=10
while True:
    print(x)
    x -=1
    if x == -9:
        break
"""

#while merge si cu else
x=10
while x>2:
    print(x)
    x-=1
else:
    print('Sfarsit')


