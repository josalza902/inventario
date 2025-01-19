from productos import *
from datetime import *
from json import *

def tiempo():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    return f"el dia {fecha} // a las {hora_personalizada}"

def insertar_inventario():
    empezar_inventario = []

    try:
        with open("Crear productos/productos.json","r") as producto:
            cargar =json.load(producto) 
    except FileNotFoundError:
        print(" no existe por favor cree un producto ")
        cargar =[{}]
    
    print(cargar)
    try:
        codigo_producto = int(input("digite el codigo del producto: "))
    except ValueError:
        print("coloque numeros porfavor")
    
    for prod in cargar:
        if  prod["id"] == codigo_producto :
            try:
                cantidad_producto = int(input("digite la cantidad del producto: "))
            except ValueError:
                print("digite un numero no una letra")
            opc = 0
            while opc != 4:
                print("escoja en que bodega quiere ir oprima 4 para salir")
                print(f"\n presione 1 para bodega norte")
                print(f"\n presione 2 para bodega centro")
                print(f"\n presione 3 para bodega sur")
                print(f"\n presione 4 para bodega salir")
                opc = int(input("digite el numero de la bodega: "))
                match opc:
                    case 1:
                        
                        dato = 0
                        print("escoja si es entrada o salida")
                        print(f"\n presione 1 para entrada")
                        print(f"\n presione 2 para salida")
                        print(f"\n presione 3 para salir del menu")
                        dato  = int(input("digite el numero "))
                        if dato == 1:                        
                            inventario = {
                            "id" : codigo_producto,
                            "cantidad": cantidad_producto ,
                            "bodega":"bodega norte",
                            "entrada":"entrada producto",
                            "tiempo":tiempo()
                            }
                            
                            try:
                                with open("Crear productos/productos.json","w") as producto:
                                    for prod in cargar:

                                            if prod["id"] == codigo_producto: 
                                                prod["cantidad"] += cantidad_producto  
                                                json.dump(cargar, producto)
                                                break
                            except FileNotFoundError:
                                print(" no existe por favor cree un producto ")
                                cargar =[]
                            print(cargar)



                                
                        elif dato == 2:
                            inventario = {
                            "id" : codigo_producto,
                            "cantidad": cantidad_producto ,
                            "bodega":"bodega norte",
                            "entrada":"salida producto",
                            "tiempo":tiempo()
                            }
                            
                            try:
                                with open("Crear productos/productos.json","w") as producto:
                                    for prod in cargar:
                                        if prod["cantidad"] >= cantidad_producto:
                                            if prod["id"] == codigo_producto: 
                                                prod["cantidad"] -= cantidad_producto  
                                                json.dump(cargar, producto)
                                                break
                                        else:
                                            print("no hay saldo suficiente")
                                            break
                            except FileNotFoundError:
                                print(" no existe por favor cree un producto ")
                                cargar =[]
                            print(cargar)
                        else:
                            print("no se coloco un numero valido intentelo nuevamente")
                        
                    case 2:
                        dato = 0
                        print("escoja si es entrada o salida")
                        print(f"\n presione 1 para entrada")
                        print(f"\n presione 2 para salida")
                        print(f"\n presione 3 para salir del menu")
                        dato  = int(input("digite el numero "))
                        if dato == 1:
                            inventario = {
                            "id" : codigo_producto,
                            "cantidad": cantidad_producto ,
                            "bodega":"bodega centro",
                            "entrada":"entrada producto",
                            "tiempo":tiempo()
                         }
                            try:
                                with open("Crear productos/productos.json","w") as producto:
                                    for prod in cargar:
                                        if prod["id"] == codigo_producto: 
                                            prod["cantidad"] += cantidad_producto  
                                            json.dump(cargar, producto)
                                            break
                                    
                            except FileNotFoundError:
                                print(" no existe por favor cree un producto ")
                                cargar =[]
                            print(cargar)
                                
                        elif dato == 2:
                            inventario = {
                            "id" : codigo_producto,
                            "cantidad": cantidad_producto - prod["cantidad"] ,
                            "bodega":"bodega centro",
                            "entrada":"salida producto",
                            "tiempo":tiempo()
                            }
                            try:
                                with open("Crear productos/productos.json","w") as producto:
                                    for prod in cargar:
                                        if prod["cantidad"] >= cantidad_producto:
                                            if prod["id"] == codigo_producto: 
                                                prod["cantidad"] -= cantidad_producto  
                                                json.dump(cargar, producto)
                                                break
                                        else:
                                            print("no hay saldo suficiente")
                                            break
                            except FileNotFoundError:
                                print(" no existe por favor cree un producto ")
                                cargar =[]
                                print(cargar)
                        else:
                            print("no se coloco un numero valido intentelo nuevamente")
                    case 3:
                        dato = 0
                        print("escoja si es entrada o salida")
                        print(f"\n presione 1 para entrada")
                        print(f"\n presione 2 para salida")
                        print(f"\n presione 3 para salir del menu")
                        dato  = int(input("digite el numero "))
                        if dato == 1:
                            inventario = {
                            "id" : codigo_producto,
                            "cantidad": cantidad_producto + prod["cantidad"] ,
                            "bodega":"bodega occidente",
                            "entrada":"entrada producto",
                            "tiempo":tiempo()
                         }
                            try:
                                with open("Crear productos/productos.json","w") as producto:
                                    for prod in cargar:
                                        
                                        if prod["id"] == codigo_producto: 
                                            prod["cantidad"] += cantidad_producto  
                                            json.dump(cargar, producto)
                                            break
                                    
                            except FileNotFoundError:
                                print(" no existe por favor cree un producto ")
                                cargar =[]
                            print(cargar)    
                        elif dato == 2:
                                    inventario = {
                                        "id" : codigo_producto,
                                        "cantidad": cantidad_producto - prod["cantidad"] ,
                                        "bodega":"bodega occidente",
                                        "entrada":"salida producto",
                                        "tiempo":tiempo()
                                }
                                    try:
                                        with open("Crear productos/productos.json","w") as producto:
                                            for prod in cargar:
                                                if prod["cantidad"] >= cantidad_producto:
                                                    if prod["id"] == codigo_producto: 
                                                        prod["cantidad"] -= cantidad_producto  
                                                        json.dump(cargar, producto)
                                                    break
                                                else:
                                                    print("no hay saldo suficiente")
                                                    break

                                    except FileNotFoundError:
                                        print(" no existe por favor cree un producto ")
                                        cargar =[]
                                    print(cargar)
                        else:
                            print("no se coloco un numero valido intentelo nuevamente")
                    case 4:
                        print("salida")
                    case _:
                        print("esta no es una opcion viable escoja del 1 al 4")

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
    
            
    