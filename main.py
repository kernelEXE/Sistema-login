# sistema de login e senha
from time import sleep
import os
import getpass


clear = "cls" if os.name == "nt" else "clear"
time = "date"

usuarios ={
    "junior":"root123",
    "ana":"1234",
    "carlos":"admin"
}

while True:
    os.system(time)
    print("ATENÇÃO ESSE SISTEMA É DE USO EXCLUSIVO DA T.I , TODOS OS ACESSOS SÃO MONITORADOS POR LOG'S!")
    print("ATENCION ESTE SISTEMA ES DE USO EXCLUSIVO DE LA T.I , TODOS LOS ACCESOS SON MONITORADOS POR LOS LOG'S!")
    print("WARNING , THIS SYSTEM IS EXCLUSIVE OF THE USE IN I.T COMPANY, ALL THE ACESS IS MONITORING IN LOG'S")
    print("\n")
    login = input("Digite seu login :")
    senha = getpass.getpass()
    if login in usuarios and usuarios[login] == senha:
        os.system(clear)
        sleep(2)
        print("Acesso permitido")
        sleep(1)
        os.system(clear)
        print(f"Seja bem vindo {login}")
        break
    else:
        os.system(clear)
        print("Aguarde")
        sleep(2)
        os.system(clear)
        print("Acesso negado")
        sleep(2)
        os.system(clear)
