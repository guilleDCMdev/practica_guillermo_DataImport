from controllers.neo4j_controller import Neo4jController

def main():
    neo4j_controller = Neo4jController()

    print("Cargando datos en Neo4j...")
    neo4j_controller.load_persons("../data/persons.csv")
    neo4j_controller.load_companies("../data/empresas.csv")
    neo4j_controller.load_works_at_relations("../data/works_at.csv")
    print("Datos cargados correctamente.")

    neo4j_controller.close_connection()

if __name__ == "__main__":
    main()
