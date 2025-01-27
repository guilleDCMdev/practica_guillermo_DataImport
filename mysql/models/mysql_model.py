import mysql.connector
import os
from dotenv import load_dotenv
from models.entities import Location, Skill, HasSkill, Pokemon

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener los valores de las variables de entorno
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")

# Función para obtener la conexión
def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT 
    )

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Crear la tabla de locations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INT PRIMARY KEY,
        name NVARCHAR(255),
        city NVARCHAR(255)
    )
    """)
    
    # Crear la tabla de skills
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INT PRIMARY KEY,
        name NVARCHAR(255)
    )
    """)
    
    # Crear la tabla de has_skill
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS has_skill (
        person_id INT,
        skill_id INT,
        proficiency NVARCHAR(255),
        PRIMARY KEY (person_id, skill_id),
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (skill_id) REFERENCES skills(id)
    )
    """)
    
    # Crear la tabla de pokemon
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        pokemon_id INT PRIMARY KEY,
        description TEXT,
        poke_game NVARCHAR(255)
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# Funciones de inserción en la base de datos
def insert_location(location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO locations (id, name, city) VALUES (%s, %s, %s)",
        (location.id, location.name, location.city)
    )
    conn.commit()
    cursor.close()
    conn.close()

def insert_skill(skill):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO skills (id, name) VALUES (%s, %s)",
        (skill.id, skill.name)
    )
    conn.commit()
    cursor.close()
    conn.close()

def insert_has_skill(has_skill):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO has_skill (person_id, skill_id, proficiency) VALUES (%s, %s, %s)",
        (has_skill.person_id, has_skill.skill_id, has_skill.proficiency)
    )
    conn.commit()
    cursor.close()
    conn.close()

def insert_pokemon(pokemon):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pokemon (pokemon_id, description, poke_game) VALUES (%s, %s, %s)",
        (pokemon.pokemon_id, pokemon.description, pokemon.poke_game)
    )
    conn.commit()
    cursor.close()
    conn.close()
