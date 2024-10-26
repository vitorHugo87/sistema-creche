from os import system as limpaTela

admins = [
    {'id': 1, 'email': 'admin@gmail.com', 'senha': 'adm123', 'acesso': 'admin', 'nome': 'Walter White'}
]
alunos = [
    {'ra': 1, 'senha': '123456', 'acesso': 'aluno', 'nome': 'Heitor Pereira', 'idade': 2, 'mae': 'Heloisa Pereira', 'turma': 'A', 'notas': [85, 75], 'media': 80},
    {'ra': 2, 'senha': '654321', 'acesso': 'aluno', 'nome': 'Laura Souza', 'idade': 3, 'mae': 'Mariana Souza', 'turma': 'A', 'notas': [65, 45], 'media': 55},
    {'ra': 3, 'senha': '112233', 'acesso': 'aluno', 'nome': 'Pedro Oliveira', 'idade': 2, 'mae': 'Ana Oliveira', 'turma': 'A', 'notas': [70, 60], 'media': 65},
    {'ra': 10, 'senha': '789123', 'acesso': 'aluno', 'nome': 'Mariana Silva', 'idade': 3, 'mae': 'Luciana Silva', 'turma': 'A', 'notas': [85, 80], 'media': 82.5},
    
    {'ra': 4, 'senha': '445566', 'acesso': 'aluno', 'nome': 'Lucas Lima', 'idade': 1, 'mae': 'Fernanda Lima', 'turma': 'B', 'notas': [50, 40], 'media': 45},
    {'ra': 5, 'senha': '778899', 'acesso': 'aluno', 'nome': 'Sofia Santos', 'idade': 2, 'mae': 'Bruna Santos', 'turma': 'B', 'notas': [90, 80], 'media': 85},
    {'ra': 6, 'senha': '123789', 'acesso': 'aluno', 'nome': 'Rafael Ferreira', 'idade': 1, 'mae': 'Juliana Ferreira', 'turma': 'B', 'notas': [60, 50], 'media': 55},
    {'ra': 11, 'senha': '987321', 'acesso': 'aluno', 'nome': 'Felipe Lopes', 'idade': 2, 'mae': 'Carla Lopes', 'turma': 'B', 'notas': [70, 60], 'media': 65},
    
    {'ra': 7, 'senha': '987654', 'acesso': 'aluno', 'nome': 'Isabela Martins', 'idade': 0, 'mae': 'Cláudia Martins', 'turma': 'C', 'notas': [95, 85], 'media': 90},
    {'ra': 8, 'senha': '321987', 'acesso': 'aluno', 'nome': 'Giovanna Costa', 'idade': 1, 'mae': 'Patrícia Costa', 'turma': 'C', 'notas': [80, 75], 'media': 77.5},
    {'ra': 9, 'senha': '654123', 'acesso': 'aluno', 'nome': 'Arthur Ribeiro', 'idade': 2, 'mae': 'Roberta Ribeiro', 'turma': 'C', 'notas': [50, 45], 'media': 47.5},
    {'ra': 12, 'senha': '321654', 'acesso': 'aluno', 'nome': 'Ana Clara Lima', 'idade': 1, 'mae': 'Sônia Lima', 'turma': 'C', 'notas': [55, 50], 'media': 52.5}
]
profs = [
    {'id': 1, 'email': 'julio@gmail.com', 'senha': 'julio123', 'acesso': 'prof', 'nome': 'Julio Vargas', 'turmas': ['A', 'C'], 'salario': 2500.0},
    {'id': 2, 'email': 'helena@gmail.com', 'senha': 'helena123', 'acesso': 'prof', 'nome': 'Helena Silva', 'turmas': ['B', 'C'], 'salario': 2750.0},
    {'id': 3, 'email': 'ana@gmail.com', 'senha': 'ana123', 'acesso': 'prof', 'nome': 'Ana Oliveira', 'turmas': ['A', 'B'], 'salario': 2600.0},
    {'id': 4, 'email': 'carlos@gmail.com', 'senha': 'carlos123', 'acesso': 'prof', 'nome': 'Carlos Souza', 'turmas': ['A', 'B', 'C'], 'salario': 2900.0},
    {'id': 5, 'email': 'maria@gmail.com', 'senha': 'maria123', 'acesso': 'prof', 'nome': 'Maria Santos', 'turmas': ['A', 'B'], 'salario': 2400.0},
    {'id': 6, 'email': 'joao@gmail.com', 'senha': 'joao123', 'acesso': 'prof', 'nome': 'João Ribeiro', 'turmas': ['C'], 'salario': 2700.0}
]

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

def exibicao(tela, userLevel):
    limpaTela('cls')
    range = 0
    if userLevel == 'admin':
        if tela == 'menu':
            range = 5
            printCor(' MENU '.center(30, '-'), 'azul')
            print('1 - Cadastro')
            print('2 - Atualizar Dados')
            print('3 - Exclusão de usuario')
            print('4 - Relatorios')
            print('5 - Sair')
            printCor(('-' * 30), 'azul')
        if tela == 'cadastro':
            range = 4
            printCor(' CADASTRO '.center(30, '-'), 'azul')
            print('1 - Aluno')
            print('2 - Professor')
            print('3 - Administrador')
            print('4 - Voltar')
            printCor(('-' * 30), 'azul')
    return pedirCmd(range)

def pedirCmd(range):
    while True:
        try:
            printCor('Comando: ', 'verde', False)
            cmd = int(input())
            if cmd < 1 or cmd > range: raise ValueError()
            return cmd
        except ValueError:
            printCor('-=- Erro! Valor Invalido Digitado -=-', 'vermelho')

def login(usuario, senha):
    if usuario.isnumeric():
        usuario = int(usuario)
        for a in alunos:
            if a['ra'] == usuario and a['senha'] == senha: return a.copy()
    else:
        for p in profs:
            if p['email'] == usuario and p['senha'] == senha: return p.copy()
        for a in admins:
            if a['email'] == usuario and a['senha'] == senha: return a.copy()
    limpaTela('cls')
    printCor('-=- Usuario ou Senha invalido! -=-', 'vermelho')
    return None

def novoAluno():
    aluno = {}
    aluno['ra'] = alunos[-1]['ra'] + 1
    aluno['senha'] = '123456'
    aluno['acesso'] = 'aluno'

    limpaTela('cls')

    while True: #Solicitação e validação do nome
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        aluno['nome'] = input('Nome: ').title().strip()
        if aluno['nome'] == 'Cancelar': return None
        elif not aluno['nome'].replace(' ', '').isalpha():
            printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
            continue
        break
    
    while True: #Solicitação e validação da idade
        try:
            printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
            aluno['idade'] = input('Idade [Para menores de 1 ano digite 0]: ')
            if aluno['idade'].lower() == 'cancelar': return None
            aluno['idade'] = int(aluno['idade'])
            if aluno['idade'] < 0: raise ValueError()
            elif aluno['idade'] > 4:
                printCor('-=- Erro! A Creche só aceita crianças com até 4 anos de idade -=-', 'vermelho')
                continue
            break
        except:
            printCor('-=- Erro! Idade Invalida Digitada! -=-', 'vermelho')

    while True: #Solicitação e validação do nome da mãe
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        aluno['mae'] = input('Nome da mãe: ').title().strip()
        if aluno['mae'] == 'Cancelar': return None
        elif not aluno['mae'].replace(' ', '').isalpha():
            printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
            continue
        break

    while True: #Solicitação e validação da turma
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        aluno['turma'] = input('Turma: ').upper()
        if aluno['turma'] == 'CANCELAR': return None
        elif not aluno['turma'].isalpha() or len(aluno['turma']) != 1:
            printCor('-=- Erro! Turma invalida digitada -=-', 'vermelho')
            continue
        break

    aluno['notas'] = []
    aluno['media'] = 0.0
    return aluno.copy()

def novoProf():
    prof = {}
    prof['id'] = profs[-1]['id'] + 1

    limpaTela('cls')

    while True: #Solicitação e validação de email
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        prof['email'] = input('Email: ')
        if prof['email'] == 'cancelar': return None
        elif not '@' in prof['email']:
            printCor('-=- Erro! Email Invalido Digitado -=-', 'vermelho')
            continue
        break

    while True: #Solicitação e validação de senha
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        prof['senha'] = input('Senha: ')
        if prof['senha'] == 'cancelar': return None
        elif len(prof['senha']) < 6:
            printCor('-=- Erro! A senha deve ter ao minimo 6 caracteres -=-', 'vermelho')
            continue
        break

    prof['acesso'] = 'prof'

    while True: #Solicitação e validação do nome
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        prof['nome'] = input('Nome: ').title().strip()
        if prof['nome'] == 'Cancelar': return None
        elif not prof['nome'].replace(' ', '').isalpha():
            printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
            continue
        break

    prof['turmas'] = []
    while True: #Solicitação e validação de turmas
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

    while True: #Solicitação e validação de salario
        try:
            printCor('-- [Digite cancelar para sair] --', 'amarelo')
            prof['salario'] = input('Salario: ')
            if prof['salario'] == 'cancelar': return None
            prof['salario'] = float(prof['salario'])
            if prof['salario'] < 0: raise ValueError()
            break
        except ValueError:
            printCor('-=- Erro! Valor invalido digitado -=-', 'vermelho')

    return prof.copy()


limpaTela('cls')
user = None
while user == None:
    usuario = input('Usuario [RA / Email]: ')
    senha = input('Senha: ')
    user = login(usuario, senha)

if user['acesso'] == 'admin':
    while True:
        cmd = exibicao('menu', 'admin')
        if cmd == 1: #Cadastro
            while True:
                cmd = exibicao('cadastro', 'admin')
                if cmd == 1: #Cadastro de Aluno
                    aluno = novoAluno()
                    if aluno != None: alunos.append(aluno)
                elif cmd == 2: #Cadastro de Prof
                    prof = novoProf()
                    if prof != None: profs.append(prof)
                    print(profs)
                    input()
                else: break #Voltar
        else: break #Sair