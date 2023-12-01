# Autor: José García
# Fecha: 15/12/2020
# Descripcion: Multiples funciones con vectores de R^n

import lalgebra as al
from itertools import permutations
from sympy.combinatorics.permutations import Permutation

# Creamos las funciones a usar

def Base(A):
# Evalua si una lista de vectores es base del espacio R^n al que pertenecen.
# Los vectores deben darse como vectores fila.
    dim = len(A[0])                                                             # Saca la dimension del primer vector

    try:
        input = al.Transpose(A)                                                 # Convierte los vectores fila a vectores columna
        if al.Det(input,dim) != 0:                                              # Usa el criterio del determinante (si el determinante no es cero, los vectores son LI)
            print('Los vectores forman una base de R',dim)
        else:
            print('Los vectores no forman una base de R',dim)
    except:
        print('Los vectores no forman una base de R',dim)                       # Si algo falla es porque los vectores no son suficientes para ser una base, o hay vectores de mas

    return

def Prodint(v1,v2):
# Realiza el producto punto de dos vectores de igual dimension.
# Ej: v1 = [1,2,3], v2 = [1,2,3]; prod = 14
    prod = 0                                                                    # Inicializa le producto
    dim = len(v1)                                                               # Obtiene la dimension del producto
# Aplica el formulazo del producto punto
    for i in range(dim):
        prod += v1[i]*v2[i]

    return prod

def onBase(A):

    output = [al.Normalize(A[0])]

    for i in range(len(A)-1):
        res = [0 for k in range(len(A))]
        for j in range(i):
            res = al.SumVec(al.Vecxconst(output[j],Prodint(A[i+1],output[j])),res)
        v = al.ResVec(A[i+1],res)
        e = al.Normalize(v)
        output.append(e)

    return output

B = [[1,1],[0,1]]

test = onBase(B)

print(test)
