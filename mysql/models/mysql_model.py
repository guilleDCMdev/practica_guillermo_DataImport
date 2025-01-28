import mysql.connector

class MySQLModel:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            user=self.config['MYSQL_USER'],
            password=self.config['MYSQL_PASSWORD'],
            database=self.config['MYSQL_DB']
        )

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params):
        cursor = None
        try:
            if not self.connection:
                self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
