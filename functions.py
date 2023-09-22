import json
import os
import time

# Cria o modelo do menu
def menu():
    print(f""" {'-' * 15} Escola {'-' * 15}

1 - Cadastrar
2 - Editar
3 - Remover
4 - Pesquisar
5 - Listar
6 - Gerar relatório
0 - Sair do programa
          
{'-' * 40}
""")
    
# Cria a função para cadastrar
def cadastrar():
    # Limpa o terminal
    os.system("cls")

    opcao = input(f""""{'-' * 15} Cadastro {'-' * 15}

1 - Cadastrar Turma
2 - Cadastrar Aluno
3 - Cadastrar Boletim

""")

    if opcao == "1":
        if not os.path.exists("turmas.json"):
            with open("turmas.json", "w") as turmas:
                id = 1
                while True:
                    nome_turma = input("Digite o nome da turma: ")
                    turno_turma = input("Digite o turno da sua turma: ")
                    ano_turma = input("Digite o ano da turma: ")

                    # Adiciona os dados no turmas.json
                    turmas[id] = {"Nome": nome_turma, "Turno": turno_turma, "Ano": ano_turma}
                    perg = input("Você quer cadastrar outra turma? Sim ou Não? ").upper()

                    if perg[0] == "S":
                        id += 1
                    else:
                        break

        else:
            id = 2
            while True:
                nome_turma = input("Digite o nome da turma: ")
                turno_turma = input("Digite o turno da sua turma: ")
                ano_turma = input("Digite o ano da turma: ")

                # Adiciona os dados no turmas.json
                turmas[id] = {"Nome": nome_turma, "Turno": turno_turma, "Ano": ano_turma}
                perg = input("Você quer cadastrar outra turma? Sim ou Não? ").upper()

                if perg[0] == "S":
                    id += 1
                else:
                    break



