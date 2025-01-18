from productos import *
from json import *


def insertar_inventario():
    empezar_inventario = []
    try:
        with open("Crear productos/productos.json","r") as producto:
            cargar =json.load(producto) 
    except FileNotFoundError:
        print(" no existe por favor cree un producto ")
        cargar =[]
    
    print(cargar)


    codigo_producto = int(input("digite el codigo del producto: "))

    
    for prod in cargar:
        if  prod["id"] == codigo_producto :

            cantidad_producto = int(input("digite la cantidad del producto: "))
            bodega =  input("digite la bodega del producto: ")
            entrada_producto = input("digite salida o entrada: ")
            inventario = {
            "id" : codigo_producto,
            "cantidad": cantidad_producto,
            "bodega":bodega,
            "entrada":entrada_producto,
            }
            try:
                with open("Crear productos/inventario.json","r") as inventarios:
                    empezar_inventario =json.load(inventarios) 
            except FileNotFoundError:
                print(" no existe camos a crear un inventario ")

            empezar_inventario.append(inventario)
            
            try:
                with open("Crear productos/inventario.json", "w") as aña:
                    escribir = json.dumps(empezar_inventario)
                    aña.write(escribir)
    
            except:
                print("no se pudo crear")
        
        
        else:
            print("el codigo no esta")
            
    