#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.


numero = int(input("Digite o número da tabuada que vc quer: "))

for i in range(11):
    tabuada = numero * i
    print(f"{numero} X {i} = {tabuada}")
