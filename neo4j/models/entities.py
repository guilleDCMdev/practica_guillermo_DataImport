class Person:
    def __init__(self, id, name, age):
        self.id = int(id)
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f'Persona: {self.name}'

    def __repr__(self):
        return f'Persona: {self.name}'

class Empresa:
    def __init__(self, id, name, sector):
        self.id = int(id)
        self.name = name
        self.sector = sector

    def __str__(self):
        return f'Empresa: {self.name}'

    def __repr__(self):
        return f'Empresa: {self.name}'
