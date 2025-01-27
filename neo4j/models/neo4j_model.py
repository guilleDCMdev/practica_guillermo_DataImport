from neo4j import GraphDatabase
from utils.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class Neo4jModel:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    def close(self):
        self.driver.close()

    def create_node(self, label, **properties):
        """
        Crea un nodo en Neo4j con una etiqueta específica y propiedades.
        """
        query = f"CREATE (n:{label} {{ {', '.join(f'{key}: ${key}' for key in properties.keys())} }})"
        with self.driver.session() as session:
            session.run(query, **properties)

    def create_relationship(self, start_label, end_label, rel_type, start_key, end_key, **properties):
        """
        Crea una relación entre dos nodos en Neo4j.
        """
        query = f"""
        MATCH (start:{start_label} {{id: $start_key}}), (end:{end_label} {{id: $end_key}})
        CREATE (start)-[r:{rel_type} {{ {', '.join(f'{key}: ${key}' for key in properties.keys())} }}]->(end)
        """
        with self.driver.session() as session:
            session.run(query, start_key=start_key, end_key=end_key, **properties)
