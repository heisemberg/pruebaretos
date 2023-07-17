import gestionCitas
import regUsuarios
import os

if __name__ == "__main__":
    try:
        isActivate = True
        while isActivate:
            os.system('clear')
            print('+','-'*55,'+')
            print("|{:^21}{}{:^22}|".format(' ','MENU PRINCIPAL', ' '))
            print('+','-'*55,'+')
            print("1. Registrar Usuario")
            print("2. Gestion de Citas")
            print("3. Salir")

            opcion = int(input(":)_"))

            if opcion == 1:
                 regUsuarios.LoadInfoUsuarios()
                 regUsuarios.MainMenu()            
            elif opcion == 2:
                 gestionCitas.LoadInfoCitas()
                 gestionCitas.MainMenu()
            elif opcion == 3:
                isActivate = False
            else:
                print("Opcion no valida")
                input("Ingrese otra opcion")
    except ValueError:
        print("Valor no valido")