from modelo import Producto


class ProductoServicio:
    def __init__(self, dao):
        self.dao = dao

    def _validar(self, nombre, precio, stock):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

    def registrar(self, nombre, precio, stock):
        self._validar(nombre, precio, stock)
        producto = Producto(None, nombre.strip(), precio, stock)
        return self.dao.crear(producto)

    def listar(self):
        return self.dao.listar()

    def buscar(self, id):
        producto = self.dao.buscar(id)
        if producto is None:
            raise ValueError("No existe un videojuego con ese ID")
        return producto

    def actualizar(self, id, nombre, precio, stock):
        self.buscar(id)  
        self._validar(nombre, precio, stock)
        producto = Producto(id, nombre.strip(), precio, stock)
        self.dao.actualizar(producto)
        return producto

    def eliminar(self, id):
        self.buscar(id)  
        self.dao.eliminar(id)

    def vender(self, id, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")
        producto = self.buscar(id)
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente: solo hay {producto.stock} unidades"
            )
        producto.stock = producto.stock - cantidad
        self.dao.actualizar(producto)
        return producto