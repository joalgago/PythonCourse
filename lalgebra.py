# Autor: José García
# Fecha: 11/12/2020
# Descripcion: Funciones de algebra lineal

from itertools import permutations
from sympy.combinatorics.permutations import Permutation

def DiagMat(input):
# Hace una matriz diagonal con los indices indicados en la entrada
# Ej: input: [1,2,3] , output: [[1,0,0],[0,2,0],[0,0,3]]
   output = []

   for i in range(len(input)):
     output.append([])                                                          # Agregar lista vacia a la salida
     for j in range(len(input)):
       if i == j:                                                               # Cuando los indices son iguales
         output[i].append(input[i])                                             # Agregar un elemento de la lista de indices
       else:
         output[i].append(0)                                                    # Agregar un cero en cualquier otra ocasion

   return output

def Matrix(indices,elements,rows,columns):
# Hace una matriz de la dimension dada por el usuario, ingresando los elementos dados en las
# posiciones indicadas, pero las posiciones deben colocarse de izquierda a derecha y de arriba
# a abajo, y en orden con los elementos.
   numElem = len(indices)                                                       # numero de elementos

   output = []                                                                  # inicializacion de la matriz

   k = 0                                                                        # iniciacion del iterador
   for i in range(rows):
     output.append([])
     for j in range(columns):
       if (i == indices[k][0] and j == indices[k][1]):                          # cuando los indices de la entrada y de la matriz coinciden
         output[i].append(elements[k])                                          # agrega elemento
         k += 1
       else:
         output[i].append(0)                                                    # de lo contrario agrega un cero

   return output

def VecNorm(input):
# Calcula la norma de un vector dado
   sqNorm = 0                                                                   # inicializacion de la norma al cuadrado
   for elem in input:
     sqNorm += elem**2

   norm = sqNorm**(1/2)                                                         # tomar la raiz cuadrada de la norma al cuadrado

   return norm

def Normalize(input):
# Normaliza un vector
   norm = VecNorm(input)
   for index in range(len(input)):
     input[index] = input[index]/norm

   return input

def Vecxconst(v,c):
# Multiplica un vector por una constante

    for i in range(len(v)):
        v[i] = (v[i]*c)

    return v

def ResVec(v1,v2):
# Resta dos vectores de la forma v1-v2
    output = []

    for i in range(len(v1)):
        output.append(0)
        output[i] = v1[i] - v2[i]

    return output

def SumVec(v1,v2):
# Suma dos vectores
    output = []

    for i in range(len(v1)):
        output.append(0)
        output[i] = v1[i] + v2[i]

    return output

def Transpose(input):
# Hace la transpuesta de una matriz intercambiando las filas y las columnas.
# Ej: input = [[1,2],[3,4]]; output = [[1,3],[2,4]]
   dim = len(input)                                                             # dimension de la matriz

   output = []                                                                  # inicializacion de la transpuesta

# Crea una matriz de dimension dimxdim con ceros en todas las posiciones
   for row in range(dim):
     output.append([])
     for column in range(dim):
       output[row].append(0)

# Crea la transpuesta intercambiando filas y columnas
   for row in range(dim):
     for column in range(dim):
       output[row][column] = input[column][row]

   return output

def Conjugate(input):
# Devuelve la conjugada de una matriz.
# Ej: input = [[j,2],[1-j,3]]; output = [[-j,2],[1+j,3]]
   dim = len(input)                                                             # Dimension de la matriz

   output = []                                                                  # Inicializacion de la matriz conjugada

# Crea una matriz de dimension dimxdim con ceros en todas sus posiciones
   for row in range(dim):
     output.append([])
     for column in range(dim):
       output[row].append(0)

# CaLcula el conjugado de cada posicion
   for row in range(dim):
     for column in range(dim):
       output[row][column] = input[row][column].conjugate()

   return output

def Trace(input):
# Calcula la traza de una matriz
# Ej: input = [[1,2],[3,4]]; Tr = 5
   dim = len(input)                                                             # dimension de la matriz

   Tr = 0                                                                       # inicializa la variable de la traza

# Suma todos los elementos de la diagonal
   for i in range(dim):
     Tr += input[i][i]

   return Tr

def matmul(A, B):
# Multiplicación de matrices:
# Implementación de la multiplicación de dos matrices A y B de dimensiones
# mxn y nxp, respectivamente, utilizando la fórmula
# c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}. Devuelve A.B.
# Ej: matmul([[0, -1j],[1j, 0]], [[0, 1],[1, 0]]) = [[-1j, 0j],[0j, 1j]]

  #   1. Inicializar una matriz de (m)x(p) con ceros en todas sus entradas
   m = len(A)
   n = len(A[0])
   p = len(B)

   output = []
   for row in range(m):
       output.append([])
       for column in range(p):
           output[row].append(0)

  #   2. Aplicar el formulazo de multiplicación de matrices para calcular
  #      cada elemento de matriz
   for i in range(m):
       for j in range(p):
           for k in range(n):
               output[i][j] += A[i][k]*B[k][j]

   return output

def printM(matrix):
# Imprimir matrices:
# Imprime una lista de listas en forma de matriz.
# Ej: - printM([[1,0],[0,1]) = [1,0]
#                              [0,1]

# Imprimir fila por fila
   for row in matrix:
        print(row)

   return

def kronecker(A,B):
# Producto de Kronecker:
# Implementación del producto de Kronecker de dos matrices A y B de
# dimensiones mxn y pxq, respectivamete, utlizando la fórmula
# c_{p(i-1)+k, q(j-1)+l}=a_{ij}b_{kl}. Devuelve A tensor B.
# Ej: - kronecker([[1, 0],[0, 1]], [[0, 1],[1, 0]]) = [[0, 1, 0, 0],[1, 0, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0]]

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

   return output

def Det(A,dim):
# Calcula el determinante de una matriz, o de una submatriz de la dimension
# especificada. dim no puede ser mayor que la dimension de la matriz.
# Es necesario importar primero estas funciones:

# Creamos las permutaciones
   perm = permutations(list(range(dim)))

# Almacenamos las permutaciones en una lista
   perm_list = []
   for i in list(perm):
       perm_list.append(list(i))                                                # Convertimos las permutaciones en listas, pues las usaremos mas adelante como listas

# Calculamos los signos de las permutaciones
   perm_sign = []                                                               # Arreglo que almacenara los signos
   for i in perm_list:
       a = Permutation(i)
       perm_sign.append(a.signature())

# Inicializamos el valor del determinante
   det = 0

# Inicializamos el ciclo for que calculara el determinante
   for i in range(len(perm_list)):                                              # Los terminos en el determinante seran los mismos que el numero de permutaciones de los indicies
       k = 0                                                                    # Inicializamos un contador
       value = 1                                                                # Inicializamos una variable para almacenar cada termino del determinante
       while k < dim:                                                           # Creamos un ciclo while que itere sobre las filas de la matriz A
           value *= A[k][perm_list[i][k]]                                       # Usando la definicion de los terminos del determinante, multiplicamos los sub-terminos uno a uno
           k += 1                                                               # Aumentamos el contador en uno
       det += value*perm_sign[i]                                                # Multiplicamos el termino obtenido por su signo y lo sumamos al determinante, reiniciando el proceso para cada termino

   return det

def reshuffle(A):
# Aplica el reshuffle a matrices de nxn, donde n es una potencia de 4.
# Es necesario importar la siguiente funcion:
# from math import sqrt

   dim = len(A)
   sep = int(sqrt(dim))

# Separamos la matriz en los elementos que moveremos de lugar
   mat_sum = []                                                                 # Lista que almacenara los elementos en una sola lista
   for i in range(dim):
       mat_sum += A[i]

   mat_inter1 = []                                                              # Lista que almacena los bloques que se van a mover
   i = 0                                                                        # Iniciamos el iterador
   while i <= dim*(dim)-sep:                                                    # Ponemos como limite el inicio de la ultima fila de la matriz
       mat_inter1.append(mat_sum[i:i + sep])                                    # Agregamos la sublista deseada
       i += sep                                                                 # Pasamos a la siguiente sublista

   mat_inter2 = []                                                              # Lista que almacena los bloques antes encontrados, por filas
   k = 0                                                                        # Iniciamos el iterador
   for j in range(dim):
       mat_inter2.append(0)                                                     # Creamos una posicion en la lista
       mat_inter2[j] = mat_inter1[k:k + sep]                                    # Agregamos la sublista deseada
       k += sep                                                                 # Pasamos a la siguiente sublista

# Movemos los elementos de lugar (usando el codigo propuesto como ayuda)
   mat_inter3 = []                                                              # Ultima matriz intermedia
   size = len(mat_inter2)
   dim = int(sqrt(size))

   for j in range(dim):
       mat_inter3.append([])
       for submatrix in mat_inter2:
           for elem in submatrix[j]:
               mat_inter3[j].append(elem)

   AR = []                                                                      # Matriz resultado
   i = 0
   for index in range(size):
       AR.append([])
       for elem in range(size):
           AR[i].append(mat_inter3[index % dim][0])
           mat_inter3[index%dim].pop(0)
       i += 1

   return AR

def Matxconst(c,A):
# Multiplica una matriz por una constante
# Ej: A = [[1,2],[3,4]], c = 2; output = [[2,4],[6,8]]
# Obtenemos las dimensiones de la matriz:

   rows = len(A)
   columns = len(A[0])

   output = []                                                                  # Iniciamos la salida

# Llenamos la salida de ceros

   for i in range(rows):
       output.append([])
       for j in range(columns):
           output[i].append(0)

# Multiplicamos cada elemento por la constante

   for i in range(rows):
       for j in range(columns):
           output[i][j] = c*A[i][j]

   return output

def MatSum(A,B):
# Suma de dos matrices de igual dimension
# Ej: A = [[1,2],[3,4]], B = [[1,1],[1,1]]; output = [[2,3],[4,5]]
    rows = len(A)                                                               # Numero de filas
    columns = len(A[0])                                                         # Numero de columnas

# Declaramos la salida
    output = []

# Llenamos la salida de ceros
    for i in range(rows):
        output.append([])
        for j in range(columns):
            output[i].append(0)

# Realizamos la suma de matrices
    for i in range(rows):
        for j in range(columns):
            output[i][j] = A[i][j] + B[i][j]

    return output

def PosDef(A):
# Evalua la positividad definida de una matriz Hermitica, lo cual requiere que todos
# los determinantes de los leading principal minors sean mayores a cero.

    dim = len(A)                                                                # Dimension de la matriz
    cond = True                                                                 # Valor del condicional

    for i in range(1,dim+1):                                                    # Para cada dimension de los minors
        if Det(A,i) <= 0:                                                       # Si su determinante es menor o igual que cero
            cond = False                                                        # Cambiamos el valor del condicional
            break                                                               # Acabamos el ciclo

    return cond

def PosSemDef(A):
# Evalua la positividad semidefinida de una matriz Hermitica, lo cual requiere que todos
# los determinantes de los leading principal minors sean no negativos

    dim = len(A)                                                                # Dimension de la matriz
    cond = True                                                                 # Valor del condicional

    for i in range(1,dim+1):                                                    # Para cada dimension de los minors
        if Det(A,i) < 0:                                                        # Si su determinante es menor que cero
            cond = False                                                        # Cambiamos el valor del condicional
            break                                                               # Acabamos el ciclo

    return cond
