import sys
sys.path.append('c:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Programação\\Projetos Pessoais\\API-ESCOLA\\funções')
from functions import *

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