from models.mongo_model import MongoModel
from utils.data_loader import load_data
import json

class MongoController:
    def __init__(self):
        self.model = MongoModel()

    def load_documents(self, file_path, collection_name, entity_class):
        entities = load_data(file_path, entity_class)
        documents = [entity.__dict__ for entity in entities]
        self.model.insert_many(collection_name, documents)

    def load_favourite_pokemon(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.model.insert_many("favourite_pokemon", data)

    def close_connection(self):
        self.model.close()
