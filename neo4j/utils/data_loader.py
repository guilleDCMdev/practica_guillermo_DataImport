import csv

def load_data(file_path, entity_class):
    entities = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entity = entity_class(**row)
            entities.append(entity)
    
    return entities
