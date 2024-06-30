from Ticket import Ticket

class General(Ticket):

    def __init__(self, ticket_id, match, seat, descuento):
        super().__init__(ticket_id, match, seat)
        self.sub_total = 35
        self.descuento = descuento
        self.iva = (self.sub_total - self.descuento) * 0.16
        self.total = self.sub_total - self.descuento + self.iva

    def show_attr(self):

        return f'''
        
        *** General ***

        Partido: {self.match.home.name} VS {self.match.away.name}
        Fecha: {self.match.date}
        
        Ticket_id: {self.ticket_id}
        Asiento: {self.seat}
        
        Sub-total: {self.sub_total}
        Descuento: {self.descuento}
        Iva: {self.iva}
        
        Total: {self.total}
        
        '''
