#!/usr/bin/python
# coding: utf-8

from random import *

intentos = int(input("Ingrese cuantas veces lanzarás el dado: "))

ganancia = 0
for nlanzamiento in range(intentos):
    ndado = randint(1, 6)
    print("Salió: " + str(ndado))
    if ndado == 6:
        ganancia += 600
    elif ndado == 3:
        ganancia += 300
    elif ndado == 1:
        ganancia += 0
    else:
        ganancia -= 50
    
if (ganancia < 0):
    ganancia = 0

print("Ganó en total: " + str(ganancia))
