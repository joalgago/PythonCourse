# Autor: José García
# Fecha: 6/12/2020
# Descripcion: Calcular el determinante de una matriz

# Importamos las funciones que vamos a utilizar

from itertools import permutations

from sympy.combinatorics.permutations import Permutation

# Inicializamos la matriz de la que queremos calcular el determinante

A = [[10,5,0],[2,9,-4],[0,-12,-7]]

# Tomamos la dimension de la matriz

dim = len(A)

# Creamos las permutaciones

perm = permutations(list(range(dim)))

# Almacenamos las permutaciones en una lista

perm_list = []

for i in list(perm):
    perm_list.append(list(i))                                                   # Convertimos las permutaciones en listas, pues las usaremos mas adelante como listas

# Calculamos los signos de las permutaciones

perm_sign = []                                                                  # Arreglo que almacenara los signos

for i in perm_list:
    a = Permutation(i)
    perm_sign.append(a.signature())

# Inicializamos el valor del determinante

det = 0

# Inicializamos el ciclo for que calculara el determinante

for i in range(len(perm_list)):                                                 # Los terminos en el determinante seran los mismos que el numero de permutaciones de los indicies
    k = 0                                                                       # Inicializamos un contador
    value = 1                                                                   # Inicializamos una variable para almacenar cada termino del determinante
    while k < dim:                                                              # Creamos un ciclo while que itere sobre las filas de la matriz A
        value *= A[k][perm_list[i][k]]                                          # Usando la definicion de los terminos del determinante, multiplicamos los sub-terminos uno a uno
        k += 1                                                                  # Aumentamos el contador en uno
    det += value*perm_sign[i]                                                   # Multiplicamos el termino obtenido por su signo y lo sumamos al determinante, reiniciando el proceso para cada termino

# Imprimimos el resultado

print('El determinante de la matriz es:', det)
