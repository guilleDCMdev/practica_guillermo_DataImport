from controllers.mongo_controller import MongoController
from models.entities import Project, Team, WorkInTeam

def main():
    mongo_controller = MongoController()

    print("Cargando proyectos...")
    mongo_controller.load_documents("../data/projects.csv", "projects", Project)

    print("Cargando equipos...")
    mongo_controller.load_documents("../data/teams.csv", "teams", Team)

    print("Cargando relaciones de trabajo en equipo...")
    mongo_controller.load_documents("../data/works_in_team.csv", "works_in_team", WorkInTeam)

    print("Cargando favoritos de Pokémon...")
    mongo_controller.load_favourite_pokemon("../data/favourite_pokemon.json")

    print("Datos cargados correctamente.")
    mongo_controller.close_connection()

if __name__ == "__main__":
    main()
