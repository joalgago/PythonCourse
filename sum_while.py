# Ejercicio 2.11
# Autor: José García
# Fecha : 2/12/2020
# Descripcion: Computando una suma

# Primero declaramos las variables a usar

s = 0                                                                           # Variable que almacenara la suma
k = 1                                                                           # Iterador de la suma
M = 100                                                                         # Limite superior de la suma

# Usamos un ciclo while para generar la suma

while k <= M:                                                                   # Indica que el ciclo se realizara mientras el valor usado sea menor que el limite
    s += 1/k                                                                    # Va sumando los valores deseados en cada iteracion
    k += 1                                                                      # Aumenta el iterador en una unidad

# Imprimimos el resultado

print(s)

# Uno de los errores es la redaccion al momento de declarar las variables, pues deben declararse en lineas diferentes.

# Otro error es que el iterador no aumentaba su valor, por lo que el programa jamas iba a salir del ciclo while.

# El tercer error es que el limite superior original del ciclo while dejaba fuera el paso k=M, por lo que habia que colocarle un igual que a la expresion
# para hacerla un menor o igual que.
