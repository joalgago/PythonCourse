# Autor: José García
# Fecha: 9/12/2020
# Descripcion: Ejericio en clase, tiro parabolico

# Abrimos el archivo en modo leer

infile = open('balldat.txt','r')

# Almacenamos el valor de v0

V0 = float(infile.readline().split()[1])

# Leer el resto de lineas y almacenar los valores

L = []

for line in infile.readlines():
    L.append(line)

# Cerrar el archivo

infile.close()

# Almacenar los valores de t en una lista

T = []

for line in L[1:]:
    for t in line.split():
        T.append(float(t))

# Ordenar los valores de t de forma ascendente

T = sorted(T, key = float)

# Calcular los valores de y y almacenarlos

g = 9.8

Y = []

for t in T:
    y = V0*t - 0.5*g*(t**2)
    Y.append(y)

# Crear el archivo de texto y abrirlo

outfile = open('yvst.txt','w')

# Imprimir columnas

for i in range(len(T)):
    outfile.write('%.5f  %.5f' %(T[i] , Y[i]) + '\n')

# Cerrar el archivo

outfile.close()    
