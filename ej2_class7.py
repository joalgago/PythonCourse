# Autor: José García
# Fecha: 8/12/2020
# Descripcion: Evaluar identidades matematicas

import math as m
from random import random

# Inicializamos los números aleatorios:

A = []                                                                          # Lista de numeros a
B = []                                                                          # Lista de numeros b

for i in range(10):
    A.append(10*random())
    B.append(10*random())

# Creamos los arreglos de las operaciones y realizamos dichas operaciones

exp_4 = []
exp = []
ln = []
sen_h = []
log = []

for i in range(len(A)):
    value1 = (A[i]*B[i])**4
    value2 = (A[i]**4)*(B[i]**4)
    value3 = "%.3f" % value1
    value4 = "%.3f" % value2
    if value1 == value2:
        cond1 = 'Si'
    else:
        cond1 = 'No'
    if float(value3) == float(value4):
        cond2 = 'Si'
    else:
        cond2 = 'No'
    exp_4.append([value1,value2,cond1,value3,value4,cond2])

for i in range(len(A)):
    a = A[i]
    b = B[i]
    value1 = m.exp(a+b)
    value2 = (m.exp(a))*(m.exp(b))
    value3 = "%.3f" % value1
    value4 = "%.3f" % value2
    if value1 == value2:
        cond1 = 'Si'
    else:
        cond1 = 'No'
    if float(value3) == float(value4):
        cond2 = 'Si'
    else:
        cond2 = 'No'
    exp.append([value1,value2,cond1,value3,value4,cond2])

for i in range(len(A)):
    value1 = m.log(A[i]*B[i])
    value2 = m.log(A[i]) + m.log(B[i])
    value3 = "%.3f" % value1
    value4 = "%.3f" % value2
    if value1 == value2:
        cond1 = 'Si'
    else:
        cond1 = 'No'
    if float(value3) == float(value4):
        cond2 = 'Si'
    else:
        cond2 = 'No'
    ln.append([value1,value2,cond1,value3,value4,cond2])

for i in range(len(A)):
    value1 = m.sinh(A[i]+B[i])
    value2 = ((m.exp(A[i])*m.exp(B[i])) - (m.exp(-A[i])*m.exp(-B[i])))/2
    value3 = "%.3f" % value1
    value4 = "%.3f" % value2
    if value1 == value2:
        cond1 = 'Si'
    else:
        cond1 = 'No'
    if float(value3) == float(value4):
        cond2 = 'Si'
    else:
        cond2 = 'No'
    sen_h.append([value1,value2,cond1,value3,value4,cond2])

for i in range(len(A)):
    value1 = m.log(100 , A[i]*B[i])
    value2 = (m.log(100, A[i])*m.log(100, B[i]))/(m.log(100, A[i]) + m.log(100, B[i]))
    value3 = "%.3f" % value1
    value4 = "%.3f" % value2
    if value1 == value2:
        cond1 = 'Si'
    else:
        cond1 = 'No'
    if float(value3) == float(value4):
        cond2 = 'Si'
    else:
        cond2 = 'No'
    log.append([value1,value2,cond1,value3,value4,cond2])

# abrir el .tex y escribir el preambulo

file = open('Identities.tex','w')

file.write('\\documentclass[11pt, spanish, letterpage]{article} \n')
file.write('\\usepackage[spanish]{babel} \n')
file.write('\\usepackage[utf8]{inputenc} \n')
file.write('\\usepackage{graphicx} \n')
file.write('\\usepackage{float} \n')
file.write('\\title{Tablas de identidades} \n')
file.write('\\author{Jose Garcia} \n')
file.write('\\date{\\today} \n')
file.write('\\begin{document} \n')
file.write('\\maketitle \n')

# Ahora creamos el entorno de la Tabla

file.write('\\begin{table}[H] \n')
file.write('\\raggedright \n')
file.write('\\begin{tabular}{||c|c|c|c|c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$(ab)^{4}$ & $a^{4}b^{4}$ & Ig & $(ab)^{4}$ red & $a^{4}b^{4}$ red & Ig \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for val in exp_4:
    line = ' {v}  &  {v2} &  {i}  &  {r} & {r2}  &  {i2} \\\\ \\hline \n'
    file.write(line.format(v = str(val[0]), v2 = str(val[1]), i = val[2], r = val[3], r2 = val[4], i2 = val[5]))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Exponencial cuarta} \n')
file.write('\\end{table} \n')

file.write('\\begin{table}[H] \n')
file.write('\\raggedright \n')
file.write('\\begin{tabular}{||c|c|c|c|c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$e^{a+b}$ & $e^{a}e^{b}$ & Ig & $e^{a+b}$ red & $e^{a}e^{b}$ red & Ig \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for val in exp:
    line = ' {v}  &  {v2} &  {i}  &  {r} & {r2}  &  {i2} \\\\ \\hline \n'
    file.write(line.format(v = str(val[0]), v2 = str(val[1]), i = val[2], r = val[3], r2 = val[4], i2 = val[5]))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Exponencial natural} \n')
file.write('\\end{table} \n')

file.write('\\begin{table}[H] \n')
file.write('\\raggedright \n')
file.write('\\begin{tabular}{||c|c|c|c|c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$\\ln(ab)$ & $\\ln(a)+\\ln(b)$ & Ig & $\\ln(ab)$ red & $\\ln(a)+\\ln(b)$ red & Ig \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for val in ln:
    line = ' {v}  &  {v2} &  {i}  &  {r} & {r2}  &  {i2} \\\\ \\hline \n'
    file.write(line.format(v = str(val[0]), v2 = str(val[1]), i = val[2], r = val[3], r2 = val[4], i2 = val[5]))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Logaritmo natural} \n')
file.write('\\end{table} \n')

file.write('\\begin{table}[H] \n')
file.write('\\raggedright \n')
file.write('\\begin{tabular}{||c|c|c|c|c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$\\sinh(a + b)$ & $\\frac{e^{a} e^{b} - e^{-a} e^{-b}}{2}$ & Ig & $\\sinh(a + b)$ red & $\\frac{e^{a} e^{b} - e^{-a} e^{-b}}{2}$ red & Ig \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for val in sen_h:
    line = ' {v}  &  {v2} &  {i}  &  {r} & {r2}  &  {i2} \\\\ \\hline \n'
    file.write(line.format(v = str(val[0]), v2 = str(val[1]), i = val[2], r = val[3], r2 = val[4], i2 = val[5]))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Seno hiperbolico} \n')
file.write('\\end{table} \n')

file.write('\\begin{table}[H] \n')
file.write('\\raggedright \n')
file.write('\\begin{tabular}{||c|c|c|c|c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$\\log _{ab}{n}$ & $\\frac{\\log _{a} {n} \\log _{b} {n}}{\\log _{a} {n} + \\log _{b} {n}}$ & Ig & $\\log _{ab} {n}$ red & $\\frac{\\log _{a} {n} \\log _{b} {n}}{\\log _{a} {n} + \\log _{b} {n}}$ red & Ig \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')

# crear la tabla y escribirla
for val in log:
    line = ' {v}  &  {v2} &  {i}  &  {r} & {r2}  &  {i2} \\\\ \\hline \n'
    file.write(line.format(v = str(val[0]), v2 = str(val[1]), i = val[2], r = val[3], r2 = val[4], i2 = val[5]))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Logaritmo} \n')
file.write('\\end{table} \n')
file.write('\\end{document}')

# cerramos el archivo

file.close()

# SUBPROCESS

import subprocess

# Para Windows

subprocess.run('pdflatex "Identities.tex"', shell = True)
subprocess.run('del "Identities.aux"', shell=True)
subprocess.run('del "Identities.log"', shell=True)
subprocess.run('del "Identities.out"', shell=True)

# Para Linux y Mac

'''
subprocess.call(['pdflatex','Identities.tex'])
subprocess.call(['rm', 'Identities.aux'])
subprocess.call(['rm', 'Identities.log'])
subprocess.call(['rm', 'Identities.out'])
subprocess.call(['evince', 'Identities.pdf'])
'''
