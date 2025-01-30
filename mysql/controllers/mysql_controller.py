from models.mysql_model import MySQLModel

class MySQLController:
    def __init__(self, config):
        self.model = MySQLModel(config)

    def create_database(self, database):
        query = f"CREATE DATABASE IF NOT EXISTS {database}"
        self.model.execute_query(query, None)

    def insert_data(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.model.execute_query(query, tuple(data.values()))

    def create_table(self, table, columns):
        columns_str = ', '.join([f"{column} {data_type}" for column, data_type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table}({columns_str})"
        self.model.execute_query(query, None)
    
    def skills_nivel_persona(self, person_id, nivel):
        query = "SELECT s.name, hs.proficiency FROM has_skill hs JOIN skills s ON hs.skill_id = s.id WHERE hs.person_id = %s AND hs.proficiency >= %s"
        return self.model.execute_query(query, (person_id, nivel))
    
    def personas_con_skills_similares(self):
        query = "SELECT hs1.person_id AS p1, hs2.person_id AS p2, s.name FROM has_skill hs1 JOIN has_skill hs2 ON hs1.skill_id = hs2.skill_id AND hs1.person_id <> hs2.person_id JOIN skills s ON hs1.skill_id = s.id"
        return self.model.execute_query(query, None)
    
    def equipos_ubicacion_especifica(self, location):
        query = "SELECT t.team_id FROM teams t JOIN projects p ON t.project_id = p.project_id JOIN locations l ON p.location_id = l.id WHERE l.name = %s"
        return self.model.execute_query(query, (location,))
    