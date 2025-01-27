# main.py
from controllers.mysql_controller import MySQLController
from models.entities import Person, Skill, Location, Pokemon, HasSkill

def main():
    mysql_controller = MySQLController()

    # Cargar nodos
    print("Cargando nodos...")
    mysql_controller.load_nodes('locations.json', 'locations', Location)
    mysql_controller.load_nodes('skills.json', 'skills', Skill)
    mysql_controller.load_nodes('persons.json', 'persons', Person)
    mysql_controller.load_nodes('pokemons.json', 'pokemons', Pokemon)

    # Cargar relaciones
    print("Cargando relaciones...")
    mysql_controller.load_relationships('has_skill.json', 'has_skill', extra_fields=["proficiency"])

    print("Datos cargados correctamente.")
    mysql_controller.close_connection()

if __name__ == "__main__":
    main()
