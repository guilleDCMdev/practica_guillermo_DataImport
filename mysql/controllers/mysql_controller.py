from models.mysql_model import MySQLModel

class MySQLController:
    def __init__(self, config):
        self.model = MySQLModel(config)

    def insert_data(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.model.execute_query(query, tuple(data.values()))

    def create_table(self, table, columns):
        columns_str = ', '.join([f"{column} {data_type}" for column, data_type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table}({columns_str})"
        self.model.execute_query(query, None)