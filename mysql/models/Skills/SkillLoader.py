import json

from mysql.DatabaseConector import DatabaseConector # type: ignore


class SkillsLoader:
    def __init__(self, db: DatabaseConector):
        self.db = db

    def create_table(self):
        columns = """
            id INT PRIMARY KEY,
            name VARCHAR(255)
        """
        self.db.create_table("skills", columns)

    def load_from_json(self, json_path):
        with open(json_path, "r") as file:
            skills_data = json.load(file)
        return [(skill["id"], skill["name"]) for skill in skills_data]

    def insert_skills(self, skills):
        for skill in skills:
            data = f"{skill[0]}, '{skill[1]}'"
            self.db.insert_data("skills", data)
