class Client():

    def __init__(self, name, dni, age):
        self.name = name
        self.dni = dni
        self.age = age
        self.tickets = []

    def show_tickets(self):
        for ticket in self.tickets:
            print(ticket.show_attr())

    def show_attr(self):

        return f'''
        
        Nombre: {self.name}
        Cedula: {self.dni}
        Edad: {self.age}
        Cantidad de Tickets comprados: {len(self.tickets)}

        '''
            