# sistema de login e senha

from time import sleep # <- os imports responsaveis 
from datetime import datetime 
import os
import getpass
import json

with open ("senhas.json" , "r") as senha: # Dicionario de login e senha
    usuarios = json.load(senha)

def hora(): # Comando para setar hora onde quiser
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def limpar (): # Limpar tela quando necessario
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)

def menu(): # Menu principal
    hora()
    print ("=" * 4, "MENU PRINCIPAL", "=" *4)
    print("1 - x")
    print("2 - x")
    print("3 - x")
    print("4 - x")

def login (): # Sistema do Login
    print("ATENÇÃO ESSE SISTEMA É DE USO EXCLUSIVO DA T.I , TODOS OS ACESSOS SÃO MONITORADOS POR LOG'S!")
    print("ATENCION ESTE SISTEMA ES DE USO EXCLUSIVO DE LA T.I , TODOS LOS ACCESOS SON MONITORADOS POR LOS LOG'S!")
    print("WARNING , THIS SYSTEM IS EXCLUSIVE OF THE USE IN I.T COMPANY, ALL THE ACESS IS MONITORING IN LOG'S")
    print("\n")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    login = input("Digite seu login :")
    senha = getpass.getpass()

    if login in usuarios and usuarios[login] == senha:
        limpar()
        sleep(2)
        print("Acesso permitido")
        sleep(1)
        limpar()
        print(f"Seja bem vindo {login}")
        return True

    else:
        limpar()
        print("Aguarde")
        sleep(2)
        limpar()
        print("Acesso negado")
        sleep(2)
        limpar()
        sleep(2)
        return False
        
while True: # Loop de Login 
    if login():
        break
        
menu() # Apos login ok começa o programa