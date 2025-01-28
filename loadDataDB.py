from mongo.starterMongoMain import MongoLoader
from mySql.starterMysqlMain import MySQLLoader
from neo4J.StarterNeo4jMain import Neo4jLoader

class LoadDataDB:
    def __init__(self):
        self.mysql_loader = MySQLLoader()
        self.mongo_loader = MongoLoader()
        self.neo4j_loader = Neo4jLoader()

    def load_all(self):
        print("Cargando datos en MySQL...")
        self.mysql_loader.load_data()

        print("Cargando datos en MongoDB...")
        self.mongo_loader.load_data()
        self.mongo_loader.close()

        print("Cargando datos en Neo4j...")
        self.neo4j_loader.load_data()
        self.neo4j_loader.close()

if __name__ == "__main__":
    loader = LoadDataDB()
    loader.load_all()
