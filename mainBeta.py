from os import system as limpaTela

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
    if userLevel == 'admin':
        if tela == 'menu':
            printCor(' MENU '.center(30, '-'), 'azul')
            print('1 - Cadastro')
            print('2 - Atualizar Dados')
            print('3 - Exclusão de usuario')
            print('4 - Relatorios')
            printCor(('-' * 30), 'azul')
            return 4

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

exibicao('menu', 'admin')