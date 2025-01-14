#carga de datos de python a mysql

# locations.json
# ● id: Identificador único para cada ubicación.Tipo entero.
# ● name: Nombre de la localización. Tipo cadena.
# ● city: Ciudad donde se encuentra la ubicación.Tipo string.

# skills.json:
# ● id: Identificador único para cada habilidad.Tipo entero.
# ● name: Nombre de la habilidad. Tipo string.

# has_skill.json
# ● person_id:Clave foránea que hace referencia al identificador único de una
# persona.Tipo Integer.
# ● skill_id: Clave foránea referida al identificador único de una habilidad.Tipo
# entero.
# ● proficiency: Nivel de competencia de la persona en la habilidad
# especificada. Tipo string

# pokemon.json
# ● pokemon_id:identificador único de pokemon.Tipo Integer.
# ● description: descripción del pokemon. Tipo string.
# ● pokeGame: nombre del juego pokemon. . Tipo string
import mysql.connector
class DatabaseConector:
    def __init__(self, host, user, password, database,port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
    
    def create_table(self,table_name,columns):
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns}
        )
        """    
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def insert_data(self, table_name, data):
        insert_query = f"INSERT INTO {table_name} VALUES ({data})"
        self.cursor.execute(insert_query)
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_all_data(self,table_name):
        select_all_query = f"SELECT * FROM {table_name}"
        self.cursor.execute(select_all_query)
        result = self.cursor.fetchall()
        return result
    
    def update_data(self, table_name, data):
        update_query = f"UPDATE {table_name} SET name=%s WHERE id=%s"
        self.cursor.execute(update_query, data)
        self.connection.commit()
    
    def delete_data(self, table_name, id):
        delete_query = f"DELETE FROM {table_name} WHERE id=%s"
        data = (id,)
        self.cursor.execute(delete_query, data)
        self.connection.commit()
    