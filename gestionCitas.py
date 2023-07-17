import os
import core
from datetime import datetime
from datetime import timedelta

diccCitas = {'data': []}
def LoadInfoCitas():
    global diccCitas
    if core.checkFile("citas.json"):
          diccCitas = core.LoadInfo("citas.json")
    else:
        core.crearInfo("citas.json",diccCitas)

if core.checkFile("usuarios.json"):
          diccUsuarios = core.LoadInfo("usuarios.json")

def MainMenu():
    os.system('clear')
    isActivate = True
    print('+','-'*55,'+')
    print("|{:^20}{}{:^21}|".format(' ','GESTION DE CITAS', ' '))
    print('+','-'*55,'+')
    print("1. Agregar cita")
    print("2. Buscar Cita")
    print("3. Modificar Cita")
    print("4. Cancelar cita")
    print("5. Salir")
    opcion = int(input(":)_"))
    
    if opcion == 1:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^22}{}{:^21}|".format(' ','BUSCAR USUARIO', ' '))
        print('+','-'*55,'+')
        print("1. Registrar cita con el documento del paciente")
        print("2. Registrar cita con el nombre del paciente")
        print("3. Salir")
        op = int(input(":)_"))
        
        if op == 1:
            cedula = input("Ingrese la cedula del paciente: ")
            for i, item in enumerate(diccUsuarios['data']):
                if item['cedula'] == cedula:
                    print('+','-'*55,'+')
                    print("|{:^16}{}{:^16}|".format(' ','DATOS DEL PACIENTE', ' '))
                    print('+','-'*55,'+')
                    paciente = item['nombre']
                    telefono = item['telefono']
                    correo = item['correo']
                    print(f'Nombre del Paciente: {paciente}\nCedula del paciente: {cedula}\nTelefono: {telefono}\nCorreo Electronico: {correo}')
                    consulta = input('Ingrese el motivo de la consulta: ')
                    input('Confirmar cita "Press Enter"')
            regCita = True
            while regCita:
                if len(diccCitas['data']) == 0:
                    id = 1
                    now = datetime.now()
                    newDate = now + timedelta(days=1)
                    horaIni = datetime(now.year, now.month, newDate.day,8,00,00,00000)
                    horaFin = datetime(now.year, now.month, newDate.day,17,00,00,00000)
                    data = {
                        'id': id,
                        'fecha': str(horaIni),
                        'nombre': paciente,
                        'cedula': cedula,
                        'consulta': consulta
                    }
                    diccCitas['data'].append(data)
                    core.crearInfo("citas.json",data)
                else:
                    id = diccCitas['data'][-1]['id']+1
                    horaIni = datetime.strptime(diccCitas["data"][-1]['fecha'],'%Y-%m-%d %H:%M:%S')
                    horaFin = datetime(horaIni.year, horaIni.month, horaIni.day,17,00,00,00000)
                    if horaIni < horaFin:
                        horaIni = horaIni + timedelta(hours=1)
                        data = {
                            'id': id,
                            'fecha': str(horaIni),
                            'nombre': paciente,
                            'cedula': cedula,
                            'consulta': consulta
                        }
                        diccCitas['data'].append(data)
                        core.crearInfo("citas.json",data)
                    else:
                        id = diccCitas['data'][-1]['id']+1
                        horaIni = horaIni + timedelta(days=1,hours=-9)
                        horaFin = datetime(horaIni.year, horaIni.month, horaIni.day,17,00,00,00000)

                        data = {
                            'id': id,
                            'fecha': str(horaIni),
                            'nombre': paciente,
                            'cedula': cedula,
                            'consulta': consulta
                        }
                        diccCitas['data'].append(data)
                        core.crearInfo("citas.json",data)
                regCita = bool(input('Pulse "Enter" para salir'))

        elif op == 2:
            paciente = input("Ingrese el nombre del paciente: ")
            for i, item in enumerate(diccUsuarios['data']):
                 if item['nombre'] == paciente:
                    print('+','-'*55,'+')
                    print("|{:^20}{}{:^20}|".format(' ','DATOS DEL PACIENTE', ' '))
                    print('+','-'*55,'+')
                    cedula = item['cedula']
                    telefono = item['telefono']
                    correo = item['correo']
                    print(f'Nombre del Paciente: {paciente}\nCedula del paciente: {cedula}\nTelefono: {telefono}\nCorreo Electronico: {correo}')
                    consulta = input('Ingrese el motivo de la consulta: ')
                    input('Confirmar cita "Press Enter"')
            regCita = True
            while regCita:
                if len(diccCitas['data']) == 0:
                    id = 1
                    now = datetime.now()
                    newDate = now + timedelta(days=1)
                    horaIni = datetime(now.year, now.month, newDate.day,8,00,00,00000)
                    horaFin = datetime(now.year, now.month, newDate.day,17,00,00,00000)
                    data = {
                        'id': id,
                        'fecha': str(horaIni),
                        'nombre': paciente,
                        'cedula': cedula,
                        'consulta': consulta
                    }
                    diccCitas['data'].append(data)
                    core.crearInfo("citas.json",data)
                else:
                    id = diccCitas['data'][-1]['id']+1
                    horaIni = datetime.strptime(diccCitas["data"][-1]['fecha'],'%Y-%m-%d %H:%M:%S')
                    horaFin = datetime(horaIni.year, horaIni.month, horaIni.day,17,00,00,00000)
                    if horaIni < horaFin:
                        horaIni = horaIni + timedelta(hours=1)
                        data = {
                            'id': id,
                            'fecha': str(horaIni),
                            'nombre': paciente,
                            'cedula': cedula,
                            'consulta': consulta
                        }
                        diccCitas['data'].append(data)
                        core.crearInfo("citas.json",data)
                    else:
                        id = diccCitas['data'][-1]['id']+1
                        horaIni = horaIni + timedelta(days=1,hours=-9)
                        horaFin = datetime(horaIni.year, horaIni.month, horaIni.day,17,00,00,00000)

                        data = {
                            'id': id,
                            'fecha': str(horaIni),
                            'nombre': paciente,
                            'cedula': cedula,
                            'consulta': consulta
                        }
                        diccCitas['data'].append(data)
                        core.crearInfo("citas.json",data)
                regCita = bool(input('Pulse "Enter" para salir'))
        else:
            input('Para continuar "Press Enter"')        


    elif opcion == 2:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^23}{}{:^23}|".format(' ','BUSCAR CITA', ' '))
        print('+','-'*55,'+')
        print("1. Buscar por Cedula")
        print("2. Buscar por Fecha")
        print("3. Salir")
        opc = int(input(":)_"))

        if opc == 1:
            cedula = input("Ingrese la cedula del paciente: ")
            for j, cita in enumerate(diccCitas['data']):
                if cedula == cita['cedula']:
                    nombre = cita['nombre']
                    fecha = cita['fecha']
                    consulta = cita['consulta']
                    print('+','-'*55,'+')
                    print(f'Nombre del Paciente: {nombre}\nCedula del paciente: {cedula}\nFecha Cita: {fecha}\nMotivo consulta: {consulta}')
                    print('+','-'*55,'+')
                    input('Para continuar "Press Enter"')

        elif opc == 2:
            fecha = input('Ingrese la fecha de la cita a consultar en formato "yyyy-mm-dd hh": ')
            for k, citas in enumerate(diccCitas['data']):
                if fecha in citas['fecha']:
                    cedula = citas['cedula']
                    nombre = citas['nombre']
                    fecha = citas['fecha']
                    consulta = citas['consulta']
                    print('+','-'*55,'+')
                    print(f'Nombre del Paciente: {nombre}\nCedula del paciente: {cedula}\nFecha Cita: {fecha}\nMotivo consulta: {consulta}')
                    print('+','-'*55,'+')
                    input('Para continuar "Press Enter"')
        else:
            input('Para continuar "Press Enter"')

    elif opcion == 3:
        id = input('Ingrese el "id"  de la cita a retroalimentar: ')
        for l, citam in enumerate(diccCitas['data']):
            if int(id) == citam['id']:
                citam['consulta'] +=' **Actualizacion** '+input('Registrar Resultado de la consulta: ')
                core.EditarData("citas.json",diccCitas)

    elif opcion == 4:
        id = input('Ingrese el "id"  de la cita a cancelar: ')
        for m, citac in enumerate(diccCitas['data']):
            if int(id) == citac['id']:
                diccCitas['data'].remove(citac)
                core.EditarData("citas.json",diccCitas)

    elif opcion == 5:
        isActivate = False
    if isActivate:
         MainMenu()