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

while True:
    mostrarMenu('inicio')
    comando = pedirComando(3)
    if comando == 1:
        mostrarMenu('cadastro')
        comando = pedirComando(3)
        if comando == 3: continue
    if comando == 3: break
print('Finalizando Programa...')