from base_datos import crear_tabla
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio


def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debes escribir un número entero")


def registrar_videojuego(servicio):
    nombre = input("Nombre del videojuego: ")
    precio = pedir_entero("Precio: ")
    stock = pedir_entero("Cantidad disponible: ")
    producto = servicio.registrar(nombre, precio, stock)
    print(f"Videojuego guardado con ID {producto.id}")


def mostrar_inventario(servicio):
    productos = servicio.listar()
    if len(productos) == 0:
        print("El inventario está vacío")
        return
    print(f"{'ID':<5}{'NOMBRE':<30}{'PRECIO':>12}{'STOCK':>8}")
    for p in productos:
        print(f"{p.id:<5}{p.nombre:<30}{p.precio:>12}{p.stock:>8}")


def buscar_videojuego(servicio):
    id = pedir_entero("ID del videojuego: ")
    p = servicio.buscar(id)
    print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: {p.precio} | Stock: {p.stock}")


def actualizar_videojuego(servicio):
    id = pedir_entero("ID del videojuego a actualizar: ")
    actual = servicio.buscar(id)
    print(f"Datos actuales: {actual.nombre} | {actual.precio} | {actual.stock}")
    nombre = input("Nuevo nombre: ")
    precio = pedir_entero("Nuevo precio: ")
    stock = pedir_entero("Nuevo stock: ")
    servicio.actualizar(id, nombre, precio, stock)
    print("Videojuego actualizado correctamente")


def eliminar_videojuego(servicio):
    id = pedir_entero("ID del videojuego a eliminar: ")
    servicio.eliminar(id)
    print("Videojuego eliminado correctamente")


def vender_unidades(servicio):
    id = pedir_entero("ID del videojuego: ")
    cantidad = pedir_entero("Cantidad a vender: ")
    p = servicio.vender(id, cantidad)
    print(f"Venta realizada. Stock de {p.nombre}: {p.stock}")


def menu(servicio):
    while True:
        print("\n--- INVENTARIO DE VIDEOJUEGOS ---")
        print("1. Registrar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar videojuego")
        print("5. Eliminar videojuego")
        print("6. Vender unidades")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                registrar_videojuego(servicio)
            elif opcion == "2":
                mostrar_inventario(servicio)
            elif opcion == "3":
                buscar_videojuego(servicio)
            elif opcion == "4":
                actualizar_videojuego(servicio)
            elif opcion == "5":
                eliminar_videojuego(servicio)
            elif opcion == "6":
                vender_unidades(servicio)
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, intenta de nuevo.")
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)


crear_tabla()
servicio = ProductoServicio(ProductoDAO())
menu(servicio)