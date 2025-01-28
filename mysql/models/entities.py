class Location:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

class Skill:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class HasSkill:
    def __init__(self, person_id, skill_id, proficiency):
        self.person_id = person_id
        self.skill_id = skill_id
        self.proficiency = proficiency

class Pokemon:
    def __init__(self, pokemon_id, description, pokeGame):
        self.pokemon_id = pokemon_id
        self.description = description
        self.pokeGame = pokeGame