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
    
    print(f"{'-' * 15} Cadastro {'-' * 15}")
    nome_turma = input("Digite o nome da turma: ")
    
    if not os.path.exists("turmas.json"): 
        with open("turmas.json", "w") as turmas:
            json.dump(nome_turma, "turmas.json")
    


