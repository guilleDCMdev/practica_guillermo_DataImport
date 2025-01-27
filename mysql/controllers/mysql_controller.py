from models.mysql_model import insert_location, insert_skill, insert_has_skill, insert_pokemon
    
def load_locations(locations_data):
    for location in locations_data:
        insert_location(location)

def load_skills(skills_data):
    for skill in skills_data:
        insert_skill(skill)

def load_has_skills(has_skills_data):
    for has_skill in has_skills_data:
        insert_has_skill(has_skill)

def load_pokemons(pokemons_data):
    for pokemon in pokemons_data:
        insert_pokemon(pokemon)
