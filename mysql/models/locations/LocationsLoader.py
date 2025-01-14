import json

from mysql import DatabaseConector


class LocationsLoader:
    def __init__(self, db: DatabaseConector):
        self.db = db

    def create_table(self):
        columns = """
            id INT PRIMARY KEY,
            name VARCHAR(255),
            city VARCHAR(255)
        """
        self.db.create_table("locations", columns)

    def load_from_json(self, json_path):
        with open(json_path, "r") as file:
            locations_data = json.load(file)
        return [(location["id"], location["name"], location["city"]) for location in locations_data]

    def insert_locations(self, locations):
        for location in locations:
            data = f"{location[0]}, '{location[1]}', '{location[2]}'"
            self.db.insert_data("locations", data)
