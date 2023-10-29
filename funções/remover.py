import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from functions import *

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
