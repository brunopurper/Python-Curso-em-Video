#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Digite quanto você tem em reais: "))
dolar = 4.94
compra = dinheiro / dolar
print(f"Com o seu dinheiro em reais {dinheiro}, você compra {compra} doláres na cotação de {dolar}")