from mongo.controllers.mongo_controller import MongoController
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
    empresa_name = input("Ingrese el nombre de la empresa: ")  
    controller = Neo4jController()
    personas_roles = controller.get_personas_y_roles_empresa(empresa_name)
    
    if personas_roles:
        print(f"\nPersonas y sus roles en la empresa '{empresa_name}':")
        for persona_rol in personas_roles:
            print(f"Persona: {persona_rol['Persona']}, Rol: {persona_rol['Rol']}")
    else:
        print(f"No se encontraron personas en la empresa '{empresa_name}'.") 
    controller.close_connection()

def personas_con_rol_diferentes_empresas():
    controller = Neo4jController()
    personas_roles_empresas = controller.personas_con_rol_diferentes_empresas()
    
    if personas_roles_empresas:
        print("\nPersonas con el mismo rol en diferentes empresas:")
        for persona in personas_roles_empresas:
            print(f"Persona: {persona['Persona']}, Rol: {persona['Rol']}, Empresas: {', '.join(persona['Empresas'])}")
    else:
        print("No se encontraron personas con el mismo rol en diferentes empresas.")
    controller.close_connection()

def empresas_comunes_entre_personas():
    persona1 = input("Ingrese el nombre de la primera persona: ")
    persona2 = input("Ingrese el nombre de la segunda persona: ")
    controller = Neo4jController()
    empresas_comunes = controller.empresas_comunes_entre_personas(persona1, persona2)
    
    if empresas_comunes:
        print(f"\nEmpresas comunes entre {persona1} y {persona2}:")
        for empresa in empresas_comunes:
            print(f"- {empresa}")
    else:
        print(f"No se encontraron empresas comunes entre {persona1} y {persona2}.")
    
    controller.close_connection()

def personas_y_funciones_equipo():
    team_id = int(input("Ingrese el ID del equipo: "))
    controller = MongoController()
    personas = controller.get_personas_por_equipo(team_id)
    
    if personas:
        print(f"\nPersonas y sus roles en el equipo {team_id}:")
        for persona in personas:
            print(f"Persona: {persona['name']}, Rol: {persona['rol']}")
    else:
        print("No se encontraron personas en este equipo.")
    
    controller.close_connection()

def equipos_con_numero_personas():
    controller = MongoController()
    equipos = controller.get_equipos_con_num_personas()
    
    for equipo in equipos:
        print(f"Equipo: {equipo['_id']}, Número de personas: {equipo['num_personas']}")
    
    controller.close_connection()

def equipos_con_numero_proyectos():
    controller = MongoController()
    equipos = controller.get_equipos_con_num_proyectos()
    
    for equipo in equipos:
        print(f"Equipo: {equipo['_id']}, Número de proyectos: {equipo['num_proyectos']}")
    
    controller.close_connection()

def skills_nivel_persona():
    proficiency = input("Ingrese el nivel de proficiency: ")
    controller = MySQLController()
    skills = controller.get_skills_por_proficiency(proficiency)
    
    for skill in skills:
        print(f"Persona: {skill['name']}, Skill: {skill['skill_name']}, Proficiency: {skill['proficiency']}")
    
    controller.close_connection()

def personas_con_skills_similares():
    controller = MySQLController()
    personas = controller.get_personas_con_skills_similares()
    
    for persona in personas:
        print(f"{persona['Persona1']} y {persona['Persona2']} comparten la skill: {persona['Skill']}")
    
    controller.close_connection()

def proyecto_con_pokemon_diferentes_tipos():
    controller = MongoController()
    proyecto = controller.get_proyecto_con_pokemon_distintos()
    print(f"Proyecto con más diversidad de Pokémon: {proyecto}")
    
    controller.close_connection()

def equipos_ubicacion_especifica():
    ubicacion = input("Ingrese el nombre de la ubicación: ")
    controller = MongoController()
    equipos = controller.get_equipos_por_ubicacion(ubicacion)
    
    for equipo in equipos:
        print(f"Equipo: {equipo['name']} - Personas: {equipo['personas']} - Proyectos: {equipo['proyectos']}")
    
    controller.close_connection()

if __name__ == "__main__":
    main_menu()
