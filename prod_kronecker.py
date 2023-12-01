# Autor: José García
# Fecha: 6/12/2020
# Descripcion: Producto de Kronecker

# Inicializamos las matrices a operar

A = [[1,4,5,3],[7,10,22,7],[76,34,12,2]]

B = [[2,7],[6,10],[87,2],[1,7]]

# Creamos la matriz que tendra la salida

output = []

# Definimos la dimension de la matriz de salida

dim = [len(A)*len(B),len(A[1])*len(B[1])]

# Tomamos las variables que necesitamos:

p = len(B)

q = len(B[0])

# Creamos el ciclo que llenara a la matriz resultado con las filas necesarias:

for i in range(dim[0]):
    output.append([])
    for j in range(dim[1]):
        output[i].append(0)

# Llenamos la matriz resultado con los valores deseados:

for i in range(len(A)):
    for j in range(len(A[0])):
        for k in range(p):
            for l in range(q):
                output[p*(i)+k][q*(j)+l] = A[i][j]*B[k][l]

# Imprimimos la matriz resultado:

for row in output:
    print(row)
