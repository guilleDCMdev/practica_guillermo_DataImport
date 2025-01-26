from neo4j import GraphDatabase
from utils.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class Neo4jModel:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    def close(self):
        self.driver.close()

    def create_person(self, person):
        query = """
        CREATE (:Person {id: $id, name: $name, age: $age})
        """
        with self.driver.session() as session:
            session.run(query, id=person.id, name=person.name, age=person.age)

    def create_company(self, company):
        query = """
        CREATE (:Company {id: $id, name: $name, sector: $sector})
        """
        with self.driver.session() as session:
            session.run(query, id=company.id, name=company.name, sector=company.sector)

    def create_works_at_relationship(self, person_id, company_id, role, location_id):
        query = """
        MATCH (p:Person {id: $person_id}), (c:Company {id: $company_id})
        CREATE (p)-[:WORKS_AT {role: $role, location_id: $location_id}]->(c)
        """
        with self.driver.session() as session:
            session.run(query, person_id=person_id, company_id=company_id, role=role, location_id=location_id)
