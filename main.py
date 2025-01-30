from monGo.controllers.mongo_controller import MongoController
from mySql.controllers.mysql_controller import MySQLController
from neo4J.controllers.neo4j_controller import Neo4jController


def main_menu():
    while True:
        print("\nMenú:")
        print("1. Personas y sus roles en una empresa concreta")
        print("2. Personas con el mismo rol en diferentes empresas")
        print("3. Empresas comunes entre dos personas")
        print("4. Personas y sus funciones en un equipo específico")
        print("5. Mostrar todos los equipos con el número de personas que los componen")
        print("6. Mostrar los equipos con el número total de proyectos a los que están asociados")
        print("7. Obtener todas las skills en las que una persona tiene al menos un nivel específico de proficiency")
        print("8. Encontrar personas con skills similares")
        print("9. Proyecto con más personas con pokemons favoritos de diferente tipo")
        print("10. Lista de equipos ubicados en una localización específica")
        print("0. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            personas_y_roles_empresa()
        elif choice == "2":
            personas_con_rol_diferentes_empresas()
        elif choice == "3":
            empresas_comunes_entre_personas()
        elif choice == "4":
            personas_y_funciones_equipo()
        elif choice == "5":
            equipos_con_numero_personas()
        elif choice == "6":
            equipos_con_numero_proyectos()
        elif choice == "7":
            skills_nivel_persona()
        elif choice == "8":
            personas_con_skills_similares()
        elif choice == "9":
            proyecto_con_pokemon_diferentes_tipos()
        elif choice == "10":
            equipos_ubicacion_especifica()
        elif choice == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def personas_y_roles_empresa():
    ne04j = Neo4jController()
    empresa = input("Introduzca el nombre de la empresa: ")
    personas = ne04j.personas_y_roles_empresa(empresa)
    print(f"Personas y sus roles en la empresa {empresa}:")
    for persona in personas:
        print(f"{persona['p.name']} - {persona['r.rol']}")
    ne04j.close_connection()
    
def personas_con_rol_diferentes_empresas():
    neo4j = Neo4jController()
    personas = neo4j.personas_con_rol_diferentes_empresas()
    print("Personas con el mismo rol en diferentes empresas:")
    for persona in personas:
        print(f"{persona['p1.name']} - {persona['e1.name']} - {persona['r1.rol']} - {persona['p2.name']} - {persona['e2.name']}")
    neo4j.close_connection()

def empresas_comunes_entre_personas():
    neo4j = Neo4jController()
    persona1 = input("Introduzca el nombre de la primera persona: ")
    persona2 = input("Introduzca el nombre de la segunda persona: ")
    empresas = neo4j.empresas_comunes_entre_personas(persona1, persona2)
    print(f"Empresas comunes entre {persona1} y {persona2}:")
    for empresa in empresas:
        print(empresa['e.name'])
    neo4j.close_connection()

def personas_y_funciones_equipo():
    mongoController = MongoController()
    team_id = input("Introduzca el ID del equipo: ")
    personas = mongoController.get_personas_por_equipo(team_id)
    
    neo4j = Neo4jController()
    personas = neo4j.personas_y_funciones_equipo(personas)
    print(f"Personas y sus funciones en el equipo {team_id}:")
    for persona in personas:
        print(persona['p.name'])
    neo4j.close_connection()

def equipos_con_numero_personas():
    mongoController = MongoController()
    equipos = mongoController.equipos_con_numero_personas()
    print("Equipos con el número de personas que los componen:")
    for equipo in equipos:
        print(f"Equipo {equipo['_id']}: {equipo['num_personas']} personas")
    mongoController.close_connection()

def equipos_con_numero_proyectos():
    mongoController = MongoController()
    equipos = mongoController.equipos_con_numero_proyectos()
    print("Equipos con el número total de proyectos a los que están asociados:")
    for equipo in equipos:
        print(f"Proyecto {equipo['_id']}: {equipo['num_equipos']} equipos")
    mongoController.close_connection()

def skills_nivel_persona():
    mysql = MySQLController()
    person_id = input("Introduzca el ID de la persona: ")
    nivel = input("Introduzca el nivel de proficiency: ")
    skills = mysql.skills_nivel_persona(person_id, nivel)
    print(f"Skills en las que la persona {person_id} tiene al menos un nivel de proficiency de {nivel}:")
    for skill in skills:
        print(f"{skill['s.name']} - {skill['hs.proficiency']}")
    mysql.close_connection()

def personas_con_skills_similares():
    mysql = MySQLController()
    personasSkills = mysql.personas_con_skills_similares()
    neo4j = Neo4jController()
    personas = neo4j.personas_y_funciones_equipo(personasSkills)
    print("Personas con skills similares:")
    for persona in personas:
        print(f"{persona['p1']} - {persona['p2']} - {persona['s.name']}")
    mysql.close_connection()


def proyecto_con_pokemon_diferentes_tipos():
    mongo = MongoController()
    proyecto = mongo.obtener_proyecto_mas_diverso()
    print(f"Proyecto con más personas con pokemons favoritos de diferente tipo: {proyecto}")
    mongo.close_connection()

def equipos_ubicacion_especifica():
    mysql = MySQLController()
    location = input("Introduzca la localización: ")
    equipos = mysql.equipos_ubicacion_especifica(location)
    mongo = MongoController()
    personas = mongo.personas_y_funciones_equipo(equipos)
    print(f"Equipos ubicados en {location}:")
    for persona in personas:
        print(persona['t.team_id'])
    mysql.close_connection()

if __name__ == "__main__":
    main_menu()