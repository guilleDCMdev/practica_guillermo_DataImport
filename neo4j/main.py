from controllers.neo4j_controller import Neo4jController
from models.entities import Person, Empresa

def main():
    neo4j_controller = Neo4jController()

    print("Cargando nodos...")
    neo4j_controller.load_nodes("../data/persons.csv", "Person", Person)
    neo4j_controller.load_nodes("../data/empresas.csv", "Company", Empresa)

    print("Cargando relaciones...")
    neo4j_controller.load_relationships(
        "../data/works_at.csv", 
        "Person", 
        "Company", 
        "WORKS_AT", 
        "person_id", 
        "location_id", 
        extra_fields=["rol"]
    )

    print("Datos cargados correctamente.")
    neo4j_controller.close_connection()

if __name__ == "__main__":
    main()
