# locations.json
# ● id: Identificador único para cada ubicación.Tipo entero.
# ● name: Nombre de la localización. Tipo cadena.
# ● city: Ciudad donde se encuentra la ubicación.Tipo string.

class Location:
    def __init__(self, location_id, name, city):
        self.id = location_id
        self.name = name
        self.city = city
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}, city: {self.city}'