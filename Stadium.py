class Stadium():

    def __init__(self, stadium_id, name, city, capacity, restaurants):
        self.stadium_id = stadium_id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants


    def show_attr(self):

        return(f'''
        
        ID: {self.stadium_id}
        Nombre: {self.name}
        Ubicacion: {self.city}
        Capacidad: {self.capacity}

        ''')


    def map(self, taken, i):

        asientos = self.capacity[i]

        for a in range(int(asientos/10)):
            fila = ["(x)" if f"{a}{b}" in taken else "( )" for b in range(10)]
            print(" ".join(fila))
