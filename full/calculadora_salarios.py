# -*- coding: utf-8 -*-
"""python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4UAKh54Kk5qPnKyHFl8M3eol0y36VYU
"""

salario = float(input("Qual o salário do funcionário?"))
aumento = float(input("Qual a porcentagem de aumento?"))

novosalario = salario + (salario*aumento)/100

print("O salario inicial era de {}, o aumento foi de {}% e o novo salario é de {}".format(salario,aumento,novosalario))