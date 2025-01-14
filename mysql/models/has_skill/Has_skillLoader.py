import json

from mysql.DatabaseConector import DatabaseConector # type: ignore

class HasSkillLoader:
    def __init__(self, db: DatabaseConector):
        self.db = db

    def create_table(self):
        columns = """
            person_id INT,
            skill_id INT,
            proficiency VARCHAR(255),
            PRIMARY KEY (person_id, skill_id),
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        """
        self.db.create_table("has_skill", columns)

    def load_from_json(self, json_path):
        with open(json_path, "r") as file:
            has_skill_data = json.load(file)
        return [(entry["person_id"], entry["skill_id"], entry["proficiency"]) for entry in has_skill_data]

    def insert_has_skill(self, has_skill_entries):
        for entry in has_skill_entries:
            data = f"{entry[0]}, {entry[1]}, '{entry[2]}'"
            self.db.insert_data("has_skill", data)
