import numpy as np
import matplotlib.pyplot as plt

try:
    h0=float(input('Z jakiej wysokości wyrzucono ciało? '))
    while h0<0:
        h0=float(input('Wysokość początkowa nie może być mniejsza od zera. Spróbuj jeszcze raz: '))
except:
    print('Wysokość początkowa powinna być wartością liczbową większą lub równą zero.')
try:
    v0=float(input('Jaka jest wartość prędkości początkowej? '))
    while v0<0:
        v0=float(input('Szybkość początkowa nie może być mniejsza od zera. Spróbuj ponownie: '))
except:
    print('Szybkość początkowa musi być liczbą.')
try:
    a=float(input('Ile wynosi wartość przyśpieszenia grawitacyjnego? '))
    while a<=0:
        a=float(input('Przyspieszenie grawitacyjne na dowolnej planecie jest większe od zera. Spróbuj jeszcze raz: '))
except:
    print('Wartość przyspieszenia grawitacyjnego jest liczbą. ')
try:
    theta=float(input('Pod jakim kątem wyrzucono ciało? (Wartość kąta podaj w stopniach) '))
    while theta>360:
        theta=theta-360
    while theta<0:
        theta=theta+360
    if theta>90 and theta<=180:
        theta=180-theta
    if theta>180 and theta<=270:
        theta=90+theta
except:
    print('Wartość kąta nachylenia powinna być liczbą.')
