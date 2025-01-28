from utils.config import MONGO_URI, MONGO_DB
from pymongo import MongoClient

class MongoModel:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.projects_collection = self.db.projects
        self.teams_collection = self.db.teams
        self.works_in_team_collection = self.db.works_in_team
        self.favourite_pokemon_collection = self.db.favourite_pokemon

    def close(self):
        self.client.close()

    def insert_many(self, collection_name, data):
        collection = getattr(self.db, collection_name)
        collection.insert_many(data)

    def insert_one(self, collection_name, data):
        collection = getattr(self.db, collection_name)
        collection.insert_one(data)
