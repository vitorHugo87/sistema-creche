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

alunos = []
professores = []

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
            if comando == 3: break
        comando = None
    if comando == 3: break
print('Finalizando Programa...')