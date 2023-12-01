# Autor: José García
# Fecha: 9/12/2020
# Descripcion: Aplicar el reshuffle a una matriz de nxn, con n una potencia de 4

from math import sqrt

# Creamos la matriz a modificar

list = [1,2,3,4]

A = []

for i in range(len(list)):
    A.append([])
    for j in range(len(list)):
        if i == j:
            A[i].append(list[i])
        else:
            A[i].append(0)

dim = len(A)
sep = int(sqrt(dim))

# Separamos la matriz en los elementos que moveremos de lugar

mat_sum = []                                                                    # Lista que almacenara los elementos en una sola lista

for i in range(dim):
    mat_sum += A[i]

mat_inter1 = []                                                                 # Lista que almacena los bloques que se van a mover

i = 0                                                                           # Iniciamos el iterador
while i <= dim*(dim)-sep:                                                       # Ponemos como limite el inicio de la ultima fila de la matriz
    mat_inter1.append(mat_sum[i:i + sep])                                       # Agregamos la sublista deseada
    i += sep                                                                    # Pasamos a la siguiente sublista

mat_inter2 = []                                                                 # Lista que almacena los bloques antes encontrados, por filas

k = 0                                                                           # Iniciamos el iterador
for j in range(dim):
    mat_inter2.append(0)                                                        # Creamos una posicion en la lista
    mat_inter2[j] = mat_inter1[k:k + sep]                                       # Agregamos la sublista deseada
    k += sep                                                                    # Pasamos a la siguiente sublista

# Movemos los elementos de lugar (usando el codigo propuesto como ayuda)

mat_inter3 = []                                                                 # Ultima matriz intermedia

size = len(mat_inter2)
dim = int(sqrt(size))

for j in range(dim):
    mat_inter3.append([])
    for submatrix in mat_inter2:
        for elem in submatrix[j]:
            mat_inter3[j].append(elem)

AR = []                                                                         # Matriz resultado

i = 0
for index in range(size):
    AR.append([])
    for elem in range(size):
        AR[i].append(mat_inter3[index % dim][0])
        mat_inter3[index%dim].pop(0)
    i += 1

# Imprimimos los resultados

print('Matriz original:')

for row in A:
    print(row)

print('')

print('Matriz resultante:')

for row in AR:
    print(row)
