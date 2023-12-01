# Ejercicio 2.16
# Autor: José García
# Fecha: 3/12/2020
# Descripcion: Tabla de valores de grados Celsius y Farenheit

# Declaramos las variables que vamos a usar:

F = 0                                                                           # Valor inicial de grados Farenheit
dF = 10                                                                         # Salto entre valores
C = 0                                                                           # Valor inicial grados Celsius
C_approx = 0                                                                    # Valor inicial aproximacion grados Celsius
LF = []                                                                         # Lista de grados Farenheit
LC = []                                                                         # Lista de grados Celsius
LCA = []                                                                        # Lista de grados Celsius aproximados
conversion = []                                                                 # Lista que contendra todos los valores

# Creamos un ciclo while que calcula el valor de los grados Celsius y su aproximado

while F <= 100:
    LF.append(F)                                                                # Agrega el valor a la lista de grados Farenheit
    C = (F - 32)*(5/9)                                                          # Calcula el valor correspondiente de grados Celsius
    LC.append(C)                                                                # Agrega dicho valor a la lista de grados Celsius
    C_approx = (F - 30)/2                                                       # Calcula el valor correspondiente de la aproximacion
    LCA.append(C_approx)                                                        # Agrega dicho valor a la lista de aprximaciones
    F += dF                                                                     # Pasa al siguiente valor de grados Farenheit

# Creamos un ciclo for que agregara los valores deseados a la lista conversion

for i in range(len(LF)):
    conversion.append([LF[i],LC[i],LCA[i]])

# Imprimimos los resultados

print('')
print(['Grados Farenheit','Grados Celsius','Aproximacion grados Celsius'])
print('')

for value in conversion:
    print(value)
    print('')
