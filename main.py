from functions import *
import os

while True:
    menu()
    pergunta = input("")
    os.system("cls")

    if pergunta == "1":
        parametro = input(f"""{'-' * 15} Cadastro {'-' * 15}

1 - Cadastrar Turma
2 - Cadastrar Aluno
3 - Cadastrar Boletim
4 - Sair do cadastro

{'-' * 40}\n""") 
        os.system("cls")
        cadastrar(parametro)

    if pergunta == "0":
        os.system("cls")
        print("FIM DO PROGRAMA!!\n")
        break

