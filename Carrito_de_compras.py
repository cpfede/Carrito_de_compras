class Producto(object):
    """Clase base de los productos"""

    def __init__(self, nombre_modelo, precio, color, peso):
        """Inicializa los atributos:
           nombre_modelo (str): Nombre o modelo del producto
           precio (int): precio del producto
           color (str): color del producto
           peso (int): peso del producto en gramos
        """
        self.nombre_modelo = nombre_modelo
        self.precio = precio
        self.color = color
        self.peso = peso


class Laptoc(Producto):
    """Clase que modela una Laptoc hereda de la clase Producto"""

    def __init__(self, nombre_modelo, precio, color, peso, procesador, ram):
        """Inicializa los atributos:
           nombre_modelo (str): Heredado de Producto
           precio (int): Heredado de Producto
           color (str): Heredado de Producto
           peso (int): Heredado de Producto
           procesador (str): Procesador de la Laptoc
           ram (srt): Cantidad de memoria ram
        """
        super().__init__(nombre_modelo, precio, color, peso)
        self.procesador = procesador
        self.ram = ram


class Camara(Producto):
    """Clase que modela una Camara hereda de la clase Producto"""

    def __init__(self, nombre_modelo, precio, color, peso, tipo, numero_megapixeles):
        """Inicializa los atributos:
           nombre_modelo (str): Heredado de Producto
           precio (int): Heredado de Producto
           color (str): Heredado de Producto
           peso (int): Heredado de Producto
           tipo (str): tipo de la Camara debe ser "digital" o "reflex"
           numero_megapixeles (srt): numero de megapixeles de la Camara
        """
        super().__init__(nombre_modelo, precio, color, peso)
        try:
            assert tipo in ("digital", "reflex")
            self.tipo = tipo
        except AssertionError:
            print("tipo debe ser un (string) = digital o reflex")
        self.numero_megapixeles = numero_megapixeles


class Minicomponente(Producto):
    """Clase que modela un Minicomponente hereda de la clase Producto"""

    def __init__(self, nombre_modelo, precio, color, peso, potencia, reproductor_usb):
        """Inicializa los atributos:
           nombre_modelo (str): Heredado de Producto
           precio (int): Heredado de Producto
           color (str): Heredado de Producto
           peso (int): Heredado de Producto
           potencia (str): potencia del Minicomponente en Watts"
           reproductor_usb (srt): Indica si posee puerto USB debe ser "si" o "no"
        """
        super().__init__(nombre_modelo, precio, color, peso)
        self.potencia = potencia
        try:
            assert reproductor_usb in ("si", "no")
            self.reproductor_usb = reproductor_usb
        except AssertionError:
            print("reproductor_usb debe ser un (string) = si o no")


class Carrito(object):
    """Clase que modela un Carrito de compras"""

    def __init__(self, productos=list()):
        """Inicializa los atributos:
           productos (list): Lista que contiene los productos a comprar de tipo (Producto), si se deja vacio se
           inicializa una lista vacia
        """
        self.productos = productos

    def agregar_producto(self, producto):
        """Agrega @producto a la lista"""

        self.productos.append(producto)

    def quitar_producto(self, producto):
        """Quita @producto de la lista"""

        self.productos.remove(producto)

    def obtener_precio_total_compra(self):
        """Retorna el precio total de la compra"""

        precio_total = sum([producto.precio for producto in self.productos])
        return precio_total

    def obtener_detalle_compra(self):
        """Retorna el detalle de la compra total, nombre de producto y cantidad"""

        compra = [producto.nombre_modelo for producto in self.productos]
        orden_de_compra = [(nombre_modelo, compra.count(nombre_modelo)) for nombre_modelo in set(compra)]
        return self.imprimir_orden_de_compra(orden_de_compra)

    def imprimir_orden_de_compra(self, orden_de_compra):
        print("Producto Cantidad \n")
        for producto in orden_de_compra:
            print(producto[0], producto[1])