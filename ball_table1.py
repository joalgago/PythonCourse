# Ejercicio 2.8
# Autor: José García
# Fecha: 2/12/2020
# Descripcion: Tabla con valores de posiciones respecto al tiempo de un tiro parabolico

# Inciso a

# Declarar las constantes a usar

v = 5                                                                           # Velocidad inicial
g = 9.81                                                                        # Gravedad
n = 20                                                                          # Numero de intervalos
s = ((2*v)/g)/n                                                                 # Saltos entre intervalos
t = 0                                                                           # Tiempo actual del movimiento

# Declaramos la variable que almacenara las posiciones calculadas y la lista que las contendra todas

y = 0.0
Y = []

# Generamos el ciclo for que calculara las posiciones y las almacenara en la lista

for i in range(n+1):
    t = i*s                                                                     # Realiza el salto de intervalo
    y = (v*t - (1/2)*(g*(t**2)))                                                # Ingresa el valor de la posicion calculada
    Y.append(y)                                                                 # Agrega el valor calculado a la lista

# Imprimimos el resultado
print('Posiciones en intervalos de tiempo:')
print('')

for posicion in Y:
    print(posicion)


# Inciso b

print('')

# Volvemos a colocar valores iniciales en las variables que usamos en el ciclo for

y = 0.0
Y = []
t = 0

# Inicializamos un iterador

i = 0

# Creamos el ciclo while para realizar lo mismo que el ciclo for anterior

while i <= n:
    t = i*s                                                                     # Realiza el salto de intervalo
    y = (v*t - (1/2)*(g*(t**2)))                                                # Ingresa el valor de la posicion calculada
    Y.append(y)                                                                 # Agrega el valor calculado a la lista
    i += 1                                                                      # Aumentamos el iterador

# Imprimimos el resultado
print('Posiciones en intervalos de tiempo:')
print('')

for posicion in Y:
    print(posicion)
