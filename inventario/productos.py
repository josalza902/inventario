from json import *

crear_producto = []
def insertar_productos():
 
    codigo_producto = input("digite el codigo del producto: ")
    nombre_producto = input("digite el nombre del producto: ")
    proveedor_producto = input("digite el nombre del proveedor: ")
    bodega = input
    productos = {
        "id" : codigo_producto,
        "nombre": nombre_producto,
        "proveedor":proveedor_producto,
    }
    
    try:
        with open("productos.json","r") as l:
             crear_producto = load(l)  
             crear_producto.append(productos)
    except:
        print(" no existe vamo a crearla ")

    
 
    try:
        with open("productos.json", "w") as añadir:
            añadir.write(dumps(crear_producto))
    except:
        print("no se pudo crear")
    

