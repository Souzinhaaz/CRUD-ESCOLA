import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from funcoes.functions import *

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
