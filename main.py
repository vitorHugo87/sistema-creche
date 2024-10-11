import os

def mostrarMenu(menu):
    os.system('cls')
    if menu == 'inicio':
        print(' Menu '.center(20, '-'))
        print('1 - Cadastro')
        print('2 - Relatorios')
        print('3 - Sair')

def pedirComando(opcoes):
    while True:
        comando = input('Comando: ')
        if comando.isnumeric():
            comando = int(comando)
            if 0 < comando <= opcoes: return comando
            else: print('-=- Erro! Valor Invalido digitado! -=-')
        else: print('-=- Erro! Comando não pode conter letras! -=-')

while True:
    pedirComando(3)