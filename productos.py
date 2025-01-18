import json 




def insertar_productos():
    crear_producto = []
    codigo_producto = int(input("digite el codigo del producto: "))
    nombre_producto = input("digite el nombre del producto: ") 
    proveedor_producto = input("digite el nombre del proveedor: ")
    productos = {
        "id":codigo_producto,
        "nombre":nombre_producto,
        "proveedor":proveedor_producto,
    }
    
    try:
        with open("Crear productos/productos.json","r") as producto:
            crear_producto = json.load(producto)  
            
    except FileNotFoundError:
        print(" no existe vamo a crearla ")

    crear_producto.append(productos)

    try:
        with open("Crear productos/productos.json", "w") as añadir:
            escribir = json.dumps(crear_producto)
            añadir.write(escribir)
    
    except:
        print("no se pudo crear")
    

