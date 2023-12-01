# Ejercicio 2.13
# Autor: José García
# Fecha: 2/12/2020
# Descripcion: Revision de ciclos while en calculo de años aplicados a intereses

# Declaracion de la funcion propuesta por el libro

initial_amount = 100
p = 5.5                                                                         # Tasa de interes
amount = initial_amount
years = 0
limit = 1.5*initial_amount                                                      # Tope de la iteración con p positivo

if p > 0:
    while amount <= limit:
        amount += (p/100)*amount
        years += 1
elif p < 0:
    print('Error, no se acepta tasa de interes negativa')

print(years)

# Este programa se encarga de calcular en cuantos años, con la tasa de interes dada, la cantidad inicial de dinero
# invertida aumentara hasta 1.5 veces su valor original

# Si p es negativo, el programa nunca sale del ciclo while, pues la variable amount solo disminuye su valor,
# por lo que es imposible que llege al limite establecido en el ciclo.
