import json
import requests
from getpass import getpass

a=input('Entre com a matrícula:  \n')

def Consulta_suap(matricula):
	r = requests.get('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/', auth=(a,getpass('\nSenha: ')))
	print(r.text)
	print(r.url)
	return matricula


if __name__ == '__main__':
	Consulta_suap(a)
