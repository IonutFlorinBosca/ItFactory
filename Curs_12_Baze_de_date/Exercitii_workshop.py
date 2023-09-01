f = open('Hello.txt', 'r')
text = f.read()
f.close()
print(text)

print("--" * 40)

list = ['\nGo', 'Kotlin', 'Swift']
with open('Hello.txt', 'a') as f:
    for l in list:
        f.write(l + '\n')

f = open('Hello.txt', 'r')
text = f.read()
f.close()
print(text)

print("--" * 40)

with open('Hello.txt', 'r') as f:
    lines = f.readlines()
    for index, l in enumerate(lines, start=1):
        if index % 2 == 1:
            print(l.strip())

print("--" * 40)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for index, element in enumerate(alphabet):
    with open(f"{element}.txt", 'w') as f:
        f.write(f"My name is letter {element}" + '\n')
        t = ""
        if index == 0 or index == 20:
            t = "'st"
        elif index == 1 or index == 21:
            t = "'nd"
        elif index == 2 or index == 22:
            t = "'rd"
        else:
            t = "'th"

        f.write(f"I am the {index + 1}{t} letter of the alphabet")

print("--" * 40)

import csv

with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    print(f"{header[0]:10}{header[1]:15}{header[2]:15}{header[3]:5}{header[4]:5}")
    for row in reader:
        print(f"{row[0]:5}{row[1]:15}{row[2]:15}{row[3]:5}{row[4]:10}")

print("--" * 40)

import pandas as pd

