# utils/config.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    host_port = os.getenv('DB_HOST')
    host, port = host_port.split(':') if ':' in host_port else (host_port, 3306)
    
    return mysql.connector.connect(
        host=host,
        port=int(port),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
