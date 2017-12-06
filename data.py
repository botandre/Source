#!/usr/bin/python3
#
# Script para calcular a diferenças entre duas datas
#

import datetime
import os

# Recebendo dados e transformandos em listas
data_atual = input("Data atual (dd/mm/aaaa): ").split('/')
data_n = input("Data N (dd/mm/aaaa): ").split('/')

os.system("clear")

# List comprehension para converter valores do tipo str para int
data_atual = [ int(i) for i in data_atual ]
data_n = [ int(i) for i in data_n]

# Envia respectivamente os valores ano, mês e dia para o metodo date
d1 = datetime.date(data_atual[2], data_atual[1], data_atual[0])
d2 = datetime.date(data_n[2], data_n[1], data_n[0])

qnt_dias = abs((d1 - d2).days) if d1 < d2 else -(d1 - d2).days


# Coloca a '/' de volta
data_atual_completa = "/".join([ str(i) for i in data_atual ])
data_n_completa = "/".join([ str(i) for i in data_n ])

print("De: {}\nPara: {}".format(data_atual_completa, data_n_completa))
print("Faltam {} dias".format(qnt_dias))
