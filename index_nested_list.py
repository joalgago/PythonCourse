# Ejercicio 2.15
# Autor: José García
# Fecha: 2/12/2020
# Descripcion: Trabajando con listas anidadas

# Inciso a

# Declaramos la lista propuesta

q = [['a','b','c'],['d','e','f'],['g','h']]

# Parte 1:

print('Parte 1:')
print(q[0][0])                                                                  # Imprime lo que queremos
print('')

# Parte 2:

print('Parte 2:')
print(q[1])                                                                     # Imprime lo que queremos
print('')

# Parte 3:

print('Parte 3:')
print(q[2][1])                                                                  # Imprime lo que queremos
print('')

# Parte 4:

print('Parte 4:')
print(q[1][0])                                                                  # Imprime lo que queremos
print('')

# q[-1][-2] tiene el valor g pues los numeros negativos comienzan a contar desde la izquierda, siendo -1 el pimer
# elmento desde la izquierda, -2 el segundo y asi sucesivamente. Por ello, elige la primera lista desde la izquierda
# ([g,h]) y luego elige el segundo elemento desde la izquierda (g)

# Inciso b

for i in q:
    for j in range(len(i)):
        print(i[j])

# i es un elemento de q, es decir, es una lista; y j es un entero que lee las posiciones de la lista i
