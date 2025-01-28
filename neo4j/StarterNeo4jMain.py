from controllers.neo4j_controller import Neo4jController
from models.entities import Person, Empresa

class Neo4jLoader:
    def __init__(self):
        self.controller = Neo4jController()

    def load_data(self):
        print("Cargando nodos...")
        self.controller.load_nodes("../data/persons.csv", "Person", Person)
        self.controller.load_nodes("../data/empresas.csv", "Company", Empresa)

        print("Cargando relaciones...")
        self.controller.load_relationships(
            "../data/works_at.csv", 
            "Person", 
            "Company", 
            "WORKS_AT", 
            "person_id", 
            "location_id", 
            extra_fields=["rol"]
        )

    def close(self):
        print("Datos cargados correctamente.")
        self.controller.close_connection()