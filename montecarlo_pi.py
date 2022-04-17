import random


print ("Script zur Berechnung von pi mit der Montecarlo-Methode")
print ("Bitte geben Sie die Anzahl der Iterationen ein:")
iterationen = int(input("Iterationen: "))
nummern = 0

for i in range(iterationen):
    x = random.random()
    y = random.random()
    if x*x+y*y < 1:
        nummern = nummern +1
print ("Pi ist ungefähr", 4*nummern/iterationen)