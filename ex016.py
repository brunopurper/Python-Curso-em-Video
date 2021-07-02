#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input("Digite um número flutuante: "))
num_inteiro = math.floor(num)
print(f"O número {num} tem a parte inteira {num_inteiro}")
