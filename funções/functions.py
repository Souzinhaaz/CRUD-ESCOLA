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


