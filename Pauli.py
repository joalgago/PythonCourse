# Autor: José García
# Fecha: 11/12/2020
# Descripcion: Calculo de matrices con la base hecha con productos tensoriales de matrices de Pauli

# Importamos nuestro modulo de algebra lineal

import lalgebra as al

# Creamos el arreglo con las matrices de Pauli

Pauli =  [[[1,0],[0,1]],[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]]

# Declaramos las matrices de entrada y de salida:

Ro1 = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
Ro2 = [[0,0,0,0],[1,0,0,1],[-1,0,0,-1],[0,0,0,0]]

# Creamos la lista con los indices rij para cada matriz, asi como la lista con
# todos los productos tensoriales

R1 = []
R2 = []
Tens = []

# Inicializamos dichas listas con ceros, y hacemos los productos tensoriales

for i in range(len(Pauli)):
    R1.append([])
    for j in range(len(Pauli)):
        R1[i].append(0)

for i in range(len(Pauli)):
    R2.append([])
    for j in range(len(Pauli)):
        R2[i].append(0)

for i in range(len(Pauli)):
    Tens.append([])
    for j in range(len(Pauli)):
        k = al.kronecker(Pauli[i],Pauli[j])
        Tens[i].append(k)

# Calculamos los indices rij

for i in range(len(R1)):
    for j in range(len(R1[0])):
        mat = al.Conjugate(al.Transpose(Tens[i][j]))
        prod = al.matmul(mat,Ro1)
        R1[i][j] = al.Trace(prod)/2

for i in range(len(R2)):
    for j in range(len(R2[0])):
        mat = al.Conjugate(al.Transpose(Tens[i][j]))
        prod = al.matmul(mat,Ro2)
        R2[i][j] = al.Trace(prod)/2

# Imprimimos las componentes:

print('Componentes de Ro1 en la nueva base:')
print('')

for i in range(len(R1)):
    for j in range(len(R1[0])):
        if R1[i][j] != 0:
            print(str(R1[i][j]) + '\t' + 'en la componente:')
            al.printM(Tens[i][j])
            print('')

print('El resto de componentes son ceros')

print('')
print('')

print('Componentes de Ro2 en la nueva base:')
print('')

for i in range(len(R2)):
    for j in range(len(R2[0])):
        if R2[i][j] != 0:
            print(str(R2[i][j]) + '\t' + 'en la componente:')
            al.printM(Tens[i][j])
            print('')

print('El resto de componentes son ceros')
