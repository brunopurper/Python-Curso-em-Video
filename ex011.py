base_parede = float(input("Digite a largura da parede a ser pintada: "))
altura_parede = float(input("Digite a altura da parede a ser pintada: "))

area_parede = base_parede * altura_parede
litro_de_tinta = 2
quantos_litros_necessarios = area_parede / litro_de_tinta

print(f"Para pintar {area_parede}m2 de parede, serão necessários {quantos_litros_necessarios} litros de tinta!")


