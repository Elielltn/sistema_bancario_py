menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
id_transacao = 0
limite = 500
extrato = []
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu) 
    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            id_transacao += 1
            extrato.append(f"{id_transacao}. Depósito de R${valor_deposito:,.2f} reais.")
            print(f"Deposito de R${valor_deposito:,.2f} reais efetuado com sucesso.")
        else:
            print(f"Você selecionou um valor inválido. Refaça a operação")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(f"A operação falhou! Você não tem saldo suficiente. Seu saldo é de R${saldo:,.2f} reais")
        elif excedeu_limite:
            print(f"A operação falhou! O valor do saque excede o limite de R${limite:,.2f} reais")
        elif excedeu_saques:
            print(f"A operação falhou! Número máximo de saques atingido")
        elif valor_saque > 0:
            saldo -= valor_saque
            id_transacao += 1
            numeros_saques += 1
            extrato.append(f"{id_transacao}. Saque de R${valor_saque:,.2f} reais.")
            print(f"Saque de R${valor_saque:,.2f} reais efetuado com sucesso.")       
                 
    elif opcao == "e":
        print (f"Este é seu saldo: R${saldo:,.2f} reais.")
        if not extrato:
            print("Você ainda não fez nenhuma trasação.")
        else:
            print (f"Estas são suas transações:")
            for info in extrato:
                print(info)
            
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")