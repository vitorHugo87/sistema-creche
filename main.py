from os import system

def mostrarMenu(menu):
    system('cls')
    if menu == 'inicio':
        print(' Menu '.center(20, '-'))
        print('1 - Cadastro')
        print('2 - Relatorios')
        print('3 - Sair')
        print('-' * 20)
    
    if menu == 'cadastro':
        print(' Cadastro '.center(25, '-'))
        print('1 - Cadastro de Aluno')
        print('2 - Cadastro de Professor')
        print('3 - Voltar')
        print('-' * 25)

    if menu == 'relatorios':
        print(' Relatorios '.center(30, '-'))
        print('1 - Lista de Professores')
        print('2 - Lista de Alunos')
        print('3 - Lista das Salas')
        print('4 - Voltar')
        print('-' * 30)

def pedirComando(opcoes):
    while True:
        comando = input('Comando: ')
        if comando.isnumeric():
            comando = int(comando)
            if 0 < comando <= opcoes: return comando
            else: print('-=- Erro! Valor Invalido digitado! -=-')
        else: print('-=- Erro! Comando não pode conter letras! -=-')

def cadastrarAluno():
    aluno = {}

    system('cls')
    print('-- [Digite cancelar para sair] --')
    aluno['nome'] = input('Nome: ')
    if aluno['nome'] == 'cancelar': return None
    aluno['nome'] = aluno['nome'].title()

    while True:
        print('-- [Digite cancelar para sair] --')
        aluno['idade'] = input('Idade [Para menores de 1 ano digite 0]: ')
        if aluno['idade'] == 'cancelar': return None
        elif aluno['idade'].isnumeric():
            aluno['idade'] = int(aluno['idade'])
            if aluno['idade'] > 4:
                print('-=- Erro! A Creche só aceita crianças com até 4 anos de idade -=-')
                continue
        else:
            print('-=- Erro! Idade Invalida Digitada! -=-')
            continue
        break
    
    print('-- [Digite cancelar para sair] --')
    aluno['mae'] = input('Nome da mãe: ')
    if aluno['mae'] == 'cancelar': return None
    aluno['mae'] = aluno['mae'].title()

    while True:
        print('-- [Digite cancelar para sair] --')
        aluno['turma'] = input('Turma: ').upper()
        if aluno['turma'] == 'cancelar': return None
        elif not aluno['turma'].isalpha() or len(aluno['turma']) != 1:
            print('-=- Erro! Turma invalida digitada -=-')
            continue
        break

    aluno['notas'] = []
    aluno['media'] = 0

    return aluno.copy()

def cadastrarProfessor():
    prof = {}

    system('cls')
    print('-- [Digite cancelar para sair] --')
    prof['nome'] = input('Nome: ')
    if prof['nome'] == 'cancelar': return None
    prof['nome'] = prof['nome'].title()

    prof['turmas'] = []
    while True:
        print('-- [Digite cancelar para sair] --')
        print('-- [Digite parar para parar de adicionar turmas] --')
        turma = input('Turma: ')
        if turma == 'cancelar': return None
        if turma == 'parar':
            if len(prof['turmas']) < 1:
                print('-=- Erro! Professor precisa possuir ao menos uma turma! -=-')
                continue
            break
        elif not turma.isalpha() or len(turma) > 1:
            print('-=- Erro! Turma Invalida! -=-')
            continue
        prof['turmas'].append(turma.upper())

    while True:
        try:
            prof['salario'] = float(input('Salário: R$'))
            break
        except ValueError:
            print('Erro! Valor invalido digitado!')
    
    return prof

def mostrarProfessores(professores):
    system('cls')
    for i, prof in enumerate(professores):
        print(f' Professor {i+1} '.center(30, '-'))
        print(f'Nome: {prof["nome"]}')
        print(f'Turmas: {prof["turmas"]}')
        print(f'Salario: R${prof["salario"]:.2f}\n')

def mostrarAlunos(alunos):
    system('cls')
    for i, aluno in enumerate(alunos):
        print(f' Aluno {i+1} '.center(30, '-'))
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade: {aluno["idade"]} ano(s)')
        print(f'Mãe: {aluno["mae"]}')
        print(f'Turma: {aluno["turma"]}')
        print(f'Notas: {aluno["notas"]}')
        print(f'Media: {aluno["media"]:.1f}\n')

def mostrarSalas(alunos, professores):
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

    system('cls')
    for sala in salas:
        print(f' Turma {sala["turma"]} '.center(30, '-'))
        print('-=- Professores -=-')
        for i, prof in enumerate(sala['professores']):
            print(f'{i+1} - {prof["nome"]}')
        
        print('-=- Alunos -=-')
        for i, aluno in enumerate(sala['alunos']):
            print(f'{i+1} - {aluno["nome"]}')
        print()

alunos = [
    {'nome': 'Heitor Pereira', 'idade': 2, 'mae': 'Heloisa Pereira', 'turma': 'A', 'notas': [85, 75], 'media': 80},
    {'nome': 'Laura Souza', 'idade': 3, 'mae': 'Mariana Souza', 'turma': 'A', 'notas': [90, 88], 'media': 89},
    {'nome': 'Lucas Lima', 'idade': 1, 'mae': 'Fernanda Lima', 'turma': 'B', 'notas': [70, 65], 'media': 67.5},
    {'nome': 'Isabela Martins', 'idade': 2, 'mae': 'Cláudia Martins', 'turma': 'C', 'notas': [95, 85], 'media': 90}
]
professores = [
    {'nome': 'Julio Vargas', 'turmas': ['A', 'C'], 'salario': 2500.0},
    {'nome': 'Helena Silva', 'turmas': ['B', 'C'], 'salario': 2750.0}
]

while True:
    mostrarMenu('inicio')
    comando = pedirComando(3)
    if comando == 1:
        while True:
            mostrarMenu('cadastro')
            comando = pedirComando(3)
            if comando == 1:
                aluno = cadastrarAluno()
                if aluno != None: alunos.append(aluno.copy())
            elif comando == 2:
                prof = cadastrarProfessor()
                if prof != None: professores.append(prof.copy())
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
                mostrarSalas(alunos, professores)
                input('Pressione Enter para continuar...')
            elif comando == 4: break

    else: break
print('Finalizando Programa...')