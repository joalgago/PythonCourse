# Ejercicio 2.6
# Autor: José García
# Fecha: 2/12/2020
# Descripcion: Calculo de energia para un atomo de hidrogeno con un electron

# Inciso a

# Definir las constantes del problema

h = 6.6261*(10**-34)                                                            # Constante de Planck
q = 1.6022*(10**-19)                                                            # Carga del electron
m = 9.1094*(10**-31)                                                            # Masa del electron
e = 8.8542*(10**-12)                                                            # Permitividad del vacio

# Definir la lista donde seran ingresados los valores

E = []

# Definir la variable que almacenara el nivel de energia correspondiente

En = 0

# Hacer el calculo de los niveles de energia

for n in range(1,21):
    En = -((m*(q**4))/(8*((e*h)**2)))*(1/(n**2))                                # Hace el calculo del nivel de energia
    E.append(En)                                                                # Lo agrega a la posicion que le corresponde en el arreglo de los niveles de energia

# Imprimir el resultado

print('Niveles de energia para el atomo de Hidrogeno con un electron (En Joules):')
print('')
for n in range(1,21):
    print('Nivel n=' + str(n) + ':' + str(E[n-1]))
    print('')

# Inciso b

# Generar la lista que contendra todas las diferencias de energia

ER = []

for i in range(5):
    ER.append([])                                                               # Genera las sublistas de la lista
    for j in range(5):
        ER[i].append(0)                                                         # Llena dichas sublistas con ceros

# Llena dicha lista con las diferencias deseadas

for f in range(5):
    for i in range(5):
        ER[f][i] = E[i] - E[f]                                                  # Realiza la resta y la almacena en la matriz

# Imprimir los resultados

print('Energia liberada al saltar de nivel (En Joules):')
print('')

for level in ER:
    print(level)
    print('')
