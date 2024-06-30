from Productos import Productos

class Alimento(Productos):

    def __init__(self, name, price, stock, tipo, adicional):
        super().__init__(name, price, stock, tipo)
        self.adicional = adicional

    def show_attr(self):

        return f'''
        
        Nombre: {self.name}
        Price: {self.price}
        Inventario: {self.stock}
        Adicional: {self.adicional}

        '''