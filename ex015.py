#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

dias_aluguel = dias * 60
km_rodados_aluguel = km_rodados * 0.15
quantidade_a_pagar = dias_aluguel + km_rodados_aluguel


print(f"O total a pagar é de R$: {quantidade_a_pagar}")