#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Digite um número"))
numerodobro = numero * 2
numerotriplo = numero * 3
raiz = float(numero) ** 0.5

print(f"O dobro de {numero}, é {numerodobro}")
print(f"O triplo de {numero}, é {numerotriplo}")
print(f"A raiz de {numero}, é {raiz}")
