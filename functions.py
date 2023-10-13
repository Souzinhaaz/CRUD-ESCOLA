import json
import os
import time

# Cria o modelo do menu principal
def menu_principal():
    pergunta = input(f""" {'-' * 15} Escola {'-' * 15}

1 - Cadastrar
2 - Editar
3 - Remover
4 - Pesquisar
5 - Listar
6 - Gerar relatório
0 - Sair do programa
          
{'-' * 40}
""")
    return pergunta

def menu_creditos():
    print(f"""FIM DO PROGRAMA!!!
    
AUTOR: GUSTAVO DE SOUZA OLIVEIRA
DURAÇÃO DO PROJETO: 2 MÊSES 

OFERECIMENTO: 

IF BAIANO
VALDEMIR TAE KWON
FATINHA
FÁBIO NUNES
EURES RIBEIRO
DELAVÊGA
PETELECO LANCHES
EDSON DO ESPETINHO
CHICO DO BREGA
TONIN BOGUÉ
CADINHA
ABRAÃO FAZ O A
ANDRE PIKA DE ASSOVIO
LEO DO ACARAJE
BENVINDO DA BARBEARIA
GILSON(VAI ACOMPANHAR BENVINDO)
D2 BOMBEIRO

""")

# Cria o modelo do menu cadastro
def menu_cadastro():
    parametro = input(f"""{'-' * 15} Cadastro {'-' * 15}

1 - Cadastrar Turma
2 - Cadastrar Aluno
3 - Cadastrar Boletim
4 - Sair 

{'-' * 40}\n""") 
    return parametro
    
# Cria o modelo do menu editar
def menu_editar():
    parametro = input(f"""{'-' * 15} Editar {'-' * 15}

1 - Editar Turma
2 - Editar Aluno
3 - Editar Boletim
4 - Sair 

{'-' * 40}\n""")
    return parametro

# Cria o modelo do menu remover
def menu_remover():
    parametro = input(f"""{'-' * 15} Remover {'-' * 15}

1 - Remover Turma
2 - Remover Aluno
3 - Remover Boletim
4 - Sair 

{'-' * 40}\n""")
    return parametro

# Cria o modelo do menu pesquisar
def menu_pesquisar():
    parametro = input(f"""{'-' * 15} Pesquisar {'-' * 15}

1 - Pesquisar Turma
2 - Pesquisar Aluno
3 - Pesquisar Boletim
4 - Sair 

{'-' * 40}\n""")
    return parametro

def menu_listar():
    parametro = input(f"""{'-' * 15} Listar {'-' * 15}

1 - Listar Turmas
2 - Listar Alunos por Turma
3 - Listar Alunos e Boletins por Turma
4 - Listar Alunos Aprovados e Boletins por Turma
5 - Listar Alunos Reprovados e Boletins por Turma
6 - Sair

{'-' * 40}\n""")
    return parametro

def menu_relatorio():
    parametro = input(f"""{'-' * 15} Relatório {'-' * 15}

1 - Total de Turmas
2 - Total de Alunos, por Turma
3 - Total de Alunos Aprovados e Reprovados, por Turma
4 - Maiores e menores médias, por turma
5 - Total de Alunos com faltas acima e abaixo do limite, por Turma
6 - Sair

{'-' * 40}\n""")
    return parametro

def lisTurma(i):
    turma = abrirTurmas()

    print(f"\n\033[31m{'-=' * 30}\033[m")
    print(f"""\n{'=' * 15} {turma[i]["Nome"]} {'=' * 15}
{'-' * 40}

ID: {int(i)}

Turno: {turma[i]["Turno"]}

Ano: {turma[i]["Ano"]}

{'-' * 40}
""")

def lisAlunos(i):
    aluno = abrirAlunos()
    print(f"\n\033[31m{'-=' * 30}\033[m")
    print(f"""\n{'-' * 15} {aluno[i]["Nome"]} - {aluno[i]["Turma"]} {'-' * 15}

ID Aluno: {int(i)}

Email: {aluno[i]["Email"]}

Telefone: {aluno[i]["Telefone"]}

{'-' * 40}
""")

def lisAlunosBoletim(i):
    aluno = abrirAlunos()
    boletim = abrirBoletins()

    if boletim.get(str(i)):
        print(f"\n\033[31m{'-=' * 30}\033[m")
        print(f"""\n{'-' * 15} {aluno[i]["Nome"]} - {aluno[i]["Turma"]} {'-' * 15}

ID Aluno: {int(i)}

Email: {aluno[i]["Email"]}

Telefone: {aluno[i]["Telefone"]}

{'-' * 15} Boletim {'-' * 15}

Notas: {boletim[i]["Notas"]}

Quantidade de Faltas: {boletim[i]["Quantidade de Faltas"]}

Situação: {boletim[i]["Situação"]}

{'-' * 40}
""")
    else:
        print(f"\n\033[31m{'-=' * 30}\033[m")
        print(f"""\n{'-' * 15} {aluno[i]["Nome"]} - {aluno[i]["Turma"]} {'-' * 15}

ID Aluno: {int(i)}

Email: {aluno[i]["Email"]}

Telefone: {aluno[i]["Telefone"]}

{'-' * 15} Boletim {'-' * 15}

Vazio

{'-' * 40}
""")

# Funções para retornar modelo de pesquisas
def rturma(i, parametro):
    turma = abrirTurmas()

    print(f""" {'=' * 15} {turma[parametro]["Nome"]} {'=' * 15}
{'-' * 40}

ID: {int(parametro)}

Turno: {turma[parametro]["Turno"]}

Ano: {turma[parametro]["Ano"]}

{'-' * 40}
""")

def raluno(i, parametro):
    aluno = abrirAlunos()

    print(f""" {'=' * 15} {aluno[parametro]["Nome"]} {'=' * 15}
{'-' * 40}

ID: {int(parametro)}

Turma: {aluno[parametro]["Turma"]}

Email: {aluno[parametro]["Email"]}

Telefone: {aluno[parametro]["Telefone"]}

{'-' * 40}
""")
    
def rboletim(i, parametro):
    aluno = abrirAlunos()
    boletim = abrirBoletins()

    if boletim.get(str(parametro)):
        print(f""" {'=' * 15} PROPRIETÁRIO DO BOLETIM: {aluno[parametro]["Nome"]} {'=' * 15}
{'-' * 40}

Código do aluno: {int(parametro)}

{'-' * 15} BOLETIM {'-' * 15}

Turma: {aluno[parametro]["Turma"]}

Notas: {boletim[parametro]["Notas"]}

Média: {boletim[parametro]["Média"]}

Quantidade de Faltas: {boletim[parametro]["Quantidade de Faltas"]}

Situação: {boletim[parametro]["Situação"]}

{'-' * 40}
""")
    else:
        print(f""" {'=' * 15} PROPRIETÁRIO DO BOLETIM: {aluno[parametro]["Nome"]} {'=' * 15}
{'-' * 40}

Código do aluno: {int(parametro)}

{'-' * 15} BOLETIM {'-' * 15}

Vazio

{'-' * 40}
""")
    
# Função para verificar se existe os arquivos necessários e cria-los
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

# Função para abrir os arquivos
def abrirArquivos():
    with open("turmas.json", "r+", encoding="utf-8") as turmas_json, open("alunos.json", "r+", encoding="utf-8") as alunos_json, open("boletim.json", "r+", encoding="utf-8") as boletins_json:
        turma = json.load(turmas_json)
        aluno = json.load(alunos_json)
        boletim = json.load(boletins_json)
    return turma, aluno, boletim

def abrirTurmas():
    with open("turmas.json", "r", encoding="utf-8") as turmas_json:
        turma = json.load(turmas_json)
    return turma

def abrirAlunos():
    with open("alunos.json", "r", encoding="utf-8") as alunos_json:
        aluno = json.load(alunos_json)
    return aluno

def abrirBoletins():
    with open("boletim.json", "r", encoding="utf-8") as boletins_json:
        boletim = json.load(boletins_json)
    return boletim
        
def guardarTurma(guardar):
    with open("turmas.json", "w", encoding="utf-8") as turmas_json:
        turmas_json.seek(0, 0)
        json.dump(guardar, turmas_json, indent=4)

def guardarAluno(guardar):
    with open("alunos.json", "w", encoding="utf-8") as alunos_json:
        alunos_json.seek(0, 0)
        json.dump(guardar, alunos_json, indent=4)

def guardarBoletim(guardar):
    with open("boletim.json", "w", encoding="utf-8") as boletins_json:
        boletins_json.seek(0, 0)
        json.dump(guardar, boletins_json, indent=4)


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

# Função para editar
def editar(parametro):
    verifica()

    # Loop para não sair da opção de parametro
    while True:
        turmas, alunos, boletins = abrirArquivos()

        # Usuário escolhe a opção de editar as turmas
        if parametro == "1":
            # Verificar se existe algum valor no arquivo
            if len(turmas) > 0:
                print(f"""{'-' * 15} Edição {'-' * 15}\n""")

                # Vai pedir o código da turma desejada
                codigo = input("Digite o código da turma que você deseja editar: ")
                os.system("cls")

                if codigo in turmas:
                    print(f"""{'-' * 15} Edição {'-' * 15}""")
                    pergunta = input("\nOque você deseja mudar [Nome, Turno ou Ano]: ")

                    # Se a pessoa desejar mudar o nome
                    if pergunta.upper() == "NOME":
                        print(f"\n{turmas[codigo]['Nome']}\n")

                        pergunta = input("Essa é a turma que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_nome = input("\nDigite o novo nome: ")
                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                turmas[codigo]["Nome"] = novo_nome

                                guardarTurma(turmas)
                                print("\nNovo nome registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break

                            else:   
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")
                        
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    # Se a pessoa desejar mudar o turno
                    elif pergunta.upper() == "TURNO":
                        print(f"\n{turmas[codigo]['Turno']}\n")

                        pergunta = input("Esse é o turno que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_turno = input("\nDigite o novo turno: ")

                            # Verificar se o turno é válido
                            turnos = ["Matutino", "Vespertino", "Noturno", "Integral"]
                            while True:
                                if novo_turno not in turnos:
                                    print("Turno inválido, digite um turno existente!!\n")
                                    novo_turno = input("Digite o turno da sua turma [Matutino, Vespertino, Noturno e Integral]: ").capitalize()
                                else:
                                    break

                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                turmas[codigo]["Turno"] = novo_turno

                                guardarTurma(turmas)
                                print("\nNovo turno registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")  
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    # Se a pessoa desejar mudar o ano
                    elif pergunta.upper() == "ANO":
                        print(f"\n{turmas[codigo]['Ano']}\n")

                        pergunta = input("Esse é o ano que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_ano = input("\nDigite o novo ano: ")

                            # Verifica se o ano da turma está correto
                            while True:
                                if int(novo_ano) not in range(1, 10):
                                    print("Valor inválido, digite um ano entre (1 e 9): \n")
                                    novo_ano = input("Digite o ano da turma(1-9): ")
                                else:
                                    novo_ano = novo_ano + "°"
                                    break

                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                turmas[codigo]["Ano"] = novo_ano

                                guardarBoletim(turmas)
                                print("\nNovo ano registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    else:
                        print("Valor informado não existe")
                        time.sleep(2)     
                        os.system("cls")      
                        parametro = menu_editar()
                        os.system("cls")     
                else:
                    print("O código informado não existe! ")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")
            else:
                print("Nenhum valor cadastrado na turma, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        # Usuário escolhe a opção de editar os alunos
        elif parametro == "2":      
            # Verificar se existe algum valor no arquivo
            if len(alunos) > 0:
                print(f"{'-' * 15} Editar {'-' * 15}\n")

                codigo = input("Digite o código do aluno que você deseja editar: ")
                os.system("cls")

                if codigo in alunos:
                    print(f"""{'-' * 15} Edição {'-' * 15}""")
                    pergunta = input("\nOque você deseja mudar [Nome, Email, Telefone ou Turma?]: ")

                    if pergunta.upper() == "NOME":
                        print(f"\n{alunos[codigo]['Nome']}\n")

                        pergunta = input("Esse é o nome que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_nome = input("\nDigite o novo nome: ").title()
                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                for i in boletins:
                                    if boletins[i]["Nome"] == alunos[codigo]["Nome"]:
                                        boletins[i]["Nome"] = novo_nome
                                alunos[codigo]["Nome"] = novo_nome
                                
                                guardarAluno(alunos)
                                guardarBoletim(boletins)
                                print("\nNovo nome registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                            
                            break

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "EMAIL":
                        print(f"\n{alunos[codigo]['Email']}\n")

                        pergunta = input("Esse é o email que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_email = input("\nDigite o novo email: ")
                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                alunos[codigo]["Email"] = novo_email

                                guardarAluno(alunos)
                                print("\nNovo email registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                break

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "TELEFONE":
                        print(f"\n{alunos[codigo]['Telefone']}\n")

                        pergunta = input("Esse é o telefone que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_telefone = input("\nDigite o novo telefone: ")
                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                alunos[codigo]["Telefone"] = novo_telefone

                                guardarAluno(alunos)
                                print("\nNovo telefone registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                break

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")    

                    elif pergunta.upper() == "TURMA":
                        print(f"\n{alunos[codigo]['Turma']}\n")

                        pergunta = input("Essa é a turma que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            nova_turma = input("\nDigite o nome da nova turma: ")

                            existe = False
                            for turma in turmas:
                                if nova_turma == turmas[turma]["Nome"]:
                                    existe = True

                            if existe:
                                pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                if pergunta[0].upper() == "S":
                                    alunos[codigo]["Turma"] = nova_turma
                                    boletins[codigo]["Turma"] = nova_turma

                                    guardarAluno(alunos)
                                    guardarBoletim(boletins)
                                    print("\nNova turma registrada com sucesso!!")
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                                else:
                                    os.system("cls")
                                    parametro = menu_editar()
                                    os.system("cls")
                            else:
                                print("Essa turma não existe!!\n")
                                time.sleep(1.5)
                                os.system("cls")
                                print("Por favor crie uma turma")
                                time.sleep(1.5)
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")   

                    else:
                        print("Valor inválido")
                        time.sleep(2)
                        os.system("cls")
                        parametro = menu_editar()
                        os.system("cls")

                else:
                    print("Esse código não existe!! Cadastre o aluno(a) primeiro!!")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")

            else:
                print("Nenhum valor cadastrado em alunos, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")
            
        # Usuário escolhe a opção de editar os boletins
        elif parametro == "3":
            
            # Verificar se existe algum valor no arquivo
            if len(boletins) > 0:
                print(f"{'-' * 15} Editar {'-' * 15}\n")

                codigo = input("Digite o código do boletim que você deseja editar: ")
                os.system("cls")

                if codigo in boletins:
                    print(f"""{'-' * 15} Edição {'-' * 15}""")
                    pergunta = input("\nOque você deseja mudar [NOME, TURMA, NOTAS, FALTA ou SITUAÇÃO?]: ")

                    if pergunta.upper() == "NOME":
                        print(f"\n{boletins[codigo]['Nome']}\n")

                        pergunta = input("Esse é o nome que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            novo_nome = input("\nDigite o novo nome: ")
                            pergunta = input("\nSe mudar o nome do boletim vai mudar o do aluno também, tem certeza que deseja editar? Sim ou Não? ")

                            if pergunta[0].upper() == "S":
                                alunos[codigo]["Nome"] = novo_nome
                                boletins[codigo]["Nome"] = novo_nome

                                guardarBoletim(boletins)
                                guardarAluno(alunos)
                                print("\nNovo nome registrado com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                break
                            
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "TURMA":
                        print(f"\n{boletins[codigo]['Turma']}\n")
                        pergunta = input("Essa é a turma que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            nova_turma = input("\nDigite a nova turma: ")

                            existe = False
                            for turma in turmas:
                                if nova_turma == turmas[turma]["Nome"]:
                                    existe = True

                            if existe:
                                pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                if pergunta[0].upper() == "S":
                                    boletins[codigo]["Turma"] = nova_turma
                                    alunos[codigo]["Turma"] = nova_turma

                                    guardarBoletim(boletins)
                                    guardarAluno(alunos)
                                    print("\nNova turma registrada com sucesso!!")
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                                else:
                                    os.system("cls")
                                    parametro = menu_editar()
                                    os.system("cls")
                            else:
                                print("Essa turma não existe!!\n")
                                time.sleep(1.5)
                                os.system("cls")
                                print("Por favor crie uma turma")
                                time.sleep(1.5)
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "NOTAS":
                        print(f"\n{boletins[codigo]['Notas']}\n")

                        pergunta = input("Essa são as notas que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            notas_aluno = []
                            for i in range(1, 5):
                                nota = float(input(f"Digite a {i}a nota: "))
                                notas_aluno.append(nota)

                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                boletins[codigo]["Notas"] = notas_aluno
                                boletins[codigo]["Média"] = sum(notas_aluno) / len(notas_aluno)

                                guardarBoletim(boletins)
                                print("Novas notas registradas com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break   
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "FALTA":
                        print(f"\n{boletins[codigo]['Quantidade de Faltas']}\n")

                        pergunta = input("Essa são as faltas que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            
                            faltas_nova = int(input("Digite a nova quantidade de faltas do aluno inserido: "))

                            pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                            if pergunta[0].upper() == "S":
                                boletins[codigo]["Quantidade de Faltas"] = faltas_nova

                                guardarBoletim(boletins)
                                print("\nNovas faltas registradas com sucesso!!")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")
                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    elif pergunta.upper() == "SITUAÇÃO" or pergunta.upper() == "SITUACAO":
                        print(f"\n{boletins[codigo]['Situação']}\n")

                        pergunta = input("Essa é a situação que deseja editar? Sim ou Não? ")

                        if pergunta[0].upper() == "S":
                            os.system("cls")
                            print(f"""{'-' * 15} Edição {'-' * 15}""")
                            
                            nova_situacao = input("Qaul a sitação do aluno, Aprovado ou Reprovado? ")

                            if nova_situacao.upper() == "APROVADO" or nova_situacao.upper() == "REPROVADO":

                                pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                if pergunta[0].upper() == "S":
                                    boletins[codigo]["Situação"] = nova_situacao

                                    guardarBoletim(boletins)
                                    print("\nNova situação registrado com sucesso!!")
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                                else:
                                    os.system("cls")
                                    parametro = menu_editar()
                                    os.system("cls")
                            else:
                                print("Valor inválido!")
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                        else:
                            os.system("cls")
                            pergunta = input("Quer tentar outro código? ")
                            if pergunta[0].upper() == "S":
                                os.system("cls")
                            else:
                                os.system("cls")
                                parametro = menu_editar()
                                os.system("cls")

                    else:
                        print("Valor informado não existe")
                        time.sleep(2)     
                        os.system("cls")
                        parametro = menu_editar()
                        os.system("cls")

                else:
                    print("Esse código não existe!! Cadastre o boletim primeiro!!")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")

            else:
                print("Nenhum valor cadastrado em boletins, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        elif parametro == "4":
            os.system("cls")
            break

        else:
            print("Valor inválido!")
            time.sleep(1)
            os.system("cls")
            parametro = menu_editar()
            os.system("cls")
        
def remover(parametro):
    verifica()

    # Loop para não sair da opção de parametro
    while True:
        turma, aluno, boletim = abrirArquivos()
        # Se o usuário escolher remover turma
        if parametro == "1": 
            if len(turma) > 0:
                codigo = input("Digite o código da turma que você deseja remover: ")

                if codigo in turma:
                    print(f"\n{turma[codigo]}\nEssa é a turma que você selecionou\n")
                    pergunta = input("Você tem certeza que deseja excluir? Sim ou Não? ")

                    if pergunta[0].upper() == "S":
                        if len(turma) > 1:

                            # Se for o ultimo dicionário vai remover
                            if int(codigo) == len(turma):
                                # Obtém o nome da turma que será removida
                                nome_turma_removida = turma[codigo]["Nome"]

                                # Remove todos os alunos com o mesmo nome da turma removida
                                alunos_para_remover = []
                                for id_alunos, dados_aluno in aluno.items():
                                    if dados_aluno["Turma"] == nome_turma_removida:
                                        alunos_para_remover.append(id_alunos)

                                # Remove os alunos do dicionário de alunos
                                for id_aluno in alunos_para_remover:
                                    del aluno[id_aluno]
                                
                                novo_aluno = {}
                                contador = 1
                                # Itere sobre o dicionário original e reorganize as chaves
                                for chave, valor in sorted(aluno.items()):
                                    novo_aluno[str(contador)] = valor
                                    contador += 1
                                
                                del turma[codigo]

                                guardarTurma(turma)
                                guardarAluno(novo_aluno)
                                print("\nTurma removida com sucesso!")
                                time.sleep(2)
                                os.system("cls")
                                break

                            # Obtém o nome da turma que será removida
                            nome_turma_removida = turma[codigo]["Nome"]

                            # Remove todos os alunos com o mesmo nome da turma removida
                            alunos_para_remover = []
                            for id_alunos, dados_aluno in aluno.items():
                                if dados_aluno["Turma"] == nome_turma_removida:
                                    alunos_para_remover.append(id_alunos)

                            # Remove os alunos do dicionário de alunos
                            for id_aluno in alunos_para_remover:
                                del aluno[id_aluno]

                            novo_aluno = {}
                            contador = 1
                            # Itere sobre o dicionário original e reorganize as chaves
                            for chave, valor in sorted(aluno.items()):
                                novo_aluno[str(contador)] = valor
                                contador += 1   

                            # Código para reescrever o código digitado pelo seu sucessor
                            turma[codigo] = turma.pop(str(int(codigo) + 1)) # Reescrever no código deletado o dicionário que estava a frente

                            for i in range(1, len(turma) + 1): # Vai percorrer todos os dicionários na turma
                                if str(i) in turma:
                                    turma[str(i)] = turma[str(i)]
                                else:
                                    turma[str(i)] = turma.pop(str(i + 1))
                        
                            guardarTurma(turma)
                            guardarAluno(novo_aluno)
                            print("\nTurma removida com sucesso!")
                            time.sleep(2)
                            os.system("cls")
                            break              
                        else:
                            # Obtém o nome da turma que será removida
                            nome_turma_removida = turma[codigo]["Nome"]

                            # Remove todos os alunos com o mesmo nome da turma removida
                            alunos_para_remover = []
                            for id_alunos, dados_aluno in aluno.items():
                                if dados_aluno["Turma"] == nome_turma_removida:
                                    alunos_para_remover.append(id_alunos)

                            # Remove os alunos do dicionário de alunos
                            for id_aluno in alunos_para_remover:
                                del aluno[id_aluno]

                            novo_aluno = {}
                            contador = 1
                            # Itere sobre o dicionário original e reorganize as chaves
                            for chave, valor in sorted(aluno.items()):
                                novo_aluno[str(contador)] = valor
                                contador += 1
                            
                            guardarAluno(novo_aluno)
                            with open("turmas.json", "w", encoding="utf-8") as turmas_json:
                                json.dump({}, turmas_json)
                                print("\nTurma removida com sucesso!")
                                time.sleep(2)
                                os.system("cls")
                                break      
                    else:
                        os.system("cls")
                        parametro = menu_remover()
                        os.system("cls")

                else:
                    os.system("cls")
                    print("Nenhuma turma com esse código, por favor, crie uma!")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_remover()
                    os.system("cls")

            else:
                print("Nenhum valor cadastrado em turmas, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")
                        
        # Se o usuário escolher remover alunos
        elif parametro == "2":
            if len(aluno) > 0:
                codigo = input("Digite o código do(a) aluno(a) que você deseja remover: ")

                if codigo in aluno:
                    print(f"\n{aluno[codigo]}\nEsse foi o aluno que você selecionou\n")
                    pergunta = input("Você tem certeza que quer excluir? Sim ou Não? ")
                    if pergunta[0].upper() == "S":
                        # Se tiver mais de um aluno no dicionário
                        if len(aluno) > 1:

                            # Se for o último dicionário vai remover
                            if int(codigo) == len(aluno):
                                # Obtém o nome do aluno que será removido
                                nome_aluno_removido = aluno[codigo]["Nome"]

                                # Remove todos os boletins com o mesmo nome da turma removida
                                boletins_para_remover = []
                                for id_boletins, dados_boletins in boletim.items():
                                    if boletim[id_boletins].get("Matrícula"):
                                        if dados_boletins["Matrícula"] == nome_aluno_removido:
                                            boletins_para_remover.append(id_boletins)
                                    else:
                                        continue

                                # Remove os boletins do dicionário de boletins
                                for id_boletim in boletins_para_remover:
                                    boletim[id_boletim] = {}

                                del aluno[codigo]

                                guardarAluno(aluno)
                                guardarBoletim(boletim)
                                print("\nAluno(a) removido(a) com sucesso!")
                                time.sleep(2)
                                os.system("cls")
                                break

                            # Obtém o nome do aluno que será removido
                            nome_aluno_removido = aluno[codigo]["Nome"]

                            # Remove todos os boletins com o mesmo nome da turma removida
                            boletins_para_remover = []
                            for id_boletins, dados_boletins in boletim.items():
                                if boletim[id_boletins].get("Matrícula"):
                                    if dados_boletins["Matrícula"] == nome_aluno_removido:
                                        boletins_para_remover.append(id_boletins)
                                else:
                                    continue

                            # Remove os boletins do dicionário de boletins
                            for id_boletim in boletins_para_remover:
                                boletim[id_boletim] = {}

                            # Código para reescrever o código digitado pelo seu sucessor
                            aluno[codigo] = aluno.pop(str(int(codigo) + 1)) # Reescrever no código deletado o dicionário que estava a frente

                            for i in range(1, len(aluno) + 1): # Vai percorrer todos os dicionários no aluno
                                if str(i) in aluno:
                                    aluno[str(i)] = aluno[str(i)]
                                else:
                                    aluno[str(i)] = aluno.pop(str(i + 1))

                            guardarAluno(aluno)
                            guardarBoletim(boletim)    
                            print("\nAluno(a) removido(a) com sucesso!")
                            time.sleep(2)
                            os.system("cls")
                            break

                        # Se tiver apenas 1 aluno no dicionário
                        else:
                            # Obtém o nome do aluno que será removido
                            nome_aluno_removido = aluno[codigo]["Nome"]

                            # Remove todos os boletins com o mesmo nome da turma removida
                            boletins_para_remover = []
                            for id_boletins, dados_boletins in boletim.items():
                                if boletim[id_boletins].get("Matrícula"):
                                    if dados_boletins["Matrícula"] == nome_aluno_removido:
                                        boletins_para_remover.append(id_boletins)
                                else:
                                    continue

                            # Remove os boletins do dicionário de boletins
                            for id_boletim in boletins_para_remover:
                                boletim[id_boletim] = {}

                            guardarBoletim(boletim)
                            with open("alunos.json", "w", encoding="utf-8") as alunos_json:
                                json.dump({}, alunos_json)    
                                print("\nAluno removido com sucesso!")
                                time.sleep(2)
                                os.system("cls")
                                break
                    else:
                        os.system("cls")
                        parametro = menu_remover()
                        os.system("cls")
                
                else:
                    os.system("cls")
                    print("Nenhum aluno(o) com esse código, por favor, crie um(a)!")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_remover()
                    os.system("cls")

            else:
                print("Nenhum valor cadastrado em alunos, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        # Se o usuário esolher remover boletim
        elif parametro == "3":
            if len(boletim) > 0:
                codigo = input("Digite o código do boletim que deseja remover: ")

                if codigo in boletim:
                    print(f"\n{boletim[codigo]}\nEsse foi o boletim que você selecionou\n")
                    pergunta = input("Você tem certeza que quer excluir? Sim ou Não? ")
                    if pergunta[0].upper() == "S":
                        
                        boletim[codigo] = {}

                        guardarBoletim(boletim)
                        print("\nBoletim removido com sucesso!")
                        time.sleep(2)
                        os.system("cls")
                        break
                        
                    else:
                        os.system("cls")
                        parametro = menu_remover()
                        os.system("cls")

                else:
                    os.system("cls")
                    print("Nenhum boletim com esse código, por favor, crie um!")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_remover()
                    os.system("cls")

            else:
                print("Nenhum valor cadastrado em boletins, por favor cadastrar!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        elif parametro == "4":
            os.system("cls")
            break

        else:
            print("Valor inválido!")
            time.sleep(1)
            os.system("cls")
            parametro = menu_remover()
            os.system("cls")

def pesquisar(parametro):
    verifica()
    while True:
        turma, alunos, boletim = abrirArquivos()
        # Loop para não sair da função
        if parametro == "1":
            if os.path.exists("turmas.json"):
                os.system("cls")
                if len(turma) > 0:
                    opcao = input("Como você quer pesquisar a turma? pelo código, nome, turno, ano ou sair? ")
                    os.system("cls")

                    # Usuário seleciona pelo código
                    if opcao.upper() == "CÓDIGO" or opcao.upper() == "CODIGO":
                        codigo = input("\nDigite o código da turma: ")
                        os.system("cls")
                        if codigo in turma:
                            for i in turma:
                                rturma(i, codigo)
                                break

                            pergunta = input("\nDeseja pesquisar outra turma? Sim ou Não? ")
                            if pergunta[0].upper() == "N":
                                os.system("cls")
                                parametro = menu_pesquisar()
                                os.system("cls")
                        else:
                            print("O código inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")

                    elif opcao.upper() == "NOME":
                        nome = input("\nDigite o nome da turma:")
                        os.system("cls")

                        for i in turma:
                            if nome.upper() == turma[str(i)]["Nome"].upper():
                                existe = True
                                break
                            else:
                                existe = False

                        if existe:
                            for i in turma:
                                if nome.upper() == turma[str(i)]["Nome"].upper():
                                    codigo = str(i)
                                    rturma(i, codigo)
                        else:
                            print("O nome inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")    

                        pergunta = input("\nDeseja pesquisar outra turma? Sim ou Não? ")
                        if pergunta[0].upper() == "N":
                            os.system("cls")
                            parametro = menu_pesquisar()
                            os.system("cls")       

                    elif opcao.upper() == "TURNO":
                        turno = input("Digite o turno da sua turma: ")        
                        os.system("cls")

                        for i in turma:
                            if turno.upper() == turma[str(i)]["Turno"].upper():
                                existe = True
                                break
                            else:
                                existe = False
                            
                        if existe:
                            for i in turma:
                                if turno.upper() == turma[str(i)]["Turno"].upper():
                                    codigo = str(i)
                                    rturma(i, codigo)
                        else:
                            print("O turno inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")

                        pergunta = input("\nDeseja pesquisar outra turma? Sim ou Não? ")
                        if pergunta[0].upper() == "N":
                            os.system("cls")
                            parametro = menu_pesquisar()
                            os.system("cls")
                            
                    elif opcao.upper() == "ANO":
                        ano = input("Digite o ano da sua turma: ")
                        os.system("cls")

                        for i in turma:
                            if ano == turma[str(i)]["Ano"][0]:
                                existe = True
                            else:
                                existe = False
                        
                        if existe:
                            for i in turma:
                                if ano == turma[str(i)]["Ano"][0]:
                                    codigo = str(i)
                                    rturma(i, codigo)
                        else:
                            print("O ano inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")

                        pergunta = input("\nDeseja pesquisar outra turma? Sim ou Não? ")
                        if pergunta[0].upper() == "N":
                            os.system("cls")
                            parametro = menu_pesquisar()
                            os.system("cls")    

                    elif opcao.upper() == "SAIR":
                        os.system("cls")
                        parametro = menu_pesquisar()
                        os.system("cls")

                    else:
                        print("Opção inválida")
                        time.sleep(1)
                        os.system("cls")
                        parametro = menu_pesquisar()
                        os.system("cls")

                else:
                    print("Nenhum valor cadastrado em turmas, por favor cadastrar!")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")    
            else:
                os.system("cls")
                print("Ainda não foi cadastrado nenhuma turma")


        # Pesquisar aluno
        elif parametro == "2":
            if os.path.exists("alunos.json"):
                os.system("cls")
                if len(alunos) > 0:
                    opcao = input("Como você quer pesquisar o(a) aluno(a)? matricula, nome ou sair? ")
                    os.system("cls")

                    if opcao.upper() == "MATRICULA" or opcao[0].upper() == "MATRÍCULA":
                        matricula = input("Digite a matricula do aluno(a): ")
                        os.system("cls")

                        if matricula in alunos:
                            for i in alunos:
                                raluno(i, matricula)
                                break

                            pergunta = input("\nDeseja pesquisar outro aluno: Sim ou Não? ")
                            if pergunta[0].upper() == "N":
                                os.system("cls")
                                parametro = menu_pesquisar()
                                os.system("cls")

                        else:
                            print("A matricula inserida não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")
                        
                    elif opcao.upper() == "NOME":
                        nome = input("\nDigite o nome do aluno(a): ")
                        os.system("cls")

                        for i in alunos:
                            if nome.upper() == alunos[str(i)]["Nome"].upper():
                                existe = True
                                break
                            else:
                                existe = False

                        if existe:
                            for i in alunos:
                                if nome.upper() == alunos[str(i)]["Nome"].upper():
                                    codigo = str(i)
                                    raluno(i, codigo)
                        else:
                            print("O nome inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")    

                        pergunta = input("\nDeseja pesquisar outro nome? Sim ou Não? ")
                        if pergunta[0].upper() == "N":
                            os.system("cls")
                            parametro = menu_pesquisar()
                            os.system("cls")

                    elif opcao.upper() == "SAIR":
                        os.system("cls")
                        parametro = menu_pesquisar()
                        os.system("cls")

                    else:
                        print("Opção inválida")
                        time.sleep(1)
                        os.system("cls")
                        parametro = menu_pesquisar()
                        os.system("cls")
                else:
                    print("Nenhum valor cadastrado em alunos, por favor cadastrar!")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")    

            else:
                os.system("cls")
                print("Ainda não foi cadastrado nenhum aluno")

        # Pesquisar Boletim
        elif parametro == "3":
            if os.path.exists("boletim.json"):
                os.system("cls")
                if len(boletim) > 0:
                    opcao = input("Como você quer pesquisar o boletim? pelo CÓDIGO do aluno, NOME do aluno ou sair[3]? ")
                    os.system("cls")

                    if opcao.upper() == "CÓDIGO" or opcao.upper() == "CODIGO":
                        codigo = input("\nDigite o código do boletim: ")
                        os.system("cls")

                        if codigo in boletim:
                            for i in boletim:
                                rboletim(i, codigo)
                                break

                            pergunta = input("\nDeseja pesquisar outro boletim? Sim ou Não? ")
                            if pergunta[0].upper() == "N":
                                os.system("cls")
                                parametro = menu_pesquisar()
                                os.system("cls")
                        else:
                            print("O código inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")

                    elif opcao.upper() == "NOME":
                        nome_aluno = input("\nDigite o nome do aluno(a): ")
                        os.system("cls")

                        for i in boletim:
                            if nome_aluno.upper() == boletim[str(i)]["Nome"].upper():
                                existe = True
                                break
                            else:
                                existe = False

                        if existe:
                            for i in alunos:
                                if nome_aluno.upper() == boletim[str(i)]["Nome"].upper():
                                    codigo = str(i)
                                    rboletim(i, codigo)
                        else:
                            print("O nome inserido não existe no sistema!")
                            time.sleep(1.5)
                            os.system("cls")    

                        pergunta = input("\nDeseja pesquisar outro boletim? Sim ou Não? ")
                        if pergunta[0].upper() == "N":
                            os.system("cls")
                            parametro = menu_pesquisar()
                            os.system("cls")

                    elif opcao.upper() == "SAIR":
                        os.system("cls")
                        parametro = menu_pesquisar()
                        os.system("cls")
                else:
                    print("Nenhum valor cadastrado em boletins, por favor cadastrar!")
                    time.sleep(2)
                    os.system("cls")
                    parametro = menu_editar()
                    os.system("cls")    

        elif parametro == "4":
            os.system("cls")
            break

        else:
            print("Valor inválido!!")
            time.sleep(1.5)
            os.system("cls")
            break
            
def listar(parametro):
    verifica()
    while True:
        turma, aluno, boletim = abrirArquivos()

        # Listar Turmas
        if parametro == "1":
            if len(turma) > 0:
                for i in turma:
                    lisTurma(i)

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_listar()
                    os.system("cls")                
                else:
                    os.system("cls")
                    break
            else:
                print("Não existe turmas!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_listar()
                os.system("cls")

        # Listar Alunos por Turma
        elif parametro == "2":
                
            if len(aluno) > 0:
                for i in aluno:
                    lisAlunos(i)     

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_listar()
                    os.system("cls")                
                else:
                    os.system("cls")
                    break
            else:
                print("Não existe alunos!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_listar()
                os.system("cls")

        # Listar Alunos e Boletins por Turma
        elif parametro == "3":

            if len(aluno) > 0:
                for i in aluno:
                    lisAlunosBoletim(i)

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_listar()
                    os.system("cls")
                else:
                    os.system("cls")
                    break
            else:
                print("Não existe alunos!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_listar()
                os.system("cls")

        # Listar Alunos Aprovados e Boletins por Turma
        elif parametro == "4":
            existe = False

            if len(aluno) > 0:
                for i in aluno:
                    if boletim.get(str(i)):
                        if boletim[i]["Situação"] == "Aprovado":
                            lisAlunosBoletim(i)
                            existe = True
                    
                if not existe:
                    os.system("cls")
                    print("Não existem alunos aprovados!")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_listar()
                    os.system("cls")

                else:
                    pergunta = input("Deseja continuar listando? Sim ou Não? ")
                    if pergunta[0].upper() == "S":
                        os.system("cls")
                        parametro = menu_listar()
                        os.system("cls")

                    else:
                        os.system("cls")
            else:
                print("Não existe alunos!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_listar()
                os.system("cls")

        # Listar Alunos Reprovados e Boletins por Turma
        elif parametro == "5":
            existe = False

            if len(aluno) > 0:
                for i in aluno:
                    if boletim.get(str(i)):
                        if boletim[i]["Situação"] == "Reprovado":
                            lisAlunosBoletim(i)
                            existe = True
                
                if not existe:
                    os.system("cls")
                    print("Não existem alunos reprovados!")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_listar()
                    os.system("cls")
                
                else:
                    pergunta = input("Deseja continuar listando? Sim ou Não? ")
                    if pergunta[0].upper() == "S":
                        os.system("cls")
                        parametro = menu_listar()
                        os.system("cls")

                    else:
                        os.system("cls")
            else:
                print("Não existe alunos!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_listar()
                os.system("cls")

        # Sair
        elif parametro == "6":
            os.system("cls")
            break                   
                        

def relatorio(parametro):
    verifica()

    while True:
        turma, aluno, boletim = abrirArquivos()

        if parametro == "1":
            if len(aluno) > 0:
                print(f"""{'-' * 15} TOTAL DE TURMAS {'-' * 15}

Total = {len(turma)}

""")

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_relatorio()
                    os.system("cls")
                else:
                    os.system("cls")
                    break
                
            else:
                print("Não existe nenhum aluno!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_relatorio()
                os.system("cls")
            
        elif parametro == "2":
            if len(turma) > 0:
                for codigo in turma:
                    qnt_aluno = 0
                    nome_turma = turma[codigo]["Nome"]
                    for turma_aluno in aluno:
                        if nome_turma == aluno[turma_aluno]["Turma"]:
                            qnt_aluno += 1

                    print(f"""{'-' * 15} {nome_turma} {'-' * 15}

Total de alunos: {qnt_aluno}

""")         

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_relatorio()
                    os.system("cls")
                else:
                    os.system("cls")
                    break  

            else:
                print("Não existe nenhum aluno!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_relatorio()
                os.system("cls")


        elif parametro == "3":
            if len(turma) > 0:
                for codigo in turma:
                    qnt_aprovado, qnt_reprovado, qnt_aluno = 0, 0, 0
                    nome_turma = turma[codigo]["Nome"]
                    for aluno_aprovado in aluno:
                        if nome_turma == aluno[aluno_aprovado]["Turma"] and boletim[aluno_aprovado]["Situação"] == "Aprovado":
                            qnt_aprovado += 1
                            qnt_aluno += 1
                        if nome_turma == aluno[aluno_aprovado]["Turma"] and boletim[aluno_aprovado]["Situação"] == "Reprovado":
                            qnt_reprovado += 1
                            qnt_aluno += 1

                    print(f"""{'-' * 15} {nome_turma} {'-' * 15}

Total de alunos: {qnt_aluno}
Alunos Aprovados: {qnt_aprovado}
Alunos Reprovados: {qnt_reprovado}

""")         

                pergunta = input("Deseja continuar listando? Sim ou Não? ")
                os.system("cls")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_relatorio()
                    os.system("cls")
                else:
                    os.system("cls")
                    break  

            else:
                print("Não existe nenhum aluno!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_relatorio()
                os.system("cls")

        # maiores e menores médias, por turma
        elif parametro == "4":
            if len(turma) > 0:
                for codigo in turma:
                    nome_turma, medias = turma[codigo]["Nome"], {}

                    if boletim.get(str(codigo)) or aluno.get(str(codigo)):
                        for media_aluno in aluno:
                            if nome_turma == aluno[media_aluno]["Turma"]:
                                medias[aluno[media_aluno]["Nome"]] = boletim[media_aluno]["Média"] 
                            
                        if medias:
                            print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\nMedias dos alunos em ordem crescente: \n")
                            for i in sorted(medias, key = medias.get):
                                print(f"{f'Aluno: {i}'.ljust(20)}        {f'Média: {medias[i]}'}")
                        else:
                            print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\n\nNão há alunos com médias.\n")
                        print(f"{'-' * 43}")
                        
                    else:
                        print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\n")
                        print("Não há boletins ou alunos para esta turma")       

                pergunta = input("\nDeseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_relatorio()
                    os.system("cls")
                else:
                    os.system("cls")
                    break  

            else:
                print("Não existe nenhum aluno!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_relatorio()
                os.system("cls")

        elif parametro == "5":
            if len(turma) > 0:
                for codigo in turma:
                    limite = {}
                    nome_turma = turma[codigo]["Nome"]

                    if boletim.get(str(codigo)) or aluno.get(str(codigo)):
                        for faltas in aluno:
                            if nome_turma == aluno[faltas]["Turma"]:
                                limite[aluno[faltas]["Nome"]] = boletim[faltas]["Quantidade de Faltas"]

                        if limite:
                            print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\nFalta dos alunos em ordem crescente: \n")
                            for i in sorted(limite, key = limite.get):
                                print(f"{f'Aluno: {i}'.ljust(20)}        {f'Faltas: {limite[i]}'}")
                        else:
                            print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\n\nNão há alunos com faltas.\n")
                        print(f"{'-' * 43}")

                    else:
                        print(f"\n{'-' * 15} {nome_turma} {'-' * 15}\n")
                        print("Não há boletins ou alunos para esta turma")  

                pergunta = input("\nDeseja continuar listando? Sim ou Não? ")
                if pergunta[0].upper() == "S":
                    os.system("cls")
                    parametro = menu_relatorio()
                    os.system("cls")
                else:
                    os.system("cls")
                    break

            else:
                print("Não existe nenhum aluno!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_relatorio()
                os.system("cls")

        elif parametro == "6":
            os.system("cls")
            break
