# skills.json:
# ● id: Identificador único para cada habilidad.Tipo entero.
# ● name: Nombre de la habilidad. Tipo string.
class Skill:
    def __init__(self, skill_id, name):
        self.id = skill_id
        self.name = name
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}'