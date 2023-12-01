# Autor: José García
# Fecha: 14/12/2020
# Descripcion: Evaluar la positividad de una matriz Hermitica

from itertools import permutations
from sympy.combinatorics.permutations import Permutation
import lalgebra as al

# Definimos las matrices a evaluar

B = [[0.9,0,0,0.1],[0,0.35,-0.15,0],[0,-0.15,0.35,0],[0.1,0,0,0.9]]
Ro1 = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]

# Definimos las funciones a usar

def PosDef(A):
# Evalua la positividad definida de una matriz Hermitica, lo cual requiere que todos
# los determinantes de los leading principal minors sean mayores a cero.

    dim = len(A)                                                                # Dimension de la matriz
    cond = True                                                                 # Valor del condicional

    for i in range(1,dim+1):                                                    # Para cada dimension de los minors
        if al.Det(A,i) <= 0:                                                    # Si su determinante es menor o igual que cero
            cond = False                                                        # Cambiamos el valor del condicional
            break                                                               # Acabamos el ciclo

    return cond

def PosSemDef(A):
# Evalua la positividad semidefinida de una matriz Hermitica, lo cual requiere que todos
# los determinantes de los leading principal minors sean no negativos

    dim = len(A)                                                                # Dimension de la matriz
    cond = True                                                                 # Valor del condicional

    for i in range(1,dim+1):                                                    # Para cada dimension de los minors
        if al.Det(A,i) < 0:                                                     # Si su determinante es menor que cero
            cond = False                                                        # Cambiamos el valor del condicional
            break                                                               # Acabamos el ciclo

    return cond

# Imprimimos los resultados

lisB = [PosDef(B),PosSemDef(B)]
lisR = [PosDef(Ro1),PosSemDef(Ro1)]

print('¿Es la matriz A positiva definida?:',lisB[0])
print('¿Es la matriz A positiva semidefinida?:',lisB[1])
print('¿Es la matriz Ro1 positiva definida?:',lisR[0])
print('¿Es la matriz Ro1 positiva semidefinida?:',lisR[1])
