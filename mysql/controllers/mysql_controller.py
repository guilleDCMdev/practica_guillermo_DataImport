# controllers/mysql_controller.py
from models.mysql_model import MySQLModel
from utils.data_loader import load_data
import json

class MySQLController:
    def __init__(self):
        self.model = MySQLModel()

    def load_nodes(self, file_path, table, entity_class):
        """
        Carga nodos en MySQL desde un archivo JSON.
        """
        entities = load_data(file_path, entity_class)
        for entity in entities:
            self.model.create_node(table, **entity.__dict__)

    def load_relationships(self, file_path, table, extra_fields=None):
        """
        Carga relaciones en MySQL desde un archivo JSON.
        """
        with open(file_path, mode='r', encoding='utf-8') as file:
            relationships = json.load(file)
            for row in relationships:
                extra_properties = {field: row[field] for field in (extra_fields or [])}
                self.model.create_relationship(table, **extra_properties)

    def close_connection(self):
        self.model.close()
