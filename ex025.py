# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite seu nome: ")).strip()
nome = nome.lower()
verificador = "silva" in nome
print(verificador)
