import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from funcoes.functions import *

def pesquisar(parametro):
    verifica()
    while True:
        turma, alunos, boletim = abrirArquivos()
        # Loop para não sair da função
        if parametro == "1":
            if os.path.exists("arquivos/turmas.json"):
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
            if os.path.exists("arquivos/alunos.json"):
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
            if os.path.exists("arquivos/boletim.json"):
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
