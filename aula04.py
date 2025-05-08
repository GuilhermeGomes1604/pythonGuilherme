import os
os.system("cls")
# #ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
# #OPERADORES CONDICIONAIS:  > >= < <= != == and or
# # > (maior)
# # >= ( maior OU igual)
# # < (menor)
# # <= (menor OU igual)
# # == (igual) 
# # != (diferente)
# # and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# # or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

# #if condicao :
# # print("verdade")
# #else: 
# #print("falso")

# # A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# # nome = "teste"
# # if "testee" != nome:
# #     print(1)
# # else:
# #     print(2)

# #exercicio if Else

# # #1
# idade= input("digite a sua idade:")
# if idade == 18: 
#     print("maior") 
# else:
#       print("menor")

# # #2
# idade= int(input("digite sua idade: "))
# if idade == 0 or idade > 120:
#         print("idade é invalida")
# else:
#     print("idade valida")


# # #3
# email= input("digite seu email:")
# senha= input("digite seua senha")
# if email  == "python@senai.com": 
#      if senha == "12345678":
#           print("usuario autenticado")
# else:
#       print("usuario ou senha invalido")

#atidade4

# print("********** COMPENN **********")
# print()


# qnt= int(input("Bom dia! Quantas maças deseja comprar hoje? ")) 

# if qnt<12:
#      print("Você comprou: ", qnt, " maçãs.")
#      calc= qnt*0.30
#      print("VALOR TOTAL:", calc, " maçãs.")
# else:
#      print("Você comprou: ", qnt, " maçãs." )
#      calc= qnt * 0.25
#      print("VALOR TOTAL: ", calc, " maças.")


#atividade 5

print("Vogal ou Consoante?")
print()
letra= str(input("Insira um letra: "))

if letra == "a" and "A" and "e" and "E" and "i" and "I" and "o" and "O" and "u" and "U":
    print("Você inseriu uma vogal.")
else:
    print("Você inseriu uma consoante.")