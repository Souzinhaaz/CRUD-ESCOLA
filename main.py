from functions import *
import os

os.system("cls")
while True:
    opcao = menu_principal()
    os.system("cls")

    # A pessoa vai escolher a opção cadastrar
    if opcao == "1":
        parametro = menu_cadastro()
        os.system("cls")
        cadastrar(parametro)

    # A pessoa vai escolher a opção editar
    elif opcao == "2":
        parametro = menu_editar()
        os.system("cls")
        editar(parametro)

    elif opcao == "3":
        parametro = menu_remover()
        os.system("cls")
        remover(parametro)

    elif opcao == "0":
        os.system("cls")
        print("FIM DO PROGRAMA!!\n")
        break

