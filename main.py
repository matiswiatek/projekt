from gettext import install
import subprocess
import sys
from operator import index
from time import perf_counter
from turtledemo.sorting_animate import ssort

import pylab
from matplotlib.pyplot import plot_date, xlabel
from sympy.physics.control.control_plots import matplotlib


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import matplotlib.pyplot as plt
except ImportError:
    install("matplotlib")
    import matplotlib.pyplot as plt
try:
    with open('C:\\Users\\Mati\\Documents\\GitHub\\projekt\\punkty.txt', 'r') as file:
        dane = file.read()
except FileNotFoundError:
    print('nie znaleziony')
#
#poczatek
#
print(dane)
print(type(dane))
dane = list(dane.split('\n'))
# posplitowane na punkty x,y
print(type(dane))
print(dane)
danebezd = list(set(dane))
print(danebezd)
danebezd = list(danebezd)
print(type(danebezd))
danepolistowaned = []
for i in danebezd:
    i = i.split(';')
    danepolistowaned.append(i)
    print(i)
print('\n' , list(danepolistowaned))
# w tym momencie dane sa podzielone w liscie na listy (x,y) bez duplikatow ale nie posortowane
print(type(danepolistowaned[0][0]))
danepolistowaned.sort(key=lambda x: x[0])
print(danepolistowaned)
pom1 = []
pom2 = []
liczbaokr = 1
for i in danepolistowaned:
    for j in i :
        liczbaokr = liczbaokr + 1
        if liczbaokr % 2 == 0:
            j = float(j)
            pom1.append(j)
        else:
            j = float(j)
            pom2.append(j)
print(pom1,pom2)
#rozdzielone x i y aby moc posortowac po zmiennej x
def synchro_sort(pom1,pom2):

    indeksy = sorted(range(len(pom1)), key=lambda k: pom1[k])

    pom2[:] = [pom2[i] for i in indeksy]
synchro_sort(pom1,pom2)
pom1.sort()
print(pom1,pom2)
x = pom1
y = pom2
#rozdzielone na x,y i posortowane posłużą do wykonania wykresu
legenda = []
for i,j in zip(x,y):
    print(i,j)
    legenda.append([i,j])
print(legenda)
print(x,y)
#tworzenie wykresu
plt.scatter(x,y,)
plt.legend([legenda])
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(range(-2,10))
plt.yticks(range(-2,10))
plt.title('Punkty')
plt.grid(True)
plt.axis(((-2),10.5,(-2),10.5))
plt.ioff()
plt.show()
