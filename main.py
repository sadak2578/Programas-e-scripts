from os import system, popen, read, write
from time import sleep
from getpass import getpass
from datetime import datetime

# Qual é a ideia aqui
# Definir a função principal onde sera abrangido o login do administrador, dentro desta função terá toda a lógica central do código

# título
sleep(1.5)
system('cls')
sleep(1.5)	
print(r''' 
  ____  __ __  ______   ___   ___ ___   ____  ______    ___         __   ___   ___      ___ 
 /    T|  T  T|      T /   \ |   T   T /    T|      T  /  _]       /  ] /   \ |   \    /  _]
Y  o  ||  |  ||      |Y     Y| _   _ |Y  o  ||      | /  [_       /  / Y     Y|    \  /  [_ 
|     ||  |  |l_j  l_j|  O  ||  \_/  ||     |l_j  l_jY    _]     /  /  |  O  ||  D  YY    _]
|  _  ||  :  |  |  |  |     ||   |   ||  _  |  |  |  |   [_     /   \_ |     ||     ||   [_ 
|  |  |l     |  |  |  l     !|   |   ||  |  |  |  |  |     T    \     |l     !|     ||     T
l__j__j \__,_j  l__j   \___/ l___j___jl__j__j  l__j  l_____j     \____j \___/ l_____jl_____j
                                                                                            

''')
sleep(1.5)
print('entrando....')
sleep(5)
system('cls')
sleep(1)
# Função de inserir usuários novos no aquivo de texto


# Função de opções

# Opção sair:
def sair(opcao_sair=''):
	sleep(1)
	print('tem certeza que deseja sair?')
	sleep(1)
	while True:
		opcao_sair = input('Sair?: [S/N] ').strip().upper()
		if opcao_sair == 'S' or opcao_sair == 's':
			sleep(1)
			print('volte sempre')
			sleep(1)
			system('cls')
			break
		elif opcao_sair == 'N' or opcao_sair == 'n':
			sleep(1)
			print('continuando código...')
			sleep(1)
			system()
			break
		elif opcao_sair not in ('S','N','s','n'):
			sleep(1)
			print('opção inválida tente novamente')
			continue


# Função Central

def login_admin(nome_login='', senha_login='', verificacao_usuario_admin=dict, opcao1=''):
	
	verificacao_usuario_admin = {
	'user':'sfalmeida',
	'password': '123456',
	}
	
	while True:
		nome_login = input('Digite o usuário administrador: ')
		senha_login = getpass('Digite a senha: ')
		if nome_login == verificacao_usuario_admin['user'] and senha_login == verificacao_usuario_admin['password']:
			sleep(1)
			print('bem vindo')
			system('cls')
			sleep(1)
			print(''' 
			Escolha uma das opções a seguir:
			[1] Fechamento de chamado de usuário
			[2] Procurar um computador no AD
			[3] Sair''')
			
			opcao1 = input('Digite sua opção: ').strip().upper()
			
			if opcao1 == '3':
				sleep(1)
				sair()
				sleep(1)
				break
			
			
			
		elif nome_login != verificacao_usuario_admin['user'] or senha_login != verificacao_usuario_admin['password']:
			sleep(1.5)
			print('tente novamente')
			sleep(1.5)
			system('cls')
			sleep(1.5)	
login_admin(nome_login='', senha_login='', verificacao_usuario_admin=dict, opcao1='')
