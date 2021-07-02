#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_em_c = float(input("Digite uma temperatura em graus celsius: "))
temperatura_em_f = (temperatura_em_c * 1.8) + 32
print(f"A temperatura de {temperatura_em_c}°C em Fahrenheit fica em {temperatura_em_f}°F ")