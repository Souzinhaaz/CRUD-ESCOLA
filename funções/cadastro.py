import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from functions import *

# Cria a função para cadastrar
def cadastrar(parametro):
    while True:
        # Cria os arquivos json se não existir
        verifica()

        # Abre os arquivos a serem usados
        nova_turma, novo_aluno, novo_boletim = abrirArquivos()
        # Usuário escolhe a opção para cadastrar turma
        if parametro == "1":
            # a variavel nova_turma vai receber o dicionário que está no turmas_json

            print(f"{'-' * 15} Cadastro Turmas {'-' * 15}\n")

            # Vai pedir as informações do usuário e as verificar
            nome_turma = input("Digite o nome da turma: ")
            while True:
                if nome_turma in nova_turma.keys():
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
            print("Carregando...\n")

            # Vai guardar a turma
            guardarTurma(nova_turma)

            # Volta para a interatividade do site
            time.sleep(1)
            print("Turma Cadastrada com sucesso!!")
            time.sleep(1.5)
            os.system("cls")
            parametro = menu_cadastro()
            os.system("cls")
                
        # Usuário vai cadastrar um aluno
        elif parametro == "2":
            # Verifica se existe alguma turma
            if len(nova_turma) > 0:
                # A variavel novo_aluno vai receber o dicionário que está no alunos_json e a nova_turma o que está em turmas_json

                print(f"{'-' * 15} Cadastro Alunos {'-' * 15}\n")

                # Vai pedir as informações do aluno
                nome_aluno = input("Digite o nome do(a) aluno(a): ").title()
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

                novo_boletim[matricula] = {}

                # Interatividade do aplicativo
                print("Carregando...\n")

                # Vai guardar os dados de alunos e boletins
                guardarAluno(novo_aluno)
                guardarBoletim(novo_boletim)
                
                # Volta para a interatividade do site
                time.sleep(1)
                print("Aluno(a) Cadastrado(a) com sucesso!!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_cadastro()
                os.system("cls")
                    
            else:
                os.system("cls")
                print("\nPor favor, crie uma turma primeiro! ")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_cadastro()
                os.system("cls")
            
        # Cadastrar o boletim
        elif parametro == "3":
            # Verifica se o json de alunos esta vazio e se o id referido está dentro do alunos_json
            if len(novo_aluno) > 0:
                # Vai pedir o codigo de matricula do aluno referido
                codigo = input("Digite o código de matrícula do Aluno referido: ")
                if codigo in novo_aluno:
                    if not novo_boletim.get(codigo):

                        # Vai guardar a quantidade de faltas na variável qnt_faltas
                        qnt_faltas = int(input("Digite a quantidade de faltas do aluno inserido: "))
                        os.system("cls")

                        # Vai guardar as notas do aluno em uma lista
                        notas_aluno = []
                        for i in range(1, 5):
                            nota = float(input(f"Digite a {i}a nota: "))
                            notas_aluno.append(nota)
                        
                        media = sum(notas_aluno) / len(notas_aluno)
                        aprovado = True

                        # Faz a verificação para saber se o aluno está aprovado ou não
                        if media >= 7 and qnt_faltas < 15:
                            aprovado = True
                        else:
                            aprovado = False
                            
                        if aprovado:
                            situacao = "Aprovado"
                        else:
                            situacao = "Reprovado"
                        
                        novo_boletim[codigo] = {
                            "Nome": novo_aluno[codigo]["Nome"],
                            "Turma": novo_aluno[codigo]["Turma"],
                            "Notas": notas_aluno,
                            "Média": media,
                            "Quantidade de Faltas": qnt_faltas,
                            "Situação": situacao
                        } 

                        print("Carregando...\n")

                        # Vai guardar o novo boletim
                        guardarBoletim(novo_boletim)

                        # Volta para a interatividade do site
                        time.sleep(1)
                        print("Boletim Cadastrado com sucesso!!")
                        time.sleep(1.5)
                        os.system("cls")
                        parametro = menu_cadastro()
                        os.system("cls")
                    
                    else:
                        print("Aluno já possui um boletim, por favor selecione outro aluno, ou remova esse")
                        time.sleep(1.5)
                        os.system("cls")
                        parametro == menu_cadastro()
                        os.system("cls")

                else:
                    print("Aluno referido não existe no sistema, por favor cadastre")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_cadastro()
                    os.system("cls")

            else:
                print("\nPara cadastrar boletim é necessário ao menos um aluno e uma turma")
                time.sleep(2)
                os.system("cls")
                parametro = menu_cadastro()
                os.system("cls")

        elif parametro == "4":
            os.system("cls")
            break

        else:
            print("Valor inválido! ")
            time.sleep(1)
            os.system("cls")
            parametro = menu_cadastro()
            os.system("cls")