# utils/data_loader.py
import json

def load_data(file_path, entity_class):
    entities = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        for row in data:
            entity = entity_class(**row)
            entities.append(entity)
    return entities
