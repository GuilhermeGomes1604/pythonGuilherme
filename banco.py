import os
os.system("cls")

print(r"""
               _____          _             _                 
__/\____/\__  | ____|   _ ___| |_ __ _  ___| | __  __/\____/\__
\    /\    /  |  _|| | | / __| __/ _` |/ __| |/ /  \    /\    /
/_  _\/_  _\  | |__| |_| \__ \ || (_| | (__|   <   /_  _\/_  _\
  \/    \/    |_____\__,_|___/\__\__,_|\___|_|\_\    \/    \/  
  """)


print("\n","="*60,"\n")
saldo=5000.00
print("Saldo Atual: R$", round(saldo, 2))
print("\n")

while True:
    resp=int(input("— Escolha um tipo de transação:\n\n 1. Sacar \n 2. Depositar\n\n— "))
    print("\n","="*60,"\n")

    if resp==1: 
        print("Você escolheu: Sacar.\n")
        print("Saldo Atual: R$", round(saldo, 2))
        neovalor=float(input("Insira um valor para retirar: "))
        if neovalor<=0 or neovalor>saldo: #essa condição faz o usuário voltar para a linha 21, ao invés da linha 27 como eu queria. o que fazer?
            print("\nValor inválido.\n\n")
            continue
        saldo=saldo-neovalor
        print("\nNovo Saldo: R$",round(saldo, 2))
        print("Valor Sacado: R$", round(neovalor,2))
    elif resp==2:
        print("Você escolheu: Depositar.\n")
        print("Saldo Atual: R$",round(saldo, 2))
        neovalor=float(input("Insira um valor para depositar: "))
        if neovalor<=0:
            print("\nValor inválido.\n\n")
            continue
        saldo=saldo+neovalor
        print("\nNovo Saldo: R$", round(saldo, 2))
        print("Valor Depositado: R$", round(neovalor,2))
    else: 
        print("Opção Inexistente.\n") # se a resposta não for int o sistema cai, mas se tirar o "int" do input na linha 22 qualquer resposta é inválida, cai no else. porque?/e o espaço? ele dá erro também? é considerado string pelo sistema?
        continue

    while True:
        print("\n","="*60,"\n")
        coisa=(input("Deseja fazer mais alguma coisa? (Sim ou Não)\n\n— "))
        if coisa=="sim" or coisa=="SIM" or coisa=="Sim": # tem como usar um "if (in)" aqui e na linha 50?
            print("\n")
            break
        elif coisa=="nao" or coisa=="não" or coisa=="Não" or coisa=="Nao" or coisa=="NAO" or coisa=="NÃO": 
            print("\n\nEntendido. Obrigado pela preferência, até mais!\n")
            print("="*60,"\n")
            quit()     
        else:
            print("\n\nResposta não compreendida. Por favor, tente novamente.\n")
            continue
