class Match():

    def __init__(self, match_id, number, home, away, date, group, stadium):
        self.match_id = match_id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium = stadium
        self.seats_vip = []
        self.seats_general = []
        self.asistencia = []

    def show_attr(self):

        return(f'''
        
    ---{self.home.name} VS {self.away.name}---

    Equipo local: {self.home.show_attr()}
    Equipo visitante: {self.away.show_attr()}
    Estadio: {self.stadium.show_attr()}
    Fecha: {self.date}
        
        ''')
    
    def resumen(self):
        return(f'''
        
    ---{self.home.name} VS {self.away.name}---
        
        ''')