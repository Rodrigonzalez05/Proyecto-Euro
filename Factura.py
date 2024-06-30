class Factura:

    def __init__(self, producto, descuento):
        self.producto = producto
        self.descuento = descuento
        self.iva = self.producto.price * 1.16
        self.total = self.iva - self.descuento

    def show_attr(self):

        return f'''
        
        Producto: {self.producto.name}
        Descuento: {self.descuento}
        Total: {self.total}
        
        '''