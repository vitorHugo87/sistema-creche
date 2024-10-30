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

def nome():
    while True: #Solicitação e validação do nome
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        nome = input('Nome: ').title().strip()
        if nome == 'Cancelar': return None
        elif not nome.replace(' ', '').isalpha():
            printCor('-=- Erro! Nome Invalido Digitado -=-', 'vermelho')
            continue
        return nome
    
def idade():
    while True: #Solicitação e validação da idade
        try:
            printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
            idade = input('Idade [Para menores de 1 ano digite 0]: ')
            if idade.lower() == 'cancelar': return None
            idade = int(idade)
            if idade < 0: raise ValueError()
            elif idade > 4:
                printCor('-=- Erro! A Creche só aceita crianças com até 4 anos de idade -=-', 'vermelho')
                continue
            return idade
        except:
            printCor('-=- Erro! Idade Invalida Digitada! -=-', 'vermelho')

def turma():
    while True: #Solicitação e validação da turma
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        turma = input('Turma: ').upper()
        if turma == 'CANCELAR': return None
        elif not turma.isalpha() or len(turma) != 1:
            printCor('-=- Erro! Turma invalida digitada -=-', 'vermelho')
            continue
        return turma
    
def notas():
    notas = []
    while True:
        try:
            printCor('-- [Digite (cancelar) para voltar] --', 'amarelo')
            printCor('-- [Digite (parar) para encerrar a atribuição de notas] --', 'amarelo')
            nota = input()
            if nota.lower() == 'cancelar': return None
            elif nota.lower() == 'parar': return notas[:]
            nota = float(nota)
            if nota < 0 or nota > 100: raise ValueError()
            notas.append(nota)
        except ValueError:
            printCor('-=- Erro! Nota invalida digitada! -=-', 'vermelho')

def email():
    while True: #Solicitação e validação de email
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        email = input('Email: ')
        if email == 'cancelar': return None
        elif not '@' in email:
            printCor('-=- Erro! Email Invalido Digitado -=-', 'vermelho')
            continue
        return email
    
def senha():
    while True: #Solicitação e validação de senha
        printCor('-- [Digite (cancelar) para sair] --', 'amarelo')
        senha = input('Senha: ')
        if senha == 'cancelar': return None
        elif len(senha) < 6:
            printCor('-=- Erro! A senha deve ter ao minimo 6 caracteres -=-', 'vermelho')
            continue
        return senha
    
def turmas():
    turmas = []
    while True: #Solicitação e validação de turmas
        printCor('-- [Digite cancelar para sair] --', 'amarelo')
        printCor('-- [Digite parar para parar de adicionar turmas] --', 'amarelo')
        turma = input('Turma: ')
        if turma == 'cancelar': return None
        if turma == 'parar':
            if len(turmas) < 1:
                printCor('-=- Erro! Professor precisa possuir ao menos uma turma! -=-', 'vermelho')
                continue
            break
        elif not turma.isalpha() or len(turma) > 1:
            printCor('-=- Erro! Turma Invalida! -=-', 'vermelho')
            continue
        turmas.append(turma.upper())
    turmas.sort()
    return turmas[:]

def salario():
    while True: #Solicitação e validação de salario
        try:
            printCor('-- [Digite cancelar para sair] --', 'amarelo')
            salario = input('Salario: ').lower()
            if salario == 'cancelar': return None
            salario = float(salario)
            if salario < 0: raise ValueError()
            return salario
        except ValueError:
            printCor('-=- Erro! Valor invalido digitado -=-', 'vermelho')