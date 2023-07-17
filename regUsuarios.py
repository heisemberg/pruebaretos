import os
import core

diccUsuarios = {'data': []}
def LoadInfoUsuarios():
    global diccUsuarios
    if core.checkFile("usuarios.json"):
          diccUsuarios= core.LoadInfo("usuarios.json")
    else:
        core.crearInfo("usuarios.json",diccUsuarios)

def MainMenu():
    isUser = True
    os.system('clear')
    print('+','-'*55,'+')
    print("|{:^18}{}{:^19}|".format(' ','REGISTRO DE USUARIOS', ' '))
    print('+','-'*55,'+')
    print("1. Registrar Usuario")
    print("2. Salir")
    opcion = int(input(":)_"))
    if opcion == 1:
        data = {
            "nombre": input("Ingrese el Nombre : "),
            "cedula": input("Ingrese la Cedula: "),
            "telefono": input("Ingrese el Telefono: "),
            "correo": input("Ingrese el Correo: "),
        }
        diccUsuarios['data'].append(data)
        core.crearInfo("usuarios.json",data)
    elif opcion == 2:
        isUser = False
    if (isUser):
        MainMenu()
    