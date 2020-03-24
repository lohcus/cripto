import crypt, os, math, sys
from time import sleep

# FUNCAO PARA EXIBIR OS TITULOS DAS TELAS
def titulo(title):
    igual = "=" * math.trunc((80-len(title))/2)
    a = 10.2
    if len(igual+title+igual) == 79:
        sys.stdout.write("\033[1;32m{}\033[1;31m{}\033[m\033[1;32m{}=\033[m\n".format(igual,title,igual))
    else:
        sys.stdout.write("\033[1;32m{}\033[1;31m{}\033[1;32m{}\033[m\n".format(igual, title, igual))
    title = "BY  DANIEL"
    igual = "=" * math.trunc((80-len(title))/2)
    sys.stdout.write("\033[1;32m{}\033[1;37m{}\033[1;32m{}\033[m\n".format(igual,title,igual))
# ========================================================================================================

def criptografa():
    salt = input("\033[1;33mDigite o salt: \033[m")
    senhas = input("\033[1;33mEntre com a senha ou um arquivo de senhas: \033[m")
    calcula_hash(salt,senhas)


def descriptografa():
    salt = input("\033[1;33mDigite o salt: \033[m")
    senhas = input("\033[1;33mEntre com o hash ou um arquivo de hashes: \033[m")
    compara_hash(salt,senhas)
# ========================================================================================================

# FUNÇÃO PARA VISUALIZAR O ARQUIVO DE HASHES GERADO
def visualizar():
    print()
    try:
        with open("hashes.txt", "r") as hashes:
            for hash in hashes:
                print(f"\033[1;33mHash: \033[1;32m{hash.split('---')[0]} \033[1;33m-> Senha: \033[1;32m{hash.split('---')[1]}\033[m")
        input("PRESSIONE ENTER PARA CONTINUAR...")

    except Exception as erro:
        print(erro)
        input('\033[1;31m\nOCORREU ALGUM PROBLEMA! PRESSIONE ENTER PARA CONTINUAR...\033[m')
# ========================================================================================================

# FUNCAO PARA CALCULAR OS HASHES E SALVAR EM UM ARQUIVO
def calcula_hash(salt,senhas):
    controle = 0
    hashes = open("hashes.txt", "w")
    try:
        # SE O QUE FOI DADO ENTRADA FOR ARQUIVO ELE LÊ LINHA A LINHA
        if os.path.exists(senhas):
            with open(senhas, "r") as senhas:
                for senha in senhas:
                    hashes.write(crypt.crypt(senha,salt) + "---" + senha)
                hashes.close()

        # CASO O QUE FOI DADO ENTRADA SEJA UMA SENHA, ELE CRIPTOGRAFA E GRAVA NO ARQUIVO
        else:
            hashes.write(crypt.crypt(senhas, salt) + "---" + senhas)
            hashes.write("\n")
            hashes.close()

        input('\033[1;32m\nARQUIVO \033[1;33m"hashes.txt"\033[1;32m GERADO COM SUCESSO! PRESSIONE ENTER PARA CONTINUAR...\033[m')

    except:
        input('\033[1;31m\nOCORREU ALGUM PROBLEMA! PRESSIONE ENTER PARA CONTINUAR...\033[m')
# ========================================================================================================

# FUNÇÃO PARA COMPARA UM HASH DIGITADO OU UM ARQUIVO COM HASHES
def compara_hash(salt,senhas):
    controle = 0
    print()
    # SE O QUE FOI DADO ENTRADA FOR ARQUIVO ELE LÊ LINHA A LINHA E COMPARA COM O ARQUIVO GERADO NA FUNÇÃO ACIMA, LINHA A LINHA
    if os.path.exists(senhas):
        with open(senhas, "r") as senhas:
            for senha in senhas:
                with open("hashes.txt", "r") as hashes:
                    for hash in hashes:
                        if senha[0] == "$":
                            if senha[:-1] == hash.split("---")[0]:
                                print(f"\033[1;33mHash: \033[1;32m{senha[:-1]} \033[1;33m-> \033[1;32m{hash.split('---')[1]}\033[m")
                                controle = 1
                        else:
                            if salt+senha[:-1] == hash.split("---")[0]:
                                print(f"\033[1;33mHash: \033[1;32m{senha[:-1]} \033[1;33m--> \033[1;32m{hash.split('---')[1]}\033[m")
                                controle = 1

    # CASO O QUE FOI DADO ENTRADA FOR UM HASH ELE O COMPARA COM O ARQUIVO GERADO NA FUNÇÃO ACIMA, LINHA A LINHA
    else:
        with open("hashes.txt", "r") as hashes:
            for hash in hashes:
                if senhas[0] == "$":
                    if senhas == hash.split("---")[0]:
                        print(f"\033[1;33mHash: \033[1;32m{senhas} \033[1;33m---> \033[1;32m{hash.split('---')[1]}\033[m")
                        controle = 1
                else:
                    if salt+senhas == hash.split("---")[0]:
                        print(f"\033[1;33mHash: \033[1;32m{senhas} \033[1;33m----> \033[1;32m{hash.split('---')[1]}\033[m")
                        controle = 1
                                                                                                                        
    if controle == 0:
        print('\033[1;31m\nNENHUMA CORRESPONDÊNCIA!\033[m')

    input("PRESSIONE ENTER PARA CONTINUAR...")
# ========================================================================================================

# ===============SEÇÃO PRINCIPAL DO SCRIPT===============
escolha = 0

# LISTA COM AS OPÇÕES DO MENU PARA SER USADO NA CRIAÇÃO DO MESMO
menu = ['CRIPTOGRAFAR','DESCRIPTOGRAFAR','VISUALIZAR ARQUIVO "hashes.txt"','SAIR']

# LAÇO DO MENU NA TELA
while True:
    _ = os.system("clear")
    titulo("EXEMPLO DE CRIPTOGRAFIA E DESCRIPTOGRAFIA")

    # LAÇO PARA DESENHAR O MENU NA TELA
    for i in range(4):
        print('[ \033[1;{}m{}\033[m ] {}'.format(32,i+1,menu[i]))

    sys.stdout.write("\033[8;0H\033[1;33mESCOLHA UMA OPÇÃO (1 a 4): \033[m\033[8;28H")
    escolha = input('')
    try:
        if int(escolha) == 1:
            criptografa()
        elif int(escolha) == 2:
            descriptografa()
        elif int(escolha) == 3:
            visualizar()
        elif int(escolha) == 4:
            print('\033[1;32m\nOBRIGADO!\033[m')
            break
        else:
            print('\033[1;31m\nOPÇÃO INVÁLIDA!\033[m')
            sleep(2)
    except:
        print('\033[1;31m\nDIGITE APENAS NUMEROS!\033[m')
        escolha = 0
        sleep(2)
