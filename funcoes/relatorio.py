import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from funcoes.functions import *

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