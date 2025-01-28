from utils.config import get_config
from utils.data_loader import load_json
from controllers.mysql_controller import MySQLController

if __name__ == '__main__':
    config = get_config()
    controller = MySQLController(config)

    datasets = {
        'locations': '../data/locations.json',
        'skills': '../data/skills.json',
        'has_skill': '../data/has_skill.json',
        'pokemon': '../data/pokemon.json'
    }

    controller.create_table('locations', {'id': 'INT PRIMARY KEY', 'name': 'VARCHAR(255)', 'city': 'VARCHAR(255)'})
    controller.create_table('skills', {'id': 'INT PRIMARY KEY', 'name': 'VARCHAR(255)'})
    controller.create_table('has_skill', {'person_id': 'INT', 'skill_id': 'INT', 'proficiency': 'VarChar(255)'})
    controller.create_table('pokemon', {'pokemon_id': 'INT', 'description': 'TEXT', 'pokeGame': 'VARCHAR(255)'})

    for table, file_path in datasets.items():
        data = load_json(file_path)
        for record in data:
            controller.insert_data(table, record)