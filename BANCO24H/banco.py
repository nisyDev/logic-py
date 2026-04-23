import random
numProt = random.randint(1000000, 7000000)

#variáveis globais imutáveis
saldo = 250.00
transf = 0



# ==================
# Validação de Dados
# ==================

print("""Bem vindo(a) ao Banco 24h\n
----------------------------------------------------------------------------------------------------------------------------\n
AVISO: Para sua segurança, informamos que seus dados serão utilizados somente para consultas e tratados conforme a lei LGPD.\n
----------------------------------------------------------------------------------------------------------------------------\n
Por favor, informe seu nome: """)
nome = input()

print("\nAgora, insira seu CPF: ")



# ==================
#  Validação de CPF
# ==================

#função = def
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    #remove tudo o que não for número no input do usuário, como string vai contar a quantidade de caracteres no cpf

    #se tamanho(input) for diferente de 11 ou o input for repetido, repete
    if len(cpf) != 11 or cpf == cpf[0] * 11: #exemplo: 5 * 11 = 55555555555
        return False

    #soma inicia com 0 para ser calculada
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    #percorre os nove dígitos, pega o número, multiplicar pelo peso e soma tudo (que é o cálculo de cpf)

    #pega o resto do cálculo total e divide ele por 11, para dar um número de 0 a 10
    totalResto = soma % 11
    dig1 = 0 if totalResto < 2 else 11 - totalResto


    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    totalResto = soma % 11
    dig2 = 0 if totalResto < 2 else 11 - totalResto

    return cpf[-2:] == f"{dig1}{dig2}"

while True:
    cpf = input()
    if validar_cpf(cpf):
        break
    else:
        print("CPF inválido. Tente novamente.")

def end():
    print("Obrigada por utilizar nosso Banco 24h!")
    exit()



# ==================
#   Menu Inicial
# ==================

def first_menu():

    while True:
        print(f"\n{nome}, este é o menu inicial do Banco 24h. Por favor, digite  opção desejada")
        print("1 - Minha Carteira")
        print("2 - Minha Conta")
        print("0 - Sair")

        select = input()

        opcoes = {
        "1": wallet,
        "2": account,
        "0": end
        }
        if select in opcoes:
            opcoes[select]()
        else:
            print("Opção inválida")



# ========================
# Submenu "Minha Carteira"
# ========================

def wallet():

    def consulSaldo():
        global saldo
        print(f"Seu saldo é de {saldo}\n")
        return True

    def addSaldo():
        global saldo
        new = float(input("Digite o valor para adicionar na carteira: "))
        saldo = saldo + new
        print(f"Seu saldo atualizado é de: R${saldo}\n")
        return True

    def transfSaldo():
        global saldo, transf
        transf = float(input("Digite o valor para transferir: "))
        saldo = saldo - transf

        print("Digite os dados do recebedor: ")
        nameTrans = input("Nome completo: ")
        numAg = input("Agência: ")
        numConta = input("Conta: ")

        print("Dados informados: ")
        print(nameTrans)
        print(numAg)
        print(numConta)
        print(f"R${transf}")
        print("\n\n\nAguarde...\n\n")
        print(f"Transferência concluída! Seu saldo atualizado é de: R${saldo}\n")
        return True

    def verExtr():
        global saldo
        print(f"Transferência realizada recentemente: {transf}")
        print(f"Saldo atual: {saldo}\n")
        return()

    def voltar_menu_princ():
        first_menu()
    

    opcoes = {
    "1": consulSaldo,
    "2": addSaldo,
    "3": transfSaldo,
    "4": verExtr,
    "5": voltar_menu_princ,
    "0": end
    }

    while True:
        print("Carteira")
        print("1 - Consultar Saldo")
        print("2 - Adicionar Saldo")
        print("3 - Transferir Saldo")
        print("4 - Extrato Geral")
        print("5 - Voltar")
        print("0 - Sair")

        select = input()

        if select in opcoes:
            opcoes[select]()
        else:
            print("Opção inválida")



# =====================
# Submenu "Minha Conta"
# =====================

def account():

    def info():
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print("Tipo de conta: Corrente\n")
        return True

    def agent():
        print(f"Seu protocolo de atendimento é {numProt}. Para validar e continuar seu atendimento, acesse sua conta no site ou aplicativo no celular.\n")
        end()

    def voltar_menu_princ():
        first_menu()


    opcoes = {
    "1": info,
    "2": agent,
    "3": voltar_menu_princ,
    "0": end
    }

    while True:
        print("Minha Conta")
        print("1 - Informações de conta")
        print("2 - Solicitar atendimento")
        print("3 - Voltar")
        print("0 - Sair")

        select = input()

        if select in opcoes:
            opcoes[select]()
        else:
            print("Opção inválida")

first_menu()