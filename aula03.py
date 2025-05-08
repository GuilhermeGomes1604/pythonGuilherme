import os
os.system("cls")

Continuação Input com Int e Float
int() -> converte para inteiro
float() -> converte para n quebrado

numero= 10
numero2 = input("digite um numero:")
print("o tipo de numero é,", type(numero2))
soma= numero + int(numero2)
print(f"soma de {numero}+{numero2}=", soma )

outro exemplo
num1= input("digite um numero")
soma = float(num1) + 50
print(" a soma de" ,num1 ,"+" "50", "=", soma)

mais um exemplo
n1= float(input("digite um numero:"))
n2= float(input("digite outro numero:"))
soma= n1+n2
print(f"a soma de {n1} + {n2} =", soma) 


exercicios
#1
numero= float(input("digite um numero:"))
numero2= float(input("digite outro numero:"))
mult= numero*numero2 
print(f"a multiplicacao de {numero} * {numero2} =", mult)

#2
nu1= float(input("digite um numero:"))
antecessor= nu1 -1
sucessor= nu1 +1
print(f"antecessor {antecessor}")
print(f"sucessor {sucessor}")

#3
ano= float(input("digite o ano de seu nascimento:"))
idade= 2025 - ano
print(f"voce tem: {idade} anos")

#porcentagem
print("25% de 100=" , 0.25 * 100)
print("4% de 400=" , 0.04 * 400)
print("99% de 1525=", 0.99 * 1525)

# supondo que um produto custa 100 reais
# e o caixa deu um de desconto de 15%
exemplo= float(input("digite o preco do produto:"))
desconto= 0.15 * exemplo
print("o preco do produto com 15% de desconto é:", exemplo-desconto)

escreva um programa que leia 2 itens de um mercado voce deve
armazenar o nome e o valor di item, no final aplicar 10% de desconto 
no primeiro item 25% no segundo. Calcule o valor total da compra 
e mostre o nome e valor com desconto de cada item

print("MERCADO")
item1= (input("digite o nome do primeiro produto:"))
desconto1=float(input("valor do produto:"))
item2= (input("digite o nome do segundo produto: "))
desconto2=float(input("volhor do outro produto:"))

valorcomdes1= 0.10 * desconto1
valorcomdes2= 0.25 * desconto2

valorfinal1= round(desconto1-valorcomdes1,2)
valorfinal2= round(desconto2-valorcomdes2,2)


print("CAIXA")
print(f"{item1} tem 10% de desconto = {valorfinal1}")
print(f"{item2}tem 25% de desconto = {valorfinal2}")

print("TOTAL")
print(f"o total é R$: {valorfinal1 + valorfinal2}")


