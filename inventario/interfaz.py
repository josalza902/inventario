from productos import *
opc = 0

while opc != 6:
    print("bienvenido al inventario")
    print(f"\n presione 1 para insertar un producto")
    opc = int(input("digite un numero: "))
    match opc:
        case 1:
            print("insertar producto")
            insertar_productos()
        case _:
            print("no es una opcion factible")

