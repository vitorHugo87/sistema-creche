from os import system

def printCor(msg, cor, end=True):
    cores = {'padrao': '\33[m',
             'vermelho': '\33[31m',
             'verde': '\33[32m',
             'amarelo': '\33[33m',
             'azul': '\33[34m',
             'roxo': '\33[35m',
             'ciano': '\33[36m',
             'cinza': '\33[37m'}
    if end: print(f'{cores[cor]}{msg}{cores["padrao"]}')
    else: print(f'{cores[cor]}{msg}{cores["padrao"]}', end='')

def mostrarMenu(menu):
    system('cls')
    if menu == 'inicio':
        printCor(' Menu '.center(20, '-'), 'azul')
        print('1 - Cadastro')
        print('2 - Relatorios')
        print('3 - Sair')
        printCor(('-' * 20), 'azul')
    
    if menu == 'cadastro':
        printCor(' Cadastro '.center(25, '-'), 'azul')
        print('1 - Cadastro de Aluno')
        print('2 - Cadastro de Professor')
        print('3 - Voltar')
        printCor(('-' * 25), 'azul')

    if menu == 'relatorios':
        printCor(' Relatorios '.center(30, '-'), 'azul')
        print('1 - Lista de Professores')
        print('2 - Lista de Alunos')
        print('3 - Lista das Salas')
        print('4 - Voltar')
        printCor(('-' * 30), 'azul')

def pedirComando(opcoes):
    while True:
        printCor('Comando: ', 'verde', False)
        comando = input()
        if comando.isnumeric():
            comando = int(comando)
            if 0 < comando <= opcoes: return comando
            else: print('-=- Erro! Valor Invalido digitado! -=-')
        else: print('-=- Erro! Comando não pode conter letras! -=-')

def cadastrarAluno():
    aluno = {}

    system('cls')
    printCor('-- [Digite cancelar para sair] --', 'amarelo')
    aluno['nome'] = input('Nome: ')
    if aluno['nome'] == 'cancelar': return None
    aluno['nome'] = aluno['nome'].title()

    while True:
        printCor('-- [Digite cancelar para sair] --', 'amarelo')
        aluno['idade'] = input('Idade [Para menores de 1 ano digite 0]: ')
        if aluno['idade'] == 'cancelar': return None
        elif aluno['idade'].isnumeric():
            aluno['idade'] = int(aluno['idade'])
            if aluno['idade'] > 4:
                printCor('-=- Erro! A Creche só aceita crianças com até 4 anos de idade -=-', 'vermelho')
                continue
        else:
            printCor('-=- Erro! Idade Invalida Digitada! -=-', 'vermelho')
            continue
        break
    
    printCor('-- [Digite cancelar para sair] --', 'amarelo')
    aluno['mae'] = input('Nome da mãe: ')
    if aluno['mae'] == 'cancelar': return None
    aluno['mae'] = aluno['mae'].title()

    while True:
        printCor('-- [Digite cancelar para sair] --', 'amarelo')
        aluno['turma'] = input('Turma: ').upper()
        if aluno['turma'] == 'cancelar': return None
        elif not aluno['turma'].isalpha() or len(aluno['turma']) != 1:
            printCor('-=- Erro! Turma invalida digitada -=-', 'vermelho')
            continue
        break

    aluno['notas'] = []
    aluno['media'] = 0

    return aluno.copy()

def cadastrarProfessor():
    prof = {}

    system('cls')
    printCor('-- [Digite cancelar para sair] --', 'amarelo')
    prof['nome'] = input('Nome: ')
    if prof['nome'] == 'cancelar': return None
    prof['nome'] = prof['nome'].title()

    prof['turmas'] = []
    while True:
        printCor('-- [Digite cancelar para sair] --', 'amarelo')
        printCor('-- [Digite parar para parar de adicionar turmas] --', 'amarelo')
        turma = input('Turma: ')
        if turma == 'cancelar': return None
        if turma == 'parar':
            if len(prof['turmas']) < 1:
                printCor('-=- Erro! Professor precisa possuir ao menos uma turma! -=-', 'vermelho')
                continue
            break
        elif not turma.isalpha() or len(turma) > 1:
            printCor('-=- Erro! Turma Invalida! -=-', 'vermelho')
            continue
        prof['turmas'].append(turma.upper())

    while True:
        try:
            prof['salario'] = float(input('Salário: R$'))
            break
        except ValueError:
            printCor('Erro! Valor invalido digitado!', 'vermelho')
    
    return prof

def mostrarProfessores(professores):
    system('cls')
    for i, prof in enumerate(professores):
        printCor(f' Professor {i+1} '.center(30, '-'), 'azul')
        print(f'Nome: {prof["nome"]}')
        print(f'Turmas: ', end='')
        printCor(prof["turmas"], 'roxo')
        print(f'Salario: ', end='')
        printCor(f'R${prof["salario"]:.2f}\n', 'verde')

def mostrarAlunos(alunos):
    system('cls')
    for i, aluno in enumerate(alunos):
        printCor(f' Aluno {i+1} '.center(30, '-'), 'azul')
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade: {aluno["idade"]} ano(s)')
        print(f'Mãe: {aluno["mae"]}')

        print('Turma: ', end='')
        printCor(aluno["turma"], 'roxo')

        print(f'Notas: [', end='')
        if len(aluno['notas']) == 0: print(']')
        for i, nota in enumerate(aluno['notas']):
            if nota > 60: cor = 'verde'
            elif nota < 50: cor = 'vermelho'
            else: cor = 'amarelo'
            printCor(nota, cor, False)
            if i != (len(aluno['notas']) - 1): print(', ', end='')
            else: print(']')
        
        print(f'Media: ', end='')
        if aluno['media'] > 60: cor = 'verde'
        elif aluno['media'] < 50: cor = 'vermelho'
        else: cor = 'amarelo'
        printCor(f'{aluno["media"]:.1f}\n', cor)

def atualizarSalas(alunos, professores):
    turmas = []
    for prof in professores:
        for turma in prof['turmas']:
            if turma not in turmas: turmas.append(turma)
    for aluno in alunos:
        if aluno['turma'] not in turmas: turmas.append(aluno['turma'])

    turmas.sort()
    
    salas = []
    for turma in turmas:
        sala = {}
        sala['turma'] = turma
        sala['professores'] = []
        for prof in professores:
            for turmaProf in prof['turmas']:
                if turmaProf == turma: sala['professores'].append(prof)

        sala['alunos'] = []
        for aluno in alunos:
            if aluno['turma'] == turma: sala['alunos'].append(aluno)

        salas.append(sala.copy())
    
    return salas[:]

def mostrarSalas(turmas):
    system('cls')
    for sala in turmas:
        printCor(f' Turma {sala["turma"]} '.center(30, '-'), 'azul')
        printCor('-=- Professores -=-', 'roxo')
        for i, prof in enumerate(sala['professores']):
            print(f'{i+1} - {prof["nome"]}')
        
        printCor('-=- Alunos -=-', 'roxo')
        for i, aluno in enumerate(sala['alunos']):
            print(f'{i+1} - {aluno["nome"]}')
        print()

alunos = [
    {'nome': 'Heitor Pereira', 'idade': 2, 'mae': 'Heloisa Pereira', 'turma': 'A', 'notas': [85, 75], 'media': 80},
    {'nome': 'Laura Souza', 'idade': 3, 'mae': 'Mariana Souza', 'turma': 'A', 'notas': [65, 45], 'media': 55},
    {'nome': 'Lucas Lima', 'idade': 1, 'mae': 'Fernanda Lima', 'turma': 'B', 'notas': [50, 40], 'media': 45},
    {'nome': 'Isabela Martins', 'idade': 2, 'mae': 'Cláudia Martins', 'turma': 'C', 'notas': [95, 85], 'media': 90}
]
professores = [
    {'nome': 'Julio Vargas', 'turmas': ['A', 'C'], 'salario': 2500.0},
    {'nome': 'Helena Silva', 'turmas': ['B', 'C'], 'salario': 2750.0}
]
turmas = atualizarSalas(alunos, professores)

while True:
    mostrarMenu('inicio')
    comando = pedirComando(3)
    if comando == 1:
        while True:
            mostrarMenu('cadastro')
            comando = pedirComando(3)
            if comando == 1:
                aluno = cadastrarAluno()
                if aluno != None:
                    alunos.append(aluno.copy())
                    turmas = atualizarSalas(alunos, professores)
            elif comando == 2:
                prof = cadastrarProfessor()
                if prof != None: 
                    professores.append(prof.copy())
                    turmas = atualizarSalas(alunos, professores)
            else: break

    elif comando == 2:
        while True:
            mostrarMenu('relatorios')
            comando = pedirComando(4)
            if comando == 1:
                mostrarProfessores(professores)
                input('Pressione Enter para continuar...')
            elif comando == 2:
                mostrarAlunos(alunos)
                input('Pressione Enter para continuar...')
            elif comando == 3:
                mostrarSalas(turmas)
                input('Pressione Enter para continuar...')
            elif comando == 4: break

    else: break
print('Finalizando Programa...')