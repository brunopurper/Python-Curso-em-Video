#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


metros = float(input("Digite aqui o valor em metros: "))

centimetros = metros * 100
milimetros = centimetros * 10

print(f"O valor em metros de {metros}, em centimetros fica {centimetros} e em milimetros, {milimetros}")
