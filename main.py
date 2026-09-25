from paciente import Paciente

paciente:list[Paciente] = [
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
            pass
        elif op == 2:
            print("Editando paciente")
            pass
        elif op == 3:
            print("Eliminando paciente")
            pass
        elif op == 4:
            print("Imprimiendo paciente")   
            pass
        elif op == 5:
            print("Imprimiendo todos los pacientes")
            pass
        elif op == 6:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()