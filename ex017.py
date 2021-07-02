import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O comprimento da sua hipotenusa com o cateto oposto de {cateto_oposto} e o adjacente de {cateto_adjacente} é de {hipotenusa:,.2f}.")