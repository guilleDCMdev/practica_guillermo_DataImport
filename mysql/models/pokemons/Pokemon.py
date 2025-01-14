# pokemon.json
# ● pokemon_id:identificador único de pokemon.Tipo Integer.
# ● description: descripción del pokemon. Tipo string.
# ● pokeGame: nombre del juego pokemon. . Tipo string
class Pokemon:
    def __init__(self, pokemon_id, description, pokeGame):
        self.id = pokemon_id
        self.description = description
        self.pokeGame = pokeGame
    
    def __str__(self):
        return f'id: {self.id}, description: {self.description}, pokeGame: {self.pokeGame}'