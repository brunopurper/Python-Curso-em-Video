#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Digite um número"))
numeroant = numero - 1
numeronext = numero + 1

print(f"Você digitou o número {numero}, o número anterior a esse é {numeroant}, e o posterior é {numeronext}")