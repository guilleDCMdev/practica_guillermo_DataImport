from utils.data_loader import load_json_data
from controllers.mysql_controller import load_locations, load_skills, load_has_skills, load_pokemons
from models.mysql_model import create_tables

def main():

    create_tables()

    # Cargar datos de los archivos JSON
    locations_data = load_json_data('../data/locations.json')
    skills_data = load_json_data('../data/skills.json')
    has_skills_data = load_json_data('../data/has_skill.json')
    pokemons_data = load_json_data('../data/pokemon.json')

    # Cargar los datos en la base de datos
    load_locations(locations_data)
    load_skills(skills_data)
    load_has_skills(has_skills_data)
    load_pokemons(pokemons_data)

if __name__ == "__main__":
    main()
