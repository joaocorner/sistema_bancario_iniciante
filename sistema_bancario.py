def cor_texto(texto, cor="default", negrito=False, sublinhado=False):
    # Dicionário de cores
    cores = {
        "preto": "30",
        "vermelho": "31",
        "verde": "32",
        "amarelo": "33",
        "azul": "34",
        "magenta": "35",
        "ciano": "36",
        "branco": "37",
        "default": "39",
    }

    # Códigos de estilo
    codigo_cor = cores.get(cor.lower(), "39")
    codigo_negrito = "1" if negrito else "22"
    codigo_sublinhado = "4" if sublinhado else "24"

    # Aplicando estilos e cor
    return f"\033[{codigo_negrito};{codigo_sublinhado};{codigo_cor}m{texto}\033[0m"



menu = """

[d] Depositar [s] Sacar [e] Extrato [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor = float(input("Qual valor a ser depositado?\n"))
        
        if valor <= 0:
            print("Favor, informar um valor de depósito positivo.")
        else:
            saldo += valor
            print(f"Saldo atual de R${saldo:.2f}")
            extrato += f" Realizado um depósito de R${cor_texto(f'{valor:.2f}','verde')}\n"
            

    elif opcao == "s":
        print("Saque")
        if saldo > 0:
            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Informa o valor a ser retirado:\n"))

                if valor >= saldo:
                    print(
                        f"Saldo de R${saldo:.2f} insuficiente para sacar R${valor:.2f}"
                    )
                
                elif valor <= 0:
                    
                    print("Favor iniciar a operação novamente informando um valor válido.")

                elif valor > 500:
                    print(f"Saque máximo permitido de R$500,00.")

                else:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f" Realizado um saque de R${cor_texto(f'{valor:.2f}','vermelho')}\n"
                    
                    if numero_saques == 2:
                        print(
                            f"Saque de R${valor:.2f} realizado com sucesso. Você tem mais 1 saque disponível."
                        )
                    elif numero_saques == 3:
                        print(
                            f"Saque de R${valor:.2f} realizado com sucesso. Fim dos saques disponíveis no dia."
                        )

                    else:
                        print(
                            f"Saque de R${valor:.2f} realizado com sucesso. Você tem mais {LIMITE_SAQUES-numero_saques} saques disponíveis."
                        )

            else:
                print("Você alcançou o limite de saques do dia.")
        else:
            print("Deposite algum valor antes, saldo zerado.")

    elif opcao == "e":
        
        if extrato == "":
            print("Ops.. Nada por aqui, realize algum depósito.")
            print(f"Saldo: R${cor_texto(f'{saldo:.2f}', 'vermelho') if saldo <= 0 else cor_texto(f'{saldo:.2f}', 'verde')}") 
            
        else:
            print(f"{"EXTRATO".center(40, '#')}")
            print(extrato)
            #uso futuro, caso o valor fosse negativo imprimiria em vermelho
            print(f" Saldo: R${cor_texto(f'{saldo:.2f}', 'vermelho') if saldo <= 0 else cor_texto(f'{saldo:.2f}', 'verde')}") 
            print(f"{"#".center(40, '#')}")

    elif opcao == "q":
        break

    else:
        print("Opcão inválida")
