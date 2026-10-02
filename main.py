from paciente import Paciente

pacientes:list[Paciente] = [
    Paciente("12345678-9","Jack Skellerman",20,"Fonasa"),
    Paciente("98765432-1","James Shell", 16,"Isapre"),
]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un numero entero")

def agregar_paciente()->None:
    rut:str = input("Ingrese el rut del paciente: ")
    nombre:str = input("Ingrese el nombre del paciente: ")
    edad:int = leer_numero("Ingrese la edad del paciente: ")
    prevision:str = input("Ingrese el tipo de seguro del paciente: ")
    paciente:Paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente")

def buscar_paciente()->Paciente:
    rut:str = input("Ingrese el rut del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    print("Paciente no encontrado")
    return None

def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print("paciente encontrado:",paciente.nombre)
        print("Menu de edicion")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar prevision")
        print("0.- Salir")
        opcion:int = leer_numero("Ingrese una opcion: ")
        if opcion == 1:
            print("Su nombre actual es:",paciente.nombre)
            nombre:str = input("Ingrese el nuevo nombre: ")
            paciente.nombre = nombre
            print("Nombre actualizado exitosamente")
        elif opcion == 2:
            print("Su edad actual es:",paciente.edad)
            edad:int = leer_numero("Ingrese la nueva edad: ")
            paciente.edad = edad
            print("Edad actualizada exitosamente")
        elif opcion == 3:
            print("Su prevision actual es:",paciente.prevision)
            prevision:str = input("Ingrese la nueva prevision: ")
            paciente.prevision = prevision
            print("Prevision actualizada exitosamente")
        elif opcion ==  0:
            print("Saliendo del menu de edicion")
            print("No se realizaron cambios")
        else:
            print("Opcion invalida no se realizaron cambios")

def imprimir_paciente()->None:
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else: 
        print("No hay pacientes registrados")
def menu()->int:
    print("Menu Clinico")
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Imprimir un paciente")
    print("5.- Imprimir todos los pacientes")
    print("6.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def main()->None:
    while True:
        op = menu()
        if op == 1:
            print("Agregando paciente")
            agregar_paciente()
        elif op == 2:
            print("Editando paciente")
            editar_paciente()
        elif op == 3:
            print("Eliminando paciente")
        elif op == 4:
            print("Imprimiendo paciente")   
        elif op == 5:
            print("Imprimiendo todos los pacientes")
        elif op == 6:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()