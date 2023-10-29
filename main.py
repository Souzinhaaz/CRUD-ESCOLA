from funções.functions import *
import os
from funções.cadastro import *
from funções.editar import *
from funções.remover import *
from funções.pesquisar import *
from funções.listar import *
from funções.relatorio import *


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

    elif opcao == "4":
        parametro = menu_pesquisar()
        os.system("cls")
        pesquisar(parametro)

    elif opcao == "5":
        parametro = menu_listar()
        os.system("cls")
        listar(parametro)

    elif opcao == "6":
        parametro = menu_relatorio()
        os.system("cls")
        relatorio(parametro)

    elif opcao == "0":
        os.system("cls")
        break

