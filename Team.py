class Team():

    def __init__(self, team_id, code, name, group):
        self.team_id = team_id
        self.code = code
        self.name = name
        self.group = group

    def show_attr(self):

        return(f'''
        
        ID: {self.team_id}
        Nombre: {self.name}
        Codigo: {self.code}
        Grupo: {self.group}
        
        ''')