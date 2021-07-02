#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


base_parede = float(input("Digite a largura da parede a ser pintada: "))
altura_parede = float(input("Digite a altura da parede a ser pintada: "))

area_parede = base_parede * altura_parede
litro_de_tinta = 2
quantos_litros_necessarios = area_parede / litro_de_tinta

print(f"Para pintar {area_parede}m2 de parede, serão necessários {quantos_litros_necessarios} litros de tinta!")


