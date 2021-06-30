dias = float(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

dias_aluguel = dias * 60
km_rodados_aluguel = km_rodados * 0.15
quantidade_a_pagar = dias_aluguel + km_rodados_aluguel


print(f"O total a pagar é de R$: {quantidade_a_pagar}")