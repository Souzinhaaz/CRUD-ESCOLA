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
    
# Cria o modelo do menu cadastro
def menu_cadastro():
    parametro = input(f"""{'-' * 15} Cadastro {'-' * 15}

1 - Cadastrar Turma
2 - Cadastrar Aluno
3 - Cadastrar Boletim
4 - Sair do cadastro

{'-' * 40}\n""") 
    
    return parametro
    
# Cria o modelo do menu editar
def menu_editar():
    parametro = input(f"""{'-' * 15} Editar {'-' * 15}

1 - Editar Turma
2 - Editar Aluno
3 - Editar Boletim
4 - Sair da edição

{'-' * 40}\n""")
    
    return parametro

def menu_remover():
    parametro = input(f"""{'-' * 15} Remover {'-' * 15}

1 - Remover Turma
2 - Remover Aluno
3 - Remover Boletim
4 - Sair da função

{'-' * 40}\n""")
    
    return parametro

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
    
# Cria a função para cadastrar
def cadastrar(parametro):
    while True:

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

                # Adiciona os dados no turmas.json
                turmas_json.seek(0, 0)
                json.dump(nova_turma, turmas_json, indent=4)

                # Volta para a interatividade do site
                time.sleep(1)
                print("Turma Cadastrada com sucesso!!")
                time.sleep(1.5)
                os.system("cls")
                break
                    
            elif parametro == "2":
                nova_turma = json.load(turmas_json)
                # Verifica se existe algum valor no arquivo
                if len(nova_turma) > 0:
                    # A variavel novo_aluno vai receber o dicionário que está no alunos_json e a nova_turma o que está em turmas_json
                    novo_aluno = json.load(alunos_json)

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

                    # Interatividade do aplicativo
                    print("Carregando...\n")

                    # Adiciona os dados no alunos.json
                    alunos_json.seek(0, 0)
                    json.dump(novo_aluno, alunos_json, indent=4)

                    # Volta para a interatividade do site
                    time.sleep(1)
                    print("Aluno(a) Cadastrado(a) com sucesso!!")
                    time.sleep(1.5)
                    os.system("cls")
                        
                else:
                    os.system("cls")
                    print("\nPor favor, crie uma turma primeiro! ")
                    time.sleep(1.5)
                    os.system("cls")
                    parametro = menu_cadastro()
                    os.system("cls")
                
            elif parametro == "3":
                # A variavel novo_boletim vai receber o dicionário que está no boletins_json e o aluno o que está em alunos_json
                novo_boletim = json.load(boletins_json)
                aluno = json.load(alunos_json)

                # Verifica se o json de alunos esta vazio e se o id referido está dentro do alunos_json
                if len(aluno) > 0:

                    # Vai pedir o id do aluno referido
                    id_aluno = input("Digite o numero de matricula do Aluno referido: ")
                    if id_aluno in aluno:
                    
                        # Vai guardar a quantidade de faltas na variável qnt_faltas
                        qnt_faltas = int(input("Digite a quantidade de faltas do aluno inserido: "))

                        # Vai guardar as notas do aluno em uma lista
                        notas_aluno = []
                        for i in range(1, 4):
                            nota = float(input(f"Digite a {i}a nota: "))
                            notas_aluno.append(nota)
                        
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

                        # Calculo para obter o novo id do boletim
                        id_boletim = str(1+int(list(novo_boletim.keys())[-1])) if len(novo_boletim) > 0 else "1"
                        
                        novo_boletim[id_boletim] = {
                            "Nome": aluno[id_aluno]["Nome"],
                            "Turma": aluno[id_aluno]["Turma"],
                            "Notas": notas_aluno,
                            "Quantidade de Faltas": qnt_faltas,
                            "Situação": situacao
                        } 

                        print("Carregando...\n")

                        # Adiciona os dados a boletins_json
                        boletins_json.seek(0, 0)
                        json.dump(novo_boletim, boletins_json, indent=4)

                        # Volta para a interatividade do site
                        time.sleep(1)
                        print("Boletim Cadastrado com sucesso!!")
                        time.sleep(1.5)
                        os.system("cls")
                        break

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
    # Loop para não sair da opção de parametro
    while True:
        # Usuário escolhe a opção de editar as turmas
        if parametro == "1":
            # Verificar se existe o arquivo na pasta
            if os.path.exists("turmas.json"):
                # Vai abrir o arquivo desejado
                with open("turmas.json", "r+", encoding="utf-8") as turmas_json:
                    # carrega o dicionário de turmas_json na variável turmas
                    turmas = json.load(turmas_json)

                    # Verificar se existe algum valor no arquivo
                    if len(turmas) > 0:
                        print(f"""{'-' * 15} Edição {'-' * 15}\n""")

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

                                        with open("turmas.json", "w", encoding="utf-8") as turmas_json:
                                            turmas_json.seek(0, 0)
                                            json.dump(turmas, turmas_json, indent=4)
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

                                        with open("turmas.json", "w", encoding="utf-8") as turmas_json:
                                            turmas_json.seek(0, 0)
                                            json.dump(turmas, turmas_json, indent=4)
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

                                        with open("turmas.json", "w", encoding="utf-8") as turmas_json:
                                            turmas_json.seek(0, 0)
                                            json.dump(turmas, turmas_json, indent=4)
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
            else:
                print("Nenhuma turma cadastrada ainda, por favor, cadastre alguma turma!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        # Usuário escolhe a opção de editar os alunos
        elif parametro == "2":
            # Verificar se existe o arquivo na pasta
            if os.path.exists("alunos.json"):
                # Vai abrir o arquivo desejado
                with open("alunos.json", "r+", encoding="utf-8") as alunos_json:
                    # carrega o dicionário de alunos_json na variável alunos
                    alunos = json.load(alunos_json)
                    
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
                                        alunos[codigo]["Nome"] = novo_nome

                                        with open("alunos.json", "w", encoding="utf-8") as alunos_json:
                                            alunos_json.seek(0, 0)
                                            json.dump(alunos, alunos_json, indent=4)
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

                                        with open("alunos.json", "w", encoding="utf-8") as alunos_json:
                                            alunos_json.seek(0, 0)
                                            json.dump(alunos, alunos_json, indent=4)
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

                                        with open("alunos.json", "w", encoding="utf-8") as alunos_json:
                                            alunos_json.seek(0, 0)
                                            json.dump(alunos, alunos_json, indent=4)
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
                                    nova_turma = input("\nDigite o código da turma: ")
                                    if not nova_turma in turmas:
                                        print("Essa turma não existe, por favor digite outra!!")
                                        nova_turma = input("\nDigite o código da turma existente: ")
                                    else:
                                        pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                        if pergunta[0].upper() == "S":
                                            alunos[codigo]["Turma"] = nova_turma

                                            with open("alunos.json", "w", encoding="utf-8") as alunos_json:
                                                alunos_json.seek(0, 0)
                                                json.dump(alunos, alunos_json, indent=4)
                                                print("\nNova turma registrada com sucesso!!")
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
            else:
                print("Nenhum aluno(a) cadastrado(a) ainda, por favor, cadastre algum(a) aluno(a)!")
                time.sleep(2)
                os.system("cls")
                parametro = menu_editar()
                os.system("cls")

        # Usuário escolhe a opção de editar os boletins
        elif parametro == "3":
            # Verificar se existe o arquivo na pasta
            if os.path.exists("boletim.json"):
                # Vai abrir o arquivo desejado
                with open("boletim.json", "r+", encoding="utf-8") as boletins_json:
                    # carrega o dicionário de boletins_json na variável boletins
                    boletins = json.load(boletins_json)

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
                                    pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                    if pergunta[0].upper() == "S":
                                        boletins[codigo]["Nome"] = novo_nome

                                        with open("boletim.json", "w", encoding="utf-8") as boletins_json:
                                            boletins_json.seek(0, 0)
                                            json.dump(boletins, boletins_json, indent=4)
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
                                    pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                    if pergunta[0].upper() == "S":
                                        boletins[codigo]["Turma"] = nova_turma

                                        with open("boletim.json", "w", encoding="utf-8") as boletins_json:
                                            boletins_json.seek(0, 0)
                                            json.dump(boletins, boletins_json, indent=4)
                                            print("\nNova turma registrada com sucesso!!")
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

                            elif pergunta.upper() == "NOTAS":
                                print(f"\n{boletins[codigo]['Notas']}\n")

                                pergunta = input("Essa são as notas que deseja editar? Sim ou Não? ")

                                if pergunta[0].upper() == "S":
                                    os.system("cls")
                                    print(f"""{'-' * 15} Edição {'-' * 15}""")
                                    notas_aluno = []
                                    for i in range(1, 4):
                                        nota = float(input(f"Digite a {i}a nota: "))
                                        notas_aluno.append(nota)

                                    pergunta = input("\nTem certeza que deseja editar? Sim ou Não? ")
                                    if pergunta[0].upper() == "S":
                                        boletins[codigo]["Notas"] = notas_aluno

                                        with open("boletim.json", "w", encoding="utf-8") as boletins_json:
                                            boletins_json.seek(0, 0)
                                            json.dump(boletins, boletins_json, indent=4)
                                            print("Novas notas registradas com sucesso!!")
                                            time.sleep(2)
                                            os.system("cls")
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

                                        with open("boletim.json", "w", encoding="utf-8") as boletins_json:
                                            boletins_json.seek(0, 0)
                                            json.dump(boletins, boletins_json, indent=4)
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

                                            with open("boletim.json", "w", encoding="utf-8") as boletins_json:
                                                boletins_json.seek(0, 0)
                                                json.dump(boletins, boletins_json, indent=4)
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
            else:
                print("Nenhum boletim cadastrado ainda, por favor, cadastre algun boletim!")
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
    # Loop para não sair da opção de parametro
    while True:

        # Se o usuário escolher remover turma
        if parametro == "1":
            if os.path.exists("turmas.json"):
                # Vai abrir o arquivo desejado
                with open("turmas.json", "r+", encoding="utf-8") as turmas_json:
                    # carrega o dicionário de turmas_json na variável turmas
                        turma = json.load(turmas_json)
                        
                        codigo = input("Digite o código da turma que você deseja remover: ")

                        if codigo in turma:
                            print(f"{turma[codigo]}\nEssa é a turma que você deseja remover")
                            pergunta = input("Você tem certeza? Sim ou Não? ")

                            if pergunta[0].upper() == "S":
                                
                                if len(turma) > 1:
                                    del turma[codigo]

                                    turma[str(int(codigo)+1)] = codigo # Simplesmente para pegar o próximo id do código digitado ou seja, 2 vai receber 1
                                
                                    with open("turmas.json", "w", encoding="utf-8") as turmas_json:
                                        json.dump(turma, turmas_json, indent=4)
                                        print("\nTurma removida com sucesso!")
                                        time.sleep(2)
                                        os.system("cls")
                                        break
                                else:
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
                            print("Nenhuma turma existente, por favor, crie uma!")
                            time.sleep(1.5)
                            os.system("cls")
                            break
            else:
                print("Nenhuma turma cadastrada ainda!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_remover()
                os.system("cls")        
        
        # Se o usuário escolher remover alunos
        elif parametro == "2":
            if os.path.exists("alunos.json"):
                pass
            else:
                print("Nenhum aluno(a) cadastrado(a) ainda!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_remover()
                os.system("cls")  

        # Se o usuário esolher remover boletim
        elif parametro == "3":
            if os.path.exists("boletim.json"):
                pass
            else:
                print("Nenhum boletim cadastrado ainda!")
                time.sleep(1.5)
                os.system("cls")
                parametro = menu_remover()
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





