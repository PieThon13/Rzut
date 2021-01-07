import numpy as np
import matplotlib.pyplot as plt
from vpython import *
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
        yx=h0-np.tan((360-theta)*np.pi/180)*x-(a*x**2)/(2*v0**2*np.cos((360-theta)*np.pi/180)**2)
        fig, ax = plt.subplots(3, 1)
        fig.tight_layout(h_pad=3.5)
        plt.subplot(3, 1, 1)
        plt.plot(x, yx, 'm')
        plt.xlim(0, z)
        plt.ylim(0, H+0.5)
        plt.title('WYKRES y(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.annotate('MAXIMUM', xy=(0, H), xytext=(0.2, H + 1), arrowprops=dict(facecolor='black'))
        plt.subplot(3, 1, 2)
        plt.plot(tt, yt, 'c')
        plt.xlim(0, tc)
        plt.ylim(0, H+0.5)
        plt.title('WYKRES y(t)')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.grid(True)
        plt.subplot(3, 1, 3)
        plt.plot(tt, vt, 'g')
        plt.xlim(0, tc)
        plt.ylim(0, vk+0.5)
        plt.title('WYKRES v(t)')
        plt.xlabel('t')
        plt.ylabel('v')
        plt.grid(True)
        plt.savefig('WYKRES.jpg')
        plt.show

        def Reset(q):
            ball.make_trail = False
            ball.clear_trail()
            time = 0
            ball.pos = vector(0, h0, 0)
            ball.make_trail = True
            while time <= tc:
                sleep(0.05)
                ball.pos.x = vx * time
                ball.pos.y = h0 - v0 * np.sin((360 - theta) * np.pi / 180) * time - 0.5 * a * time ** 2
                time = time + dt

        scene = canvas(title='Symulacja rzutu', autoscale=True)
        button(bind=Reset, pos=scene.caption_anchor, text='Reset')
        ball = sphere(pos=vector(0, h0, 0), radius=1, color=color.magenta, make_trail=True, trail_color=color.white,
                      trail_radius=0.1)
        ground = box(pos=vector(0, 0, 0), length=3 * z, height=0.01, width=100, opacity=0.5, color=color.orange)
        time = 0
        dt = 0.05
        while time <= tc:
            sleep(0.05)
            ball.pos.x = vx * time
            ball.pos.y = h0 - v0 * np.sin((360 - theta) * np.pi / 180) * time - 0.5 * a * time ** 2
            time = time + dt
    else:
        fig, ax = plt.subplots(2, 1)
        fig.tight_layout(h_pad=4)
        plt.subplot(2, 1, 1)
        plt.plot(tt, yt, 'c')
        plt.xlim(0, tc)
        plt.ylim(0, H+0.5)
        plt.title('WYKRES y(t)')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.grid(True)
        plt.subplot(2, 1, 2)
        plt.plot(tt, vt, 'g')
        plt.xlim(0, tc)
        plt.ylim(0, vk+0.5)
        plt.title('WYKRES v(t)')
        plt.xlabel('t')
        plt.ylabel('v')
        plt.grid(True)
        plt.savefig('WYKRES.jpg')
        plt.show()

        def Reset(q):
            ball.make_trail = False
            ball.clear_trail()
            time = 0
            ball.pos = vector(0, h0, 0)
            ball.make_trail = True
            while time <= tc:
                sleep(0.05)
                ball.pos.y = h0 - v0 * np.sin((360 - theta) * np.pi / 180) * time - 0.5 * a * time ** 2
                time = time + dt

        scene = canvas(title='Symulacja rzutu', autoscale=True)
        button(bind=Reset, pos=scene.caption_anchor, text='Reset')
        ball = sphere(pos=vector(0, h0, 0), radius=1, color=color.magenta, make_trail=True, trail_color=color.white,
                      trail_radius=0.1)
        ground = box(pos=vector(0, 0, 0), length=100, height=0.01, width=100, opacity=0.5, color=color.orange)
        time = 0
        dt = 0.05
        while time <= tc:
            sleep(0.05)
            ball.pos.y = h0 - v0 * np.sin((360 - theta) * np.pi / 180) * time - 0.5 * a * time ** 2
            time = time + dt
    plik = open('Rzuty.txt', 'w')
    plik.write('Czas trwania ruchu wynosi: ' + str(tc) + '.\n')
    if theta!=270:
        plik.write('Zasięg ruchu: ' + str(z) + '.\n')
    plik.write('Wysokosc maksymalna: ' + str(H) + '.\n')
    plik.write('Prędkosc końcowa: ' + str(vk) + '.\n')
    plik.close()
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
    if theta!=90 and v0!=0:
        x=np.linspace(0,z,1000)
        yx=h0+np.tan(theta*np.pi/180)*x-(a*(x**2))/(2*(v0**2)*(np.cos(theta*np.pi/180)**2))
        xH = v0 ** 2 * np.cos(theta * np.pi / 180) * np.sin(theta * np.pi / 180) / a
        fig, ax = plt.subplots(3, 1)
        fig.tight_layout(h_pad=3)
        plt.subplot(3, 1, 1)
        plt.plot(x, yx, 'm')
        plt.xlim(0, z)
        plt.ylim(0, H + 0.5)
        plt.title('WYKRES y(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.annotate(f'MAXIMUM = ({xH:.3f},{H:.3f})', xy=(xH, H), xytext=(0.2, H + 1),
                     arrowprops=dict(facecolor='black'))
        plt.subplot(3, 1, 2)
        plt.plot(tt, yt, 'c')
        plt.xlim(0, tc)
        plt.ylim(0, H + 0.5)
        plt.title('WYKRES y(t)')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.grid(True)
        plt.subplot(3, 1, 3)
        plt.plot(tt, vt, 'g')
        plt.xlim(0, tc)
        plt.ylim(0, vk + 0.5)
        plt.title('WYKRES v(t)')
        plt.xlabel('t')
        plt.ylabel('v')
        plt.grid(True)
        plt.savefig('WYKRES.jpg')
        plt.show

        def Reset(q):
            ball.make_trail = False
            ball.clear_trail()
            time = 0
            ball.pos = vector(0, h0, 0)
            ball.make_trail = True
            while time <= tc:
                sleep(0.05)
                ball.pos.x = vx * time
                ball.pos.y = h0 + v0 * np.sin(theta * np.pi / 180) * time - 0.5 * a * time ** 2
                time = time + dt

        scene = canvas(title='Symulacja rzutu', autoscale=True)
        button(bind=Reset, pos=scene.caption_anchor, text='Reset')
        ball = sphere(pos=vector(0, h0, 0), radius=1, color=color.magenta, make_trail=True, trail_color=color.white,
                      trail_radius=0.1)
        ground = box(pos=vector(0, 0, 0), length=3 * z, height=0.01, width=100, opacity=0.5, color=color.orange)
        time = 0
        dt = 0.05
        while time <= tc:
            sleep(0.05)
            ball.pos.x = vx * time
            ball.pos.y = h0 + v0 * np.sin(theta * np.pi / 180) * time - 0.5 * a * time ** 2
            time = time + dt
    else:
        fig, ax = plt.subplots(2, 1)
        fig.tight_layout(h_pad=4)
        plt.subplot(2, 1, 1)
        plt.plot(tt, yt, 'c')
        plt.xlim(0, tc)
        plt.ylim(0, H+0.5)
        plt.title('WYKRES y(t)')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.grid(True)
        plt.subplot(2, 1, 2)
        plt.plot(tt, vt, 'g')
        plt.xlim(0, tc)
        plt.ylim(0, vk+0.5)
        plt.title('WYKRES v(t)')
        plt.xlabel('t')
        plt.ylabel('v')
        plt.grid(True)
        plt.savefig('WYKRES.jpg')
        plt.show()

        def Reset(q):
            ball.make_trail = False
            ball.clear_trail()
            time = 0
            ball.pos = vector(0, h0, 0)
            ball.make_trail = True
            while time <= tc:
                sleep(0.05)
                ball.pos.y = h0 + v0 * np.sin(theta * np.pi / 180) * time - 0.5 * a * time ** 2
                time = time + dt

        scene = canvas(title='Symulacja rzutu', autoscale=True)
        button(bind=Reset, pos=scene.caption_anchor, text='Reset')
        ball = sphere(pos=vector(0, h0, 0), radius=1, color=color.magenta, make_trail=True, trail_color=color.white,
                      trail_radius=0.1)
        ground = box(pos=vector(0, 0, 0), length=100, height=0.01, width=100, opacity=0.5, color=color.orange)
        time = 0
        dt = 0.05
        while time <= tc:
            sleep(0.05)
            ball.pos.y = h0 + v0 * np.sin(theta * np.pi / 180) * time - 0.5 * a * time ** 2
            time = time + dt
    plik = open('Rzuty.txt', 'w')
    plik.write('Czas trwania ruchu wynosi: ' + str(tc) + '.\n')
    if theta != 90 and v0!=0:
        plik.write('Zasięg ruchu: ' + str(z) + '.\n')
    plik.write('Wysokosc maksymalna: ' + str(H) + '.\n')
    plik.write('Prędkosc końcowa: ' + str(vk) + '.\n')
    plik.close()
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
    if theta>180 and theta<270:
        theta=90+theta
except:
    print('Wartość kąta nachylenia powinna być liczbą.')
if v0==0 or (theta>=0 and theta<=90):
    rzut2(h0,v0,a,theta)
elif theta>=270 and theta<360:
    rzut1(h0,v0,a,theta)
plik=open('Rzuty.txt','r')
print(plik.read())
plik.close()