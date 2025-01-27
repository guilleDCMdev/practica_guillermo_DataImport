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
