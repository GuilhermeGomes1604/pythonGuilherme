import os
os.system("cls")

# atividade 1: maças

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


# atividade 2: vogal ou consoante

# print("Vogal ou Consoante?")
# print()
# letra= str(input("Insira um letra: "))

# if letra == "a" or letra =="A" or letra =="e" or letra =="E" or letra =="i" or letra =="I" or letra =="o" or letra =="O" or letra =="u" or letra =="U":
#     print("Você inseriu uma vogal.")
# else:
#     print("Você inseriu uma consoante.")

# atividade 3: maior ou menor

# print()
# print("********** Maior ou menor? **********")
# print()

# no1= float(input("Digite um primeiro número:  "))
# no2= float(input("Digite um segundo número:   "))
# print()

# if no1<no2:
#     print(no1, "<", no2)
#     print()
#     print("Maior número: ",no2)
#     print("Menor número: ",no1)
#     print()
# elif no1==no2:
#     print("ERRO: Os dois números são iguais.")
#     print()
# else:
#     print(no2,"<",no1)
#     print()
#     print("Maior número: ",no1)
#     print("Menor número: ",no2)
#     print()

#teste de sistema de autenticação por email

# email=input("Digite seu email: ")
# senha=input("Digite a senha: ")

# if email=="email@gmail.com":
#     if senha=="gamma":
#         print("dados corretos")
#     else:
#         print ("dados incorretos: email certo, senha errada")
# elif senha=="gamma":
#     print("dados incorretos: senha certa, email errado")
# else:
#     print("dados completamente incorretos")

#atividade 3: sistema de notas

# print()
# print("****************** <BOLETIM> ******************")
# print()
# nota1= float(input("Digite a primeira nota: "))
# nota2= float(input("Digite a segunda nota:  "))
# print()
# media= (nota1+nota2)/2
# print("***********************************************")
# print()
# print(f"Média do aluno: {media:.2f}")

# if media<5:
#     print("<ALUNO REPROVADO>")
# elif media >=5 and media <=7:
#     print("<ALUNO EM RECUPERAÇÃO>")
# else:
#     print("<ALUNO APROVADO!>")
#     print()

#atividade 4:

# print()
# print("*"*15, "<Cálculo de IMC (Índice de Massa Corporal>", "*"*15)
# print()

# p=float(input("Digite seu peso (em KG): "))
# h=float(input("Digite sua altura (em metros): "))
# imc= p/(h*h)

# print()
# print("Seu IMC é de: ", round(imc, 2))
# print()
# if imc <17:
#     print("Situação: Muito Abaizo do Peso")

# elif imc>= 17 and imc<=18.49:
#     print("Situação: Abaixo do Peso")

# elif imc>=18.5 and imc<=24.49:
#     print("Situação: Peso Normal")

# elif imc>=24.5 and imc<=29.99:
#     print("Situação: Acima do Peso")

# elif imc>=30 and imc<=34.99:
#     print("Situação: Obesidade I")

# elif imc>=35 and imc<=39.99:
#     print("Situação: Obesidade II")

# else:
#     print("Situação: Obesidade Mórbida (III)")

# atividade 6

print()
print(r"""    
                   _         _                      
                  / \  _   _| |_ ___   ___ __ _ _ __ 
                 / _ \| | | | __/ _ \ / __/ _` | '__|
                / ___ \ |_| | || (_) | (_| (_| | |   
               /_/   \_\__,_|\__\___/ \___\__,_|_|   


                       _____________________                              
                     //|           |        \                            
                   //  |           |          \                          
      ___________//____|___________|__________()\__________________      
    /__________________|_=_________|_=___________|_________________{}    
    [           ______ |           | .           | ==  ______      { }   
  __[__        /##  ##\|           |             |    /##  ##\    _{# }_ 
 {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
             /  ##__##                              /  ##__##        \ 


""")

print("*"*20,"<REAJUSTE SALARIAL>","*"*20)
print()
salini=float(input("Informe seu salário: R$"))
print()

if salini<=2799.99:
    salfin=salini * 1.2
    aum= salfin - salini
    print("1. Salário Original: R$",salini)
    print("2. Percentual de Aumento Aplicado: 20%")
    print("3. Valor do Aumento: R$",round(aum,2))
    print("4. Salário Atualizado: R$",round(salfin,2))
elif salini<=6999.99:
    salfin=salini* 1.15
    aum= salfin - salini
    print("1. Salário Original: R$", salini)
    print("2. Percentual de Aumento Aplicado: 15%")
    print("3. Valor do Aumento: R$",round(aum,2))
    print("4. Salário Atualizado: R$", round(salfin,2))
elif salini<=14999.99:
    salfin=salini* 1.1
    aum= salfin - salini
    print("1. Salário Original: R$", salini)
    print("2. Percentual de Aumento Aplicado: 10%")
    print("3. Valor do Aumento: R$",round(aum,2))
    print("4. Salário Atualizado: R$",round(salfin,2))
else:
    salfin=salini*1.05
    aum= salfin - salini
    print("1. Salário Original: R$", salini)
    print("2. Percentual de Aumento Aplicado: 5%")
    print("3. Valor do Aumento: R$", round(aum,2))
    print("4. Salário Atualizado: R$", round(salfin,2))

print()
