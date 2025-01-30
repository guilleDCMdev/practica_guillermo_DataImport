from controllers.mongo_controller import MongoController
from models.entities import Project, Team, WorkInTeam
import requests

class MongoLoader:
    def __init__(self):
        self.controller = MongoController()

    def load_data(self):
        self.controller.create_database("teamwork")

        self.controller.create_collection("projects")

        self.controller.load_documents("../data/projects.csv", "projects", Project)
        self.controller.load_documents("../data/teams.csv", "teams", Team)
        self.controller.load_documents("../data/works_in_team.csv", "works_in_team", WorkInTeam)
        self.controller.load_favourite_pokemon("../data/favourite_pokemon.json")

    def close(self):
        self.controller.close_connection()
        
    def get_personas_por_equipo(self, team_id):
        return self.controller.get_personas_por_equipo(team_id)

    def equipos_con_numero_personas(self):
        pipeline = [
            {"$group": {"_id": "$team_id", "num_personas": {"$sum": 1}}}
        ]
        return self.controller.aggregate("works_in_team", pipeline)
    
    def equipos_con_numero_proyectos(self):
        pipeline = [
            {"$group": {"_id": "$project_id", "num_equipos": {"$sum": 1}}}
        ]
        return self.controller.aggregate("teams", pipeline)
    
    def personas_y_funciones_equipo(self, team_id):
        return self.controller.find("works_in_team", {"team_id": {"$in": team_id}})
    
    def obtener_proyecto_mas_diverso(self):
        equipo_mas_grande = self.controller.aggregate("works_in_team", [
            {"$group": {"_id": "$team_id", "num_personas": {"$sum": 1}}},
            {"$sort": {"num_personas": -1}},
            {"$limit": 1}
        ])
        
        if not equipo_mas_grande:
            return "No hay equipos disponibles."
        
        team_id = equipo_mas_grande[0]['_id']
        
        personas = self.controller.find("works_in_team", {"team_id": team_id})
        person_ids = [p["person_id"] for p in personas]
        
        pokemons = self.controller.find("favourite_pokemon", {"person_id": {"$in": person_ids}})
        pokemon_ids = [p["pokemon_id"] for p in pokemons]
        
        pokemon_types = set()
        for poke_id in pokemon_ids:
            url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for poke_type in data['types']:
                    pokemon_types.add(poke_type['type']['name'])
        
        proyecto = self.controller.find("teams", {"team_id": team_id}, {"project_id": 1, "_id": 0})
        project_id = proyecto[0]["project_id"] if proyecto else None
        
        return {
            "project_id": project_id,
            "team_id": team_id,
            "pokemon_types": list(pokemon_types)
        }