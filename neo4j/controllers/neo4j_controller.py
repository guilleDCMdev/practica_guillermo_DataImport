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

    def get_personas_y_roles_empresa(self, empresa_name):
        query = """
        MATCH (p:Person)-[w:WORKS_AT]->(e:Company)
        WHERE e.name = $empresa_name
        RETURN p.name AS Persona, w.rol AS Rol
        """
        with self.model.driver.session() as session:
            result = session.run(query, empresa_name=empresa_name)
            personas_roles = [{"Persona": record["Persona"], "Rol": record["Rol"]} for record in result]
        return personas_roles
    
    def personas_con_rol_diferentes_empresas(self):
        query = """
        MATCH (p:Person)-[w:WORKS_AT]->(e:Company)
        WITH p, w.rol AS rol, COLLECT(DISTINCT e.name) AS empresas
        WHERE SIZE(empresas) > 1
        RETURN p.name AS Persona, rol, empresas
        """
        
        with self.model.driver.session() as session:
            result = session.run(query)
            personas_roles_empresas = [{"Persona": record["Persona"], "Rol": record["rol"], "Empresas": record["empresas"]} for record in result]
            
        return personas_roles_empresas
    
    def empresas_comunes_entre_personas(self, persona1, persona2):
        query = """
        MATCH (p1:Person)-[w1:WORKS_AT]->(e:Company), (p2:Person)-[w2:WORKS_AT]->(e)
        WHERE p1.name = $persona1 AND p2.name = $persona2
        RETURN e.name AS Empresa
        """
        
        with self.model.driver.session() as session:
            result = session.run(query, persona1=persona1, persona2=persona2)
            empresas_comunes = [record["Empresa"] for record in result]
            
        return empresas_comunes