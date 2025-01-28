class Project:
    def __init__(self, project_id, name, description, location_id, company_id):
        self.project_id = int(project_id)
        self.name = name
        self.description = description
        self.location_id = int(location_id)
        self.company_id = int(company_id)

    def __str__(self):
        return f'Project: {self.name}'

    def __repr__(self):
        return f'Project: {self.name}'


class Team:
    def __init__(self, team_id, name, description, project_id):
        self.team_id = int(team_id)
        self.name = name
        self.description = description
        self.project_id = int(project_id)

    def __str__(self):
        return f'Team: {self.name}'

    def __repr__(self):
        return f'Team: {self.name}'


class WorkInTeam:
    def __init__(self, person_id, team_id, rol):
        self.person_id = int(person_id)
        self.team_id = int(team_id)
        self.rol = rol

    def __str__(self):
        return f'WorkInTeam: {self.rol}'

    def __repr__(self):
        return f'WorkInTeam: {self.rol}'


class FavouritePokemon:
    def __init__(self, person_id, pokemon_id, dateCaptured):
        self.person_id = int(person_id)
        self.pokemon_id = int(pokemon_id)
        self.dateCaptured = dateCaptured

    def __str__(self):
        return f'FavouritePokemon: {self.pokemon_id}'

    def __repr__(self):
        return f'FavouritePokemon: {self.pokemon_id}'
