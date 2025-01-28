from controllers.mongo_controller import MongoController
from models.entities import Project, Team, WorkInTeam

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
