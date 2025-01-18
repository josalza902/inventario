from productos import *
from inventario import *
from json import *
opc = 0

while opc != 6:
    print("bienvenido al inventario")
    print(f"\n presione 1 para insertar un producto")
    print(f"\n presione 2 para insertar un insertar inventario")
    print(f"\n presione 6 para salir")
    opc = int(input("digite un numero: "))
    match opc:
        case 1:
            print("insertar producto")
            insertar_productos()
        case 2:
            print("insertar inventario")
            insertar_inventario()
        case 6:
            print("usted ha salido del programa")
        case _:
            print("no es una opcion factible")

