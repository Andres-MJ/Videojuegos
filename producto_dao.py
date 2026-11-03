from base_datos import abrir_conexion
from modelo import Producto

class ProductoDAO:
    def crear(self, producto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES(?, ?, ?)"
        cursor.execute(sql, (producto.nombre, producto.precio, producto.stock))
        producto.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return producto


    def listar(self):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos")
        filas = cursor.fetchall()
        conexion.close()

        lista = []
        for fila in filas:
            lista.append(Producto(fila[0], fila[1], fila[2], fila[3]))
        return lista

    def buscar(self, id):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ? ", (id,))
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None
        return Producto(fila[0], fila[1], fila[2], fila[3])

    def actualizar(self, producto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        sql = ("UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?")
        cursor.execute (sql, (producto.nombre, producto.precio, producto.stock, producto.id))
        modificado = cursor.rowcount > 0
        conexion.commit()
        conexion.close()
        return modificado

    def eliminar(self, id):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        eliminado = cursor.rowcount > 0
        conexion.commit()
        conexion.close()
        return eliminado
