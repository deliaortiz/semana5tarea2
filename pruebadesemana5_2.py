import os

productos = []#lista donde se van a guadar los datos

def añadir_producto():
    
    nombre = input("Ingrese el nombre: ")

    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Por favor, ingrese un precio valido")

    while True:
            try:
                cantidad = int(input("Ingrese la cantidad: \n"))
                break
            except ValueError:
                print("Por favor, ingrese una cantidad valida")

    nuevo_producto = {
    'nombre': nombre,
    'precio': precio,
    'cantidad': cantidad
    }
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' añadido exitosamente")

def ver_productos():
    #verifica si la lista productos está vacia
    if not productos:
        print("NO hay productos cargados.")
        return
    print("Productos Disponibles")
    for i, producto in enumerate (productos):#.2f es para que devulve dos numero despue de la coma
        print(f"{i + 1}:Nombre: {producto['nombre']}, Precio: {producto['precio']:.2f},Cantidad: {producto['cantidad']}")
    

def actualizar_producto():
    ver_productos()

    if not productos:
        print("NO hay productos disponibles")
        return#se resta menos 1 ya que el indice empieza por la posicion 0
    
    indice = int(input("Ingrese el numero del producto que desea actualiar: ")) -1
    if 0 <= indice < len(productos):
        nombre = input("Ingrese el producto, si no desea cambiar dejelo vacio: ")
        precio = input("Ingrese el precio, si no desea cambiar dejelo vacio: ")
        cantidad = input("Ingrese la cantidad, si no desea cambiar dejelo vacio: ")

        if nombre:
            productos[indice]['nombre'] = nombre
        if precio:
            productos[indice]['precio'] = float(precio)
        if cantidad: 
            productos[indice]['cantidad'] = int(cantidad)

        print("Actualizado con éxito")
    else:
        print("Indice incorrecto, ingrese un indice valido")



def eliminar_producto():
    ver_productos()

    if not productos:
        return 
    
    indice = int(input("Ingrese el numero del indice a eliminar: "))-1
    if 0 <= indice < len(productos):
        eliminar = productos.pop(indice)
        print(f"Producto '{eliminar['nombre']}' eliminado exitosamente.")
    else:
        print("Indice invalido")
    

def guardar_datos():
    with open('productos.txt','w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados")
    

def cargar_datos():
    global productos
    if os.path.exists('productos.txt'):#comprueba que existe el archivo
        with open('productos.txt','r')as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')#strip elimina espacios al inicio del nombre y slipt elimina el espacio al final separando con ,
                productos.append ({
                    'nombre':nombre,
                    'precio':float(precio),
                    'cantidad':int(cantidad)
            })
        #print("Datos cargados desde productos.txt")
    else:
        print("No se encontró el archivo productos.txt.")


def menu():
    cargar_datos()#llama a los datos
    while True:
       
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: \n")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
