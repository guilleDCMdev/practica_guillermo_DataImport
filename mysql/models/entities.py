# models/entities.py
class Location:
    def __init__(self, id, name, city):
        self.id = int(id)
        self.name = name
        self.city = city

class Skill:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name

class Person:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name

class Pokemon:
    def __init__(self, pokemon_id, description, pokeGame):
        self.pokemon_id = int(pokemon_id)
        self.description = description
        self.pokeGame = pokeGame

class HasSkill:
    def __init__(self, person_id, skill_id, proficiency):
        self.person_id = int(person_id)
        self.skill_id = int(skill_id)
        self.proficiency = proficiency
