from utils.config import get_config
from utils.data_loader import load_json
from controllers.mysql_controller import MySQLController

class MySQLLoader:
    def __init__(self):
        self.config = get_config()
        self.controller = MySQLController(self.config)

    def load_data(self):
        datasets = {
            'locations': '../data/locations.json',
            'skills': '../data/skills.json',
            'has_skill': '../data/has_skill.json',
            'pokemon': '../data/pokemon.json'
        }

        self.controller.create_database('pokemon')

        self.controller.create_table('locations', {'id': 'INT PRIMARY KEY', 'name': 'VARCHAR(255)', 'city': 'VARCHAR(255)'})
        self.controller.create_table('skills', {'id': 'INT PRIMARY KEY', 'name': 'VARCHAR(255)'})
        self.controller.create_table('has_skill', {'person_id': 'INT', 'skill_id': 'INT', 'proficiency': 'VARCHAR(255)'})
        self.controller.create_table('pokemon', {'pokemon_id': 'INT', 'description': 'TEXT', 'pokeGame': 'VARCHAR(255)'})

        for table, file_path in datasets.items():
            data = load_json(file_path)
            for record in data:
                self.controller.insert_data(table, record)