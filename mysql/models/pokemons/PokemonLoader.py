import json

from mysql.DatabaseConector import DatabaseConector # type: ignore

class PokemonLoader:
    def __init__(self, db: DatabaseConector):
        self.db = db

    def create_table(self):
        columns = """
            pokemon_id INT PRIMARY KEY,
            description TEXT,
            pokeGame VARCHAR(255)
        """
        self.db.create_table("pokemon", columns)

    def load_from_json(self, json_path):
        with open(json_path, "r") as file:
            pokemon_data = json.load(file)
        return [(pokemon["pokemon_id"], pokemon["description"], pokemon["pokeGame"]) for pokemon in pokemon_data]

    def insert_pokemon(self, pokemon_entries):
        for entry in pokemon_entries:
            data = f"{entry[0]}, '{entry[1]}', '{entry[2]}'"
            self.db.insert_data("pokemon", data)
