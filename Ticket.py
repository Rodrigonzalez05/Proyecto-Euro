class Ticket():

    def __init__(self, ticket_id, match, seat):

        self.ticket_id = ticket_id
        self.match = match
        self.seat = seat

    def show_attr(self):

        return f'''

        Partido: {self.match.home.name} VS {self.match.away.name}
        Fecha: {self.match.date}
        
        Ticket_id: {self.ticket_id}
        Seat: {self.seat}
        
        '''