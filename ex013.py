#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário: "))
aumento = (salario * 15) / 100 + salario
print(f"O salário de R${salario}, que o funcionário recebia, ganhou um aumento e agora é de R${aumento}")