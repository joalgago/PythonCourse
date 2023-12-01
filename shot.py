# Autor: José García
# Fecha: 17/12/2020
# Descripcion: Análisis de un tiro penal

import numpy as np
import matplotlib.pyplot as plt

# Abrimos el archivo de texto

file = open('data.txt','r')

# Tomamos cada línea por separado

L = []

for line in file.readlines():
    L.append(line)

# Leemos las lineas y las almacenamos

T = []
Y = []
X = []

for line in L:
    T.append(float(line.split()[0]))
    X.append(float(line.split()[1]))
    Y.append(float(line.split()[2]))

# Cerramos el archivo

file.close()

# Convertimos las listas a arreglos de numpy para poder iterar sobre ellos en las graficas facilmente.

x = np.array(X)
y = np.array(Y)
t = np.array(T)

# A) Graficamos el movimiento de la pelota en una grafica x vs y

plt.plot(x,y,'k',label=r'$tray$')                                               # Creamos la grafica
plt.legend()                                                                    # Colocamos el label en la grafica
plt.xlabel(r'$x$')                                                              # Le ponemos nombre al eje x
plt.ylabel(r'$y$')                                                              # Le ponemos nombre al eje y
plt.show()                                                                      # Mostramos la grafica

# B) Ploteamos Y y X como funciones del tiempo

fig, ax = plt.subplots(2, gridspec_kw={'hspace': 0.05})

# Primer plot

ax[0].plot(t,x,)
ax.flat[0].set(ylabel= '$x [m]$')                                               # Ponerle label al eje y del primer plot

# Segundo plot

ax[1].plot(t,y,)
ax.flat[1].set(ylabel= '$y [m]$')                                               # Ponerle label al eje y del segundo plot

# Mostrar el resultado

plt.xlabel(r'$t [s]$')                                                          # Poner label al eje x
plt.show()

# C) El balon efectivamente golpea la porteria, pues en x=0 m, y=27.4 m, el cual esta dentro del rango dado.

# D) Ploteamos las velocidades promedio haciendo derivadas numericas.

dy = np.diff(y)                                                                 # Sacamos el diferencial de y
dx = np.diff(x)                                                                 # Sacamos el diferencial de x
dt = np.diff(t)[0]                                                              # Sacamos el diferencial de t, el cual por ser constante podemos usar solo el primero

vy = dy/dt                                                                      # Definimos la velocidad en y
vx = dx/dt                                                                      # Definimos la velocidad en x

fig, xa = plt.subplots(2, gridspec_kw={'hspace': 0.05})

# Primer plot

xa[0].plot(t[:-1],vx,)
xa.flat[0].set(ylabel= '$v_{x} [m/s]$')                                         # Ponerle label al eje y del primer plot

# Segundo plot

xa[1].plot(t[:-1],vy,)
xa.flat[1].set(ylabel= '$v_{y} [m/s]$')                                         # Ponerle label al eje y del segundo plot

# Mostrar el resultado

plt.xlabel(r'$t [s]$')                                                          # Poner label al eje x
plt.show()

# La velocidad en y es máxima (en valor absoluto) al final de la trayectoria (en y=27.4 m),
# y la velocidad en x (en valor absoluto) es máxima al inicio de la trayectoria (en x=11 m)

# E) Extraemos la velocidad inicial y la velocidad al final de la trayectoria (en x=0 m)

Vxi = vx[0]                                                                     # Comp. x de la velocidad inicial
Vyi = vy[0]                                                                     # Comp. y de la velocidad inicial

Vxf = float(vx[-1:])
Vyf = float(vy[-1:])

Vi = (Vxi**2 + Vyi**2)**(1/2)                                                   # Calculo de la velocidad inicial por medio de sus componentes
Vf = (Vxf**2 + Vyf**2)**(1/2)

print('Velocidades en m/s')
print('La velocidad inicial es aproximadamente:',Vi)
print('La velocidad final es aproximadamente:',Vf)

# F) Ploteamos las componentes de las aceleraciones promedio

dvx = np.diff(vx)
dvy = np.diff(vy)

ax = dvx/dt
ay = dvy/dt

fig, az = plt.subplots(2, gridspec_kw={'hspace': 0.05})

# Primer plot

az[0].plot(t[:-2],ax)
az.flat[0].set(ylabel= '$a_{x} [m/s^2]$')                                       # Ponerle label al eje y del primer plot

# Segundo plot

az[1].plot(t[:-2],ay)
az.flat[1].set(ylabel= '$a_{y} [m/s^2]$')                                       # Ponerle label al eje y del segundo plot

# Mostrar el resultado

plt.xlabel(r'$t [s]$')
plt.show()

# G) La aceleracion en x, al variar tan poco, puede ser causada por corrientes de aire que
# empujan al balon. La aceleracion en y, al ser negativa, se trata de la gravedad auxiliada por
# corrientes de aire que aceleran aún mas al balon.
