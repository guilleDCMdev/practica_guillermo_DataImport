from models.neo4j_model import Neo4jModel
from utils.data_loader import load_data
from models.entities import Person, Empresa
import csv

class Neo4jController:
    def __init__(self):
        self.model = Neo4jModel()

    def load_persons(self, file_path):
        persons = load_data(file_path, Person)
        for person in persons:
            self.model.create_person(person)

    def load_companies(self, file_path):
        companies = load_data(file_path, Empresa)
        for company in companies:
            self.model.create_company(company)

    def load_works_at_relations(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                person_id = int(row['person_id'])
                role = row['rol']
                location_id = int(row['location_id'])
                self.model.create_works_at_relationship(person_id, location_id, role, location_id)

    def close_connection(self):
        self.model.close()
