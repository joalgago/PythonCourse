# Autor: José García
# Fecha: 8/12/2020
# Descripcion: Tomar nombres, calcular su score e imprimirlos en una tabla

import string

# abrir el archivo y leerlo
file = open('p022_names.txt','r')

DATA = [line.split(',') for line in file]

file.close()

# Calculamos el score de cada nombre y almacenamos nombre y score en una lista

dat = DATA[0]                                                                   # Arreglo que extrae la sublista con solo nombres
letters = 0                                                                     # Variable que almacenara la suma de las posiciones de las letras del nombre

names = []                                                                      # Arreglo que guardara nombres
scores = []                                                                     # Arreglo que guardara scores

for i in range(len(dat)):
    for j in range(1,len(dat[i])-1):                                            # Toma el rango del nombre, quitando las dobles comillas
        letters += (string.ascii_lowercase.index(str(dat[i][j].lower())) + 1)   # Funcion que devuelve el valor de la posicion de las letras en el abecedario, per primero pone el nombre en minusculas
        score = (i + 1)*letters                                                 # Calcula el score
    names.append(dat[i])                                                        # Almacena el nombre
    scores.append(score)                                                        # Almacena el score

# Imprimimos el nombre con el score más alto

msc = max(scores)                                                               # Calcula el score más alto

for i in range(len(scores)):
    if scores[i] == msc:                                                        # Evalua en que posicion se encuentra el maximo
        max = names[i]                                                          # Guarda el nombre que le corresponde

print('El score más alto es de:',max)

# abrir el .tex y escribir el preambulo

file = open('Names_scores.tex','w')

file.write('\\documentclass[11pt, spanish, letterpage]{article} \n')
file.write('\\usepackage[spanish]{babel} \n')
file.write('\\usepackage[utf8]{inputenc} \n')
file.write('\\usepackage{graphicx} \n')
file.write('\\usepackage{float} \n')
file.write('\\title{Nombres y scores} \n')
file.write('\\author{Jose Garcia} \n')
file.write('\\date{\\today} \n')
file.write('\\begin{document} \n')
file.write('\\maketitle \n')

# Ahora creamos el entorno de la Tabla

file.write('\\begin{table}[H] \n')
file.write('\\centering \n')
file.write('\\begin{tabular}{||c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('Nombre & score \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for i in range(30):
    line = ' {n}  &  {s} \\\\ \\hline \n'
    file.write(line.format(n = names[i], s = str(scores[i])))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Datos} \n')
file.write('\\end{table} \n')
file.write('\\end{document}')

# cerramos el archivo

file.close()

# SUBPROCESS

import subprocess

# Para Windows

subprocess.run('pdflatex "Names_scores.tex"', shell = True)
subprocess.run('del "Names_scores.aux"', shell=True)
subprocess.run('del "Names_scores.log"', shell=True)
subprocess.run('del "Names_scores.out"', shell=True)

# Para Linux y Mac

'''
subprocess.call(['pdflatex','Names_scores.tex'])
subprocess.call(['rm', 'Names_scores.aux'])
subprocess.call(['rm', 'Names_scores.log'])
subprocess.call(['rm', 'Names_scores.out'])
subprocess.call(['evince', 'Names_scores.pdf'])
'''

# Archivo en Word
'''
file = open('Names_scores.docx','w')

file.write('Nombre ---------- Score \n')

for i in range(len(scores)):
    line = '{n} ---------- {s} \n'
    file.write(line.format(n = names[i], s = str(scores[i])))

file.close()
'''
