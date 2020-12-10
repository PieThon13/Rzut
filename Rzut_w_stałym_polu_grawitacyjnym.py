import numpy as np
import matplotlib.pyplot as plt
def rzut1(h0,v0,a,theta):
    H=h0
    tc=(v0*np.sin((360-theta)*np.pi/180)-np.sqrt((v0**2*np.sin((360-theta)*np.pi/180)**2)+2*a*h0))/(-a)
    z=v0*np.cos((360-theta)*np.pi/180)*tc
    vx=v0*np.cos((360-theta)*np.pi/180)
    vy=-a*tc-v0*np.sin((360-theta)*np.pi/180)
    vk=np.sqrt(vx**2+vy**2)
    tt=np.linspace(0,tc,1000)
    yt=h0-v0*np.sin((360-theta)*np.pi/180)*tt-0.5*a*tt**2
    vt=np.sqrt((v0*np.cos((360-theta)*np.pi/180))**2+((-a*tt)-v0*np.sin((360-theta)*np.pi/180))**2)
    if theta!=270:
        x=np.linspace(0,z,1000)
        y=h0-np.tan((360-theta)*np.pi/180)*x-(a*x**2)/(2*v0**2*np.cos((360-theta)*np.pi/180)**2)
def rzut2(h0,v0,a,theta):
    H=h0+((v0**2)*(np.sin(theta*np.pi/180)**2))/(2*a)
    tc=(v0*np.sin(theta*np.pi/180)/a)+np.sqrt(2*H/a)
    z=v0*np.cos(theta*np.pi/180)*tc
    vx=v0*np.cos((theta)*np.pi/180)
    vy=v0*np.sin(theta*np.pi/180)-a*tc
    vk=np.sqrt(vx**2+vy**2)
    tt=np.linspace(0,tc,1000)
    yt=h0+v0*np.sin(theta*np.pi/180)*tt-0.5*a*tt**2
    vt=np.sqrt((v0*np.cos((theta)*np.pi/180))**2+(v0*np.sin(theta*np.pi/180)-a*tt)**2)
    if theta!=90 or v0!=0:
        x=np.linspace(0,z,1000)
        y=h0+np.tan(theta*np.pi/180)*x-(a*(x**2))/(2*(v0**2)*(np.cos(theta*np.pi/180)**2))
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
if v0==0 or (theta>=0 and theta<=90):
    rzut2(h0,v0,a,theta)
elif theta>=270 and theta<360:
    rzut1(h0,v0,a,theta)