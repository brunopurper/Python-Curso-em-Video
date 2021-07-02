#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preco_do_produto = float(input("Qual o preço do produto? "))
desconto = 5 * preco_do_produto
preco_do_produto_com_desconto = preco_do_produto - (desconto / 100)
print(f"O preço do produto era de R${preco_do_produto} e com o desconto de 5%, fico com o preço de R${preco_do_produto_com_desconto}.")
