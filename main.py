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
        print('3 - Atualizar Dados')
        print('4 - Sair')
        printCor(('-' * 20), 'azul')
    
    elif menu == 'cadastro':
        printCor(' Cadastro '.center(25, '-'), 'azul')
        print('1 - Cadastro de Aluno')
        print('2 - Cadastro de Professor')
        print('3 - Voltar')
        printCor(('-' * 25), 'azul')

    elif menu == 'relatorios':
        printCor(' Relatorios '.center(30, '-'), 'azul')
        print('1 - Lista de Professores')
        print('2 - Lista de Alunos')
        print('3 - Lista das Salas')
        print('4 - Voltar')
        printCor(('-' * 30), 'azul')

    elif menu == 'atualizacao':
        printCor(' Atualização '.center(30, '-'), 'azul')
        print('1 - Professor')
        print('2 - Aluno')
        print('3 - Voltar')
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
        if aluno['turma'] == 'CANCELAR': return None
        elif not aluno['turma'].isalpha() or len(aluno['turma']) != 1:
            printCor('-=- Erro! Turma invalida digitada -=-', 'vermelho')
            continue
        break

    aluno['notas'] = []
    aluno['media'] = 0

    return aluno.copy()

def cadastrarProfessor(professores):
    prof = {}
    prof['id'] = professores[-1]['id'] + 1

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
    prof['turmas'].sort()

    while True:
        try:
            prof['salario'] = float(input('Salário: R$'))
            break
        except ValueError:
            printCor('-=- Erro! Valor invalido digitado! -=-', 'vermelho')

    return prof

def mostrarProfessores(professores):
    system('cls')
    for i, prof in enumerate(professores):
        printCor(f' Professor {i+1} '.center(30, '-'), 'azul')
        print(f'Id: {prof["id"]}')
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

def localizarProfessor(professores):
    mostrarProfessores(professores)
    while True:
        try:
            printCor('-- [Digite cancelar para sair] --', 'amarelo')
            printCor('Digite o ID do professor: ', 'verde', False)
            id = input()
            if id == 'cancelar': return None
            id = int(id)
            for prof in professores:
                if id == prof['id']: return prof
            printCor('-=- Erro! Não foi possivel localizar este ID -=-', 'vermelho')
        except ValueError:
            printCor('-=- Erro! ID Invalido digitado', 'vermelho')

def localizarPosicaoProfessor(professor, professores):
    for i, prof in enumerate(professores):
        if prof['id'] == professor['id']: return i
    return -1

def editarProfessor(professor):
    professor = professor.copy()
    while True:
        system('cls')
        printCor(f' Professor ID:{professor["id"]} '.center(30, '-'), 'azul')
        print(f'Nome: {professor["nome"]}')
        print('Turmas: ', end='')
        printCor(professor['turmas'], 'roxo')
        print('Salário: ', end='')
        printCor(f'R${professor["salario"]:.2f}', 'verde')
        printCor(('-' * 30), 'azul')

        while True:
            printCor('-- [Digite cancelar para sair] --', 'amarelo')
            printCor('-- [Digite salvar para salvar alterações] --', 'amarelo')
            printCor('Digite o nome do campo a ser atualizado: ', 'verde', False)
            campo = input().lower().strip()
            if campo == 'cancelar': return None
            elif campo == 'salvar': return professor
            elif campo not in ['nome', 'turmas', 'salario']:
                printCor('-=- Erro! Campo Invalido informado -=-', 'vermelho')
                continue
            break

        if campo == 'nome': professor['nome'] = input('Novo nome: ').title().strip()

        elif campo == 'turmas':
            backup = professor['turmas']
            professor['turmas'] = []
            while True:
                printCor('-- [Digite cancelar para sair] --', 'amarelo')
                printCor('-- [Digite parar para parar de adicionar turmas] --', 'amarelo')
                turma = input('Turma: ')
                if turma == 'cancelar':
                    professor['turmas'] = backup[:]
                    break
                if turma == 'parar':
                    if len(professor['turmas']) < 1:
                        printCor('-=- Erro! Professor precisa possuir ao menos uma turma! -=-', 'vermelho')
                        continue
                    break
                elif not turma.isalpha() or len(turma) > 1:
                    printCor('-=- Erro! Turma Invalida! -=-', 'vermelho')
                    continue
                professor['turmas'].append(turma.upper())
            professor['turmas'].sort()

        else:
            while True:
                try:
                    printCor('-- [Digite cancelar para sair] --', 'amarelo')
                    salario = input('Salário: R$')
                    if salario == 'cancelar': break
                    salario = float(salario)
                    professor['salario'] = salario
                    break
                except ValueError:
                    printCor('-=- Erro! Valor invalido digitado! -=-', 'vermelho')


alunos = [
    {'nome': 'Heitor Pereira', 'idade': 2, 'mae': 'Heloisa Pereira', 'turma': 'A', 'notas': [85, 75], 'media': 80},
    {'nome': 'Laura Souza', 'idade': 3, 'mae': 'Mariana Souza', 'turma': 'A', 'notas': [65, 45], 'media': 55},
    {'nome': 'Lucas Lima', 'idade': 1, 'mae': 'Fernanda Lima', 'turma': 'B', 'notas': [50, 40], 'media': 45},
    {'nome': 'Isabela Martins', 'idade': 2, 'mae': 'Cláudia Martins', 'turma': 'C', 'notas': [95, 85], 'media': 90},
    
    {'nome': 'Pedro Oliveira', 'idade': 3, 'mae': 'Ana Oliveira', 'turma': 'A', 'notas': [70, 60], 'media': 65},
    {'nome': 'Sofia Santos', 'idade': 2, 'mae': 'Bruna Santos', 'turma': 'A', 'notas': [90, 80], 'media': 85},
    {'nome': 'Rafael Ferreira', 'idade': 4, 'mae': 'Juliana Ferreira', 'turma': 'B', 'notas': [60, 50], 'media': 55},
    {'nome': 'Giovanna Costa', 'idade': 1, 'mae': 'Patrícia Costa', 'turma': 'C', 'notas': [80, 75], 'media': 77.5},

    {'nome': 'Miguel Almeida', 'idade': 3, 'mae': 'Tatiana Almeida', 'turma': 'D', 'notas': [85, 70], 'media': 77.5},
    {'nome': 'Emily Rocha', 'idade': 2, 'mae': 'Renata Rocha', 'turma': 'D', 'notas': [95, 90], 'media': 92.5},
    {'nome': 'Arthur Ribeiro', 'idade': 4, 'mae': 'Roberta Ribeiro', 'turma': 'B', 'notas': [50, 45], 'media': 47.5},
    {'nome': 'Mariana Silva', 'idade': 3, 'mae': 'Luciana Silva', 'turma': 'C', 'notas': [85, 80], 'media': 82.5},

    {'nome': 'Felipe Lopes', 'idade': 2, 'mae': 'Carla Lopes', 'turma': 'A', 'notas': [70, 60], 'media': 65},
    {'nome': 'Ana Clara Lima', 'idade': 1, 'mae': 'Sônia Lima', 'turma': 'B', 'notas': [55, 50], 'media': 52.5},
    {'nome': 'Henrique Barbosa', 'idade': 3, 'mae': 'Aline Barbosa', 'turma': 'C', 'notas': [95, 90], 'media': 92.5},
    {'nome': 'Valentina Carvalho', 'idade': 4, 'mae': 'Bianca Carvalho', 'turma': 'D', 'notas': [65, 55], 'media': 60},

    {'nome': 'Gabriel Martins', 'idade': 3, 'mae': 'Renata Martins', 'turma': 'A', 'notas': [80, 75], 'media': 77.5},
    {'nome': 'Lara Costa', 'idade': 1, 'mae': 'Viviane Costa', 'turma': 'D', 'notas': [60, 50], 'media': 55},
    {'nome': 'João Pedro Lima', 'idade': 2, 'mae': 'Tatiana Lima', 'turma': 'B', 'notas': [65, 60], 'media': 62.5},
    {'nome': 'Camila Fonseca', 'idade': 4, 'mae': 'Juliana Fonseca', 'turma': 'C', 'notas': [75, 70], 'media': 72.5},

    {'nome': 'Daniel Souza', 'idade': 2, 'mae': 'Paula Souza', 'turma': 'A', 'notas': [90, 80], 'media': 85},
    {'nome': 'Beatriz Mota', 'idade': 1, 'mae': 'Carolina Mota', 'turma': 'B', 'notas': [55, 50], 'media': 52.5},
    {'nome': 'Yasmin Oliveira', 'idade': 3, 'mae': 'Cláudia Oliveira', 'turma': 'D', 'notas': [85, 75], 'media': 80},
    {'nome': 'Matheus Rodrigues', 'idade': 4, 'mae': 'Fernanda Rodrigues', 'turma': 'C', 'notas': [60, 55], 'media': 57.5}
]
professores = [
    {'id': 1, 'nome': 'Julio Vargas', 'turmas': ['A', 'C'], 'salario': 2500.0},
    {'id': 2, 'nome': 'Helena Silva', 'turmas': ['B', 'C'], 'salario': 2750.0},
    {'id': 3, 'nome': 'Ana Oliveira', 'turmas': ['A'], 'salario': 2400.0},
    {'id': 4, 'nome': 'Carlos Pereira', 'turmas': ['A', 'D'], 'salario': 2600.0},

    {'id': 5, 'nome': 'Bruna Mendes', 'turmas': ['B'], 'salario': 2300.0},
    {'id': 6, 'nome': 'Fernando Costa', 'turmas': ['C', 'D'], 'salario': 2800.0},
    {'id': 7, 'nome': 'Roberta Nunes', 'turmas': ['A', 'B', 'D'], 'salario': 2900.0},
    {'id': 8, 'nome': 'Marcelo Souza', 'turmas': ['B', 'C', 'D'], 'salario': 3100.0}
]
turmas = atualizarSalas(alunos, professores)

while True:
    mostrarMenu('inicio')
    comando = pedirComando(4)
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
                prof = cadastrarProfessor(professores)
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
            else: break

    elif comando == 3:
        while True:
            mostrarMenu('atualizacao')
            comando = pedirComando(3)
            if comando == 1:
                prof = localizarProfessor(professores)
                if prof != None:
                    prof = editarProfessor(prof)
                    if prof != None:
                        professores[localizarPosicaoProfessor(prof, professores)] = prof
                        atualizarSalas(alunos, professores)
            else: break

    else: break
print('Finalizando Programa...')