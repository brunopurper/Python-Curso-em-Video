#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome: ")).strip()
nomeup= nome.upper()
nomelow= nome.lower()

nomefatia = nome.split()
nomefatia = len(nomefatia[0]) + len(nomefatia[1])

primeiro_nome = nome.split()
primeiro_nome = len(primeiro_nome[0])

print(f""" =============================================
O seu nome em letras maisculas é {nomeup} e minisculas é {nomelow}:
Seu nome completo tem {len(nome) - nome.count(' ')} letras, e somente seu primeiro nome tem {primeiro_nome}

""")