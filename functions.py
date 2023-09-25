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
    
def verifica():
    if not os.path.exists("turmas.json"):
        with open("turmas.json", "w", encoding="utf-8") as arq:
            json.dump({}, arq)

    if not os.path.exists("alunos.json"):
        with open("alunos.json", "w", encoding="utf-8") as arq:
            json.dump({}, arq)

    if not os.path.exists("boletim.json"):
        with open("boletim.json", "w", encoding="utf-8") as arq:
            json.dump({}, arq)
    
# Cria a função para cadastrar
def cadastrar(parametro):
    # Cria os arquivos json se não existir
    verifica()

    # Abre os arquivos a serem usados
    with open("turmas.json", 'r+', encoding="utf-8") as turmas_json, open("alunos.json", "r+", encoding="utf-8") as alunos_json, open("boletim.json", 'r+', encoding="utf-8") as boletins_json:
        # Usuário escolhe a opção para cadastrar turma
        if parametro == "1":
            # a variavel nova_turma vai receber o dicionário que está no turmas_json
            nova_turma = json.load(turmas_json)

            print(f"{'-' * 15} Cadastro Turmas {'-' * 15}\n")

            # Vai pedir as informações do usuário e as verificar
            nome_turma = input("Digite o nome da turma: ")
            while True:
                if nome_turma in list(nova_turma.keys()):
                    print("Valor já existente, digite outro nome!\n")
                    nome_turma = input("Digite o nome da turma: ")
                else:
                    break 


            turno_turma = input("Digite o turno da sua turma [Matutino, Vespertino, Noturno e Integral]: ").capitalize()
            turnos = ["Matutino", "Vespertino", "Noturno", "Integral"]
            while True:
                if turno_turma not in turnos:
                    print("Turno inválido, digite um turno existente!!\n")
                    turno_turma = input("Digite o turno da sua turma [Matutino, Vespertino, Noturno e Integral]: ").capitalize()
                else:
                    break


            ano_turma = input("Digite o ano da turma(1-9): ")
            # Verifica se o ano da turma está correto
            while True:
                if int(ano_turma) not in range(1, 10):
                    print("Valor inválido, digite um ano entre (1 e 9): \n")
                    ano_turma = input("Digite o ano da turma(1-9): ")
                else:
                    ano_turma = ano_turma + "°"
                    break
            
            # Calculo para o id da turma
            id_turma = str(1+int(list(nova_turma.keys())[-1])) if len(nova_turma) > 0 else "1"  

            # Adiciona os dados em um dicionário
            nova_turma[id_turma] = {
                "Nome": nome_turma,
                "Turno": turno_turma,
                "Ano": ano_turma
            }

            # Interatividade do aplicativo
            print(f"Carregando...\n")

            # Adiciona os dados no turmas.json
            turmas_json.seek(0, 0)
            json.dump(nova_turma, turmas_json, indent=4)

            # Volta para a interatividade do site
            time.sleep(1)
            print("Turma Cadastrada com sucesso!!")
            time.sleep(1.5)
            os.system("cls")
                
        elif parametro == "2":
            # A variavel novo_aluno vai receber o dicionário que está no alunos_json e a nova_turma o que está em turmas_json
            novo_aluno = json.load(alunos_json)
            nova_turma = json.load(turmas_json)

            print(f"{'-' * 15} Cadastro Alunos {'-' * 15}\n")

            # Vai pedir as informações do aluno
            nome_aluno = input("Digite o nome do(a) aluno(a): ").capitalize()
            email_aluno = input("Digite o email do(a) aluno(a): ")
            telefone_aluno = input("Digite o telefone do(a) responsável do aluno(a): ")
            turma = input("Insira o código da turma: ")

            # Verifica se a turma existe no arquivo json
            if turma not in nova_turma:
                print("Turma inserida não existe no sistema, por favor insira outra!!")
                turma = input("Insira o código da turma: ") 

            matricula = str(1+int(list(novo_aluno.keys())[-1])) if len(novo_aluno) > 0 else "1"

            # Adiciona as informações do aluno no dicionário 
            novo_aluno[matricula] = {
                "Turma": nova_turma[turma]["Nome"],
                "Nome": nome_aluno,
                "Email": email_aluno,
                "Telefone": telefone_aluno,
            }

            # Interatividade do aplicativo
            print(f"Carregando...\n")

            # Adiciona os dados no alunos.json
            alunos_json.seek(0, 0)
            json.dump(novo_aluno, alunos_json, indent=4)

            # Volta para a interatividade do site
            time.sleep(1)
            print("Aluno(a) Cadastrado(a) com sucesso!!")
            time.sleep(1.5)
            os.system("cls")

        elif parametro == "3":
            # A variavel novo_boletim vai receber o dicionário que está no boletins_json e o novo_aluno o que está em alunos_json
            novo_boletim = json.load(boletins_json)
            novo_aluno = json.load(alunos_json)

            print(f"{'-' * 15} Cadastro Alunos {'-' * 15}\n")

            # Vai pedir o id do aluno referido
            id_aluno = input("Digite o numero de matricula do Aluno referido: ")

            # Vai guardar a quantidade de faltas na variável qnt_faltas
            qnt_faltas = int(input("Digite a quantidade de faltas do aluno inserido: "))

            # Vai guardar as notas do aluno em uma lista
            n1 = float(input("Digite a primeira nota do aluno inserido: "))
            n2 = float(input("Digite a segunda nota do aluno inserido: "))
            n3 = float(input("Digite a terceira nota do aluno inserido: "))
            n4 = float(input("Digite a quarta nota do aluno inserido: "))
            notas_aluno = [n1, n2, n3, n4]
            media = sum(notas_aluno) / len(notas_aluno)
            aprovado = True
            situacao = ""

            # Faz a verificação para saber se o aluno está aprovado ou não
            if media >= 7 and qnt_faltas < 15:
                aprovado = True
            else:
                aprovado = False
                
            if aprovado:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            # Faz a verificação para saber se o id do aluno existe no alunos_json
            if id_aluno not in novo_aluno:
                print("Aluno inserido não existe, por favor digite um existente.")
                id_aluno = input("Digite o número de matricula do Aluno referido: ")

            # Calculo para obter o novo id do boletim
            id_boletim = str(1+int(list(novo_boletim.keys())[-1])) if len(novo_boletim) > 0 else "1"
            
            novo_boletim[id_boletim] = {
                "Matrícula": id_aluno,
                "Nome": novo_aluno[id_aluno]["Nome"],
                "Turma": novo_aluno[id_aluno]["Turma"],
                "Notas": notas_aluno,
                "Quantidade de Faltas": qnt_faltas,
                "Situação": situacao
            } 





