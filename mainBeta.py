from os import system as limpaTela

import solicita

admins = [
    {'id': 1, 'email': 'admin@gmail.com', 'senha': 'adm123', 'acesso': 'admin', 'nome': 'Walter White', 'salario': 3500.0},
    {'id': 2, 'email': 'admin2@gmail.com', 'senha': 'adm123', 'acesso': 'admin', 'nome': 'John Lark', 'salario': 4700.0}
]
alunos = [
    {'ra': 1, 'senha': '123456', 'acesso': 'aluno', 'nome': 'Heitor Pereira', 'idade': 2, 'mae': 'Heloisa Pereira', 'turma': 'A', 'notas': [85, 75], 'media': 80},
    {'ra': 2, 'senha': '654321', 'acesso': 'aluno', 'nome': 'Laura Souza', 'idade': 3, 'mae': 'Mariana Souza', 'turma': 'A', 'notas': [65, 45], 'media': 55},
    {'ra': 3, 'senha': '112233', 'acesso': 'aluno', 'nome': 'Pedro Oliveira', 'idade': 2, 'mae': 'Ana Oliveira', 'turma': 'A', 'notas': [70, 60], 'media': 65},
    {'ra': 4, 'senha': '789123', 'acesso': 'aluno', 'nome': 'Mariana Silva', 'idade': 3, 'mae': 'Luciana Silva', 'turma': 'A', 'notas': [85, 80], 'media': 82.5},
    
    {'ra': 5, 'senha': '445566', 'acesso': 'aluno', 'nome': 'Lucas Lima', 'idade': 1, 'mae': 'Fernanda Lima', 'turma': 'B', 'notas': [50, 40], 'media': 45},
    {'ra': 6, 'senha': '778899', 'acesso': 'aluno', 'nome': 'Sofia Santos', 'idade': 2, 'mae': 'Bruna Santos', 'turma': 'B', 'notas': [90, 80], 'media': 85},
    {'ra': 7, 'senha': '123789', 'acesso': 'aluno', 'nome': 'Rafael Ferreira', 'idade': 1, 'mae': 'Juliana Ferreira', 'turma': 'B', 'notas': [60, 50], 'media': 55},
    {'ra': 8, 'senha': '987321', 'acesso': 'aluno', 'nome': 'Felipe Lopes', 'idade': 2, 'mae': 'Carla Lopes', 'turma': 'B', 'notas': [70, 60], 'media': 65},
    
    {'ra': 9, 'senha': '987654', 'acesso': 'aluno', 'nome': 'Isabela Martins', 'idade': 0, 'mae': 'Cláudia Martins', 'turma': 'C', 'notas': [95, 85], 'media': 90},
    {'ra': 10, 'senha': '321987', 'acesso': 'aluno', 'nome': 'Giovanna Costa', 'idade': 1, 'mae': 'Patrícia Costa', 'turma': 'C', 'notas': [80, 75], 'media': 77.5},
    {'ra': 11, 'senha': '654123', 'acesso': 'aluno', 'nome': 'Arthur Ribeiro', 'idade': 2, 'mae': 'Roberta Ribeiro', 'turma': 'C', 'notas': [50, 45], 'media': 47.5},
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
            print('3 - Exclusão de Usuario')
            print('4 - Relatorios')
            print('5 - Sair')
            printCor(('-' * 30), 'azul')

        elif tela == 'cadastro':
            range = 4
            printCor(' CADASTRO '.center(30, '-'), 'azul')
            print('1 - Aluno')
            print('2 - Professor')
            print('3 - Administrador')
            print('4 - Voltar')
            printCor(('-' * 30), 'azul')

        elif tela == 'atualizacao':
            range = 4
            printCor(' ATUALIZAÇÃO '.center(30, '-'), 'azul')
            print('1 - Aluno')
            print('2 - Professor')
            print('3 - Administrador')
            print('4 - Voltar')
            printCor(('-' * 30), 'azul')

        elif tela == 'exclusao':
            range = 4
            printCor(' EXCLUSÃO '.center(30, '-'), 'azul')
            print('1 - Aluno')
            print('2 - Professor')
            print('3 - Administrador')
            print('4 - Voltar')
            printCor(('-' * 30), 'azul')

        elif tela == 'relatorios':
            range = 4
            printCor(' RELATORIOS '.center(30, '-'), 'azul')
            print('1 - Lista de Alunos')
            print('2 - Lista de Professores')
            print('3 - Lista de Admins')
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

    aluno['nome'] = solicita.nome()
    if aluno['nome'] == None: return None
    
    aluno['idade'] = solicita.idade()
    if aluno['idade'] == None: return None

    aluno['mae'] = solicita.nome()
    if aluno['mae'] == None: return None

    aluno['turma'] = solicita.turma()
    if aluno['turma'] == None: return None

    aluno['notas'] = []
    aluno['media'] = 0.0
    return aluno.copy()

def novoProf():
    prof = {}
    prof['id'] = profs[-1]['id'] + 1

    limpaTela('cls')

    prof['email'] = solicita.email()
    if prof['email'] == None: return None

    prof['senha'] = solicita.senha()
    if prof['senha'] == None: return None

    prof['acesso'] = 'prof'

    prof['nome'] = solicita.nome()
    if prof['nome'] == None: return None

    prof['turmas'] = solicita.turmas()
    if prof['turmas'] == None: return None

    prof['salario'] = solicita.salario()
    if prof['salario'] == None: return None

    return prof.copy()

def novoAdm():
    adm = {}
    adm['id'] = admins[-1]['id'] + 1

    limpaTela('cls')

    adm['email'] = solicita.email()
    if adm['email'] == None: return None

    adm['senha'] = solicita.senha()
    if adm['senha'] == None: return None

    adm['acesso'] = 'admin'

    adm['nome'] = solicita.nome()
    if adm['nome'] == None: return None

    adm['salario'] = solicita.salario()
    if adm['salario'] == None: return None
    
    return adm.copy()

def mostraAluno(aluno):
    printCor(f' RA: {aluno["ra"]} '.center(30, '-'), 'azul')
    print(f'Nome: {aluno["nome"]}')
    print(f'Idade: {aluno["idade"]}')
    print(f'Mãe: {aluno["mae"]}')

    print('Turma: ', end='')
    printCor(aluno["turma"], 'roxo')

    print('Notas: [', end='')
    for i, nota in enumerate(aluno['notas']):
        if nota >= 60: cor = 'verde'
        elif nota < 50: cor = 'vermelho'
        else: cor = 'amarelo'
        printCor(nota, cor, False)
        if i != len(aluno['notas']) - 1: print(', ', end='')
    print(']')

    print('Media: ', end='')
    if aluno['media'] >= 60: cor = 'verde'
    elif aluno['media'] < 50: cor = 'vermelho'
    else: cor = 'amarelo'
    printCor(f'{aluno["media"]:.1f}', cor)
        
    printCor(('-' * 30) + '\n', 'azul')

def mostraAlunos():
    limpaTela('cls')
    for a in alunos:
        mostraAluno(a)       

def mostraProf(prof):
    printCor(f' ID: {prof["id"]} '.center(30, '-'), 'azul')
    print(f'Nome: {prof["nome"]}')
    print(f'Email: {prof["email"]}')

    print('Turmas: ', end='')
    printCor(prof["turmas"], 'roxo')

    print('Salario: ', end='')
    printCor(f'R${prof["salario"]:.2f}', 'verde')
    printCor(('-' * 30) + '\n', 'azul')

def mostraProfs():
    limpaTela('cls')
    for p in profs:
        mostraProf(p)

def mostraAdmin(admin):
    printCor(f' ID: {admin["id"]} '.center(30, '-'), 'azul')
    print(f'Email: {admin["email"]}')
    print(f'Nome: {admin["nome"]}')

    print('Salario: ', end='')
    printCor(f'R${admin["salario"]:.2f}', 'verde')
    printCor(('-' * 30) + '\n', 'azul')

def mostraAdmins():
    limpaTela('cls')
    for a in admins:
        mostraAdmin(a)

def seleciona(entidade):
    if entidade == 'aluno': mostraAlunos()
    elif entidade == 'professor': mostraProfs()
    elif entidade == 'admin': mostraAdmins()

    while True:
            printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
            id = input(f'{"RA" if entidade == "aluno" else "ID"}: ')
            if id == 'cancelar': return None
            try: id = int(id)
            except ValueError:
                printCor(f'-=- Erro! {"RA" if entidade == "aluno" else "ID"} Invalido Digitado! -=-', 'vermelho')
                continue

            if entidade == 'aluno':
                for a in alunos:
                    if id == a['ra']: return a.copy()

            elif entidade == 'professor':
                for p in profs:
                    if id == p['id']: return p.copy()

            elif entidade == 'admin':
                for a in admins:
                    if id == a['id']: return a.copy()

            printCor(f'-=- Erro! {"RA" if entidade == "aluno" else "ID"} Não Encontrado! -=-', 'vermelho')

def excluir(entidade):
    tipo = entidade['acesso']
    
    limpaTela('cls')
    if tipo == 'aluno': mostraAluno(entidade)
    elif tipo == 'prof': mostraProf(entidade)
    elif tipo == 'admin': mostraAdmin(entidade)

    while True:
        printCor(f'Tem certeza que deseja excluir esse {tipo}? [S/N]: ', 'vermelho', False)
        cmd = input().upper().strip()
        if cmd not in 'SN':
            printCor('-=- Erro! Comando Invalido Digitado!', 'vermelho')
            continue
        break

    if cmd == 'N': return None
    else:
        if tipo == 'aluno':
            for i, a in enumerate(alunos):
                if entidade['ra'] == a['ra']:
                    del alunos[i]
                    return None

        elif tipo == 'prof':
            for i, p in enumerate(profs):
                if entidade['id'] == p['id']:
                    del profs[i]
                    return None
                    
        elif tipo == 'admin':
            for i, a in enumerate(admins):
                if entidade['id'] == a['id']:
                    del admins[i]
                    return None

def acharIndex(entidade):
    if entidade['acesso'] == 'aluno':
        for i, a, in enumerate(alunos):
            if a['ra'] == entidade['ra']: return i

def editarAluno(aluno):
    while True:
        limpaTela('cls')
        mostraAluno(aluno)
        
        while True:
            printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
            printCor('-- [Digite (salvar) para salvar alterações] --', 'amarelo')
            campo = input('Digite o campo a ser alterado: ')
            if campo == 'cancelar': return None
            elif campo == 'salvar': return aluno.copy()
            elif campo not in ['nome', 'idade', 'mae', 'turma', 'notas', 'media']:
                printCor('-=- Erro! Campo Invalido Digitado! -=-', 'vermelho')
                continue
            elif campo == 'media':
                printCor('-=- Erro! A média é calculada automaticamente com base nas notas! -=-', 'vermelho')
                continue
            break

        if campo == 'nome':
            while True: #Solicitação e validação do nome
                printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
                nome = input('Nome: ').title().strip()
                if nome == 'Cancelar': break
                elif not nome.replace(' ', '').isalpha():
                    printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
                    continue
                aluno['nome'] = nome
                break
        
        elif campo == 'idade':
            while True: #Solicitação e validação da idade
                try:
                    printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
                    idade = input('Idade [Para menores de 1 ano digite 0]: ')
                    if idade.lower() == 'cancelar': return None
                    idade = int(idade)
                    if idade < 0: raise ValueError()
                    elif idade > 4:
                        printCor('-=- Erro! A Creche só aceita crianças com até 4 anos de idade -=-', 'vermelho')
                        continue
                    aluno['idade'] = idade
                    break
                except:
                    printCor('-=- Erro! Idade Invalida Digitada! -=-', 'vermelho')

        elif campo == 'mae':
            while True: #Solicitação e validação do nome da mãe
                printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
                mae = input('Nome da mãe: ').title().strip()
                if mae == 'Cancelar': break
                elif not mae.replace(' ', '').isalpha():
                    printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
                    continue
                aluno['mae'] = mae
                break

        elif campo == 'turma':
            while True: #Solicitação e validação da turma
                printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
                turma = input('Turma: ').upper()
                if turma == 'CANCELAR': return None
                elif not turma.isalpha() or len(turma) != 1:
                    printCor('-=- Erro! Turma invalida digitada -=-', 'vermelho')
                    continue
                aluno['turma'] = turma
                break

        elif campo == 'notas':
            notas = []
            while True:
                try:
                    printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
                    printCor('-- [Digite (parar) para encerrar a atribuição de notas] --', 'amarelo')
                    nota = input()
                    if nota.lower() == 'cancelar': break
                    elif nota.lower() == 'parar':
                        aluno['notas'] = notas[:]
                        aluno['media'] = sum(notas) / len(notas)
                        break
                    nota = float(nota)
                    if nota < 0 or nota > 100: raise ValueError()
                    notas.append(nota)
                except ValueError:
                    printCor('-=- Erro! Nota invalida digitada! -=-', 'vermelho')
                    

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
                    if aluno != None: alunos.append(aluno.copy())
                elif cmd == 2: #Cadastro de Prof
                    prof = novoProf()
                    if prof != None: profs.append(prof.copy())
                elif cmd == 3: #Cadastro de Adm
                    adm = novoAdm()
                    if adm != None: admins.append(adm.copy())
                else: break #Voltar
        elif cmd == 2: #Atualização
            while True:
                cmd = exibicao('atualizacao', 'admin')
                if cmd == 1: #Atualizar Aluno
                    aluno = seleciona('aluno')
                    aluno = editarAluno(aluno)
                    if aluno != None: alunos[acharIndex(aluno)] = aluno.copy()
                else: break #Voltar
        elif cmd == 3: #Exclusão
            while True:
                cmd = exibicao('exclusao', 'admin')
                if cmd == 1: #Exclusão de Aluno
                    aluno = seleciona('aluno')
                    if aluno != None: excluir(aluno)
                elif cmd == 2: #Exclusão de Professor
                    prof = seleciona('professor')
                    if prof != None: excluir(prof)
                elif cmd == 3: #Exclusão de Administrador
                    admin = seleciona('admin')
                    if admin != None: excluir(admin)
                else: break #Voltar
        elif cmd == 4: #Relatorios
            while True:
                cmd = exibicao('relatorios', 'admin')
                if cmd == 1: #Lista de Alunos
                    mostraAlunos()
                    input('Pressione Enter para continuar...')
                elif cmd == 2: #Lista de Professores
                    mostraProfs()
                    input('Pressione Enter para continuar...')
                elif cmd == 3: #Lista de Admins
                    mostraAdmins()
                    input('Pressione Enter para continuar...')
                else: break #Voltar
        else: break #Sair