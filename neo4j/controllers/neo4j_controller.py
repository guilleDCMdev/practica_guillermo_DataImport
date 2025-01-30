from models.neo4j_model import Neo4jModel
from utils.data_loader import load_data
from models.entities import Person, Empresa
import csv

class Neo4jController:
    def __init__(self):
        self.model = Neo4jModel()

    def load_nodes(self, file_path, label, entity_class):
        """
        Carga nodos en Neo4j desde un archivo CSV.
        """
        entities = load_data(file_path, entity_class)
        for entity in entities:
            self.model.create_node(label, **entity.__dict__)

    def load_relationships(self, file_path, start_label, end_label, rel_type, start_key_field, end_key_field, extra_fields=None):
        """
        Carga relaciones en Neo4j desde un archivo CSV.
        """
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                start_key = int(row[start_key_field])
                end_key = int(row[end_key_field])
                extra_properties = {field: row[field] for field in (extra_fields or [])}
                self.model.create_relationship(start_label, end_label, rel_type, start_key, end_key, **extra_properties)

    def close_connection(self):
        self.model.close()

    # Personas y sus roles en una empresa concreta
    # MATCH (p:Person)-[r:WORKS_AT]->(e:Company)
    # WHERE e.name = "NombreDeLaEmpresa"
    # RETURN p.name, r.rol
    def personas_y_roles_empresa(self, empresa):
        query = f"MATCH (p:Person)-[r:WORKS_AT]->(e:Company) WHERE e.name = '{empresa}' RETURN p.name, r.rol"
        return self.model.execute_query(query)
    
    # MATCH (p1:Person)-[r1:WORKS_AT]->(e1:Company),
    #   (p2:Person)-[r2:WORKS_AT]->(e2:Company)
    # WHERE p1 <> p2 AND r1.rol = r2.rol AND e1 <> e2
    # RETURN p1.name, e1.name, r1.rol, p2.name, e2.name
    def personas_con_rol_diferentes_empresas(self):
        query = "MATCH (p1:Person)-[r1:WORKS_AT]->(e1:Company), (p2:Person)-[r2:WORKS_AT]->(e2:Company) WHERE p1 <> p2 AND r1.rol = r2.rol AND e1 <> e2 RETURN p1.name, e1.name, r1.rol, p2.name, e2.name"
        return self.model.execute_query(query)
    
    # MATCH (p1:Person)-[:WORKS_AT]->(e:Company)<-[:WORKS_AT]-(p2:Person)
    # WHERE p1.name = "Persona1" AND p2.name = "Persona2"
    # RETURN e.name
    def empresas_comunes_entre_personas(self, persona1, persona2):
        query = f"MATCH (p1:Person)-[:WORKS_AT]->(e:Company)<-[:WORKS_AT]-(p2:Person) WHERE p1.name = '{persona1}' AND p2.name = '{persona2}' RETURN e.name"
        return self.model.execute_query(query)
    
    # MATCH (p:Person)
    # WHERE p.id IN [LISTA_DE_PERSON_ID]
    # RETURN p.name
    def personas_y_funciones_equipo(self, team_id):
        query = f"MATCH (p:Person) WHERE p.id IN {team_id} RETURN p.name"
        return self.model.execute_query(query)

    # MATCH (p:Person)
    # WHERE p.id IN [LISTA_DE_PERSON_ID]
    # RETURN p.name
    def personas_y_funciones_equipo(self, personas):
        query = f"MATCH (p:Person) WHERE p.id IN {personas} RETURN p.name"
        return self.model.execute_query(query)
     