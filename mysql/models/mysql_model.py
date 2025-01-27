# models/mysql_model.py
import mysql.connector
from utils.config import get_db_connection

class MySQLModel:
    def __init__(self):
        self.connection = get_db_connection()

    def close(self):
        self.connection.close()

    def create_node(self, table, **properties):
        """
        Crea un registro en una tabla específica.
        """
        columns = ', '.join(properties.keys())
        placeholders = ', '.join(['%s'] * len(properties))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.connection.cursor()
        cursor.execute(query, tuple(properties.values()))
        self.connection.commit()
        cursor.close()

    def create_relationship(self, table, **properties):
        """
        Crea una relación entre dos registros de tablas diferentes.
        """
        columns = ', '.join(properties.keys())
        placeholders = ', '.join(['%s'] * len(properties))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.connection.cursor()
        cursor.execute(query, tuple(properties.values()))
        self.connection.commit()
        cursor.close()
