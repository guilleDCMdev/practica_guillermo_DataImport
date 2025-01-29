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
        
        if choice == "0":
            print("Saliendo del programa...")
            break
        elif choice == "1":
            empresa = input("Ingrese el nombre de la empresa: ")
            buscar_personas_por_empresa(empresa)
        elif choice == "2":
            rol = input("Ingrese el rol a buscar: ")
            buscar_personas_por_rol(rol)
        elif choice == "3":
            persona1 = input("Ingrese el nombre de la primera persona: ")
            persona2 = input("Ingrese el nombre de la segunda persona: ")
            buscar_empresas_comunes(persona1, persona2)
        elif choice == "4":
            equipo = input("Ingrese el nombre del equipo: ")
            buscar_personas_por_equipo(equipo)
        elif choice == "5":
            mostrar_todos_los_equipos()
        elif choice == "6":
            mostrar_equipos_por_proyectos()
        elif choice == "7":
            persona = input("Ingrese el nombre de la persona: ")
            proficiency = input("Ingrese el nivel mínimo de proficiency: ")
            buscar_skills_por_persona(persona, proficiency)
        elif choice == "8":
            buscar_personas_con_skills_similares()
        elif choice == "9":
            buscar_proyecto_pokemon_variedad()
        elif choice == "10":
            ubicacion = input("Ingrese el nombre de la ubicación: ")
            buscar_equipos_por_ubicacion(ubicacion)
        else:
            print("Opción no válida. Intente nuevamente.")


# Datos neo4j
# persons.csv
# ● id: Identicador único para cada persona. Tipo entero.
# ● name: Nombre de la persona. Tipo String.
# ● age: Edad de la persona. Tipo entero.
# empresas.csv:
# ● id: Identicador único para cada empresa. Tipo entero.
# ● name: Nombre de la empresa. Tipo String.
# ● sector: Sector en el que opera la empresa. Tipo cadena.
# works_at.csv:
# ● rol: Rol o cargo de la persona en la empresa. Tipo String.
# ● location_id: Clave foránea referida al identicador único de una
# localización asociada al proyecto. Tipo entero.


# Datos MySQL
# locations.json
# ● id: Identicador único para cada ubicación.Tipo entero.
# ● name: Nombre de la localización. Tipo cadena.
# ● city: Ciudad donde se encuentra la ubicación.Tipo string.
# skills.json:
# ● id: Identicador único para cada habilidad.Tipo entero.
# ● name: Nombre de la habilidad. Tipo string
# has_skill.json
# ● person_id:Clave foránea que hace referencia al identicador único de una
# persona.Tipo Integer.
# ● skill_id: Clave foránea referida al identicador único de una habilidad.Tipo
# entero.
# ● prociency: Nivel de competencia de la persona en la habilidad
# especicada. Tipo string.
# pokemon.json
# ● pokemon_id:identicador único de pokemon.Tipo Integer.
# ● description: descripción del pokemon. Tipo string.
# ● pokeGame: nombre del juego pokemon. . Tipo string.

# Datos de mongo
# projects.csv
# ● project_id: Identicador único para cada proyecto. Tipo entero.
# ● name: Nombre del proyecto. Tipo string.
# ● description: Descripción del proyecto. Tipo cadena.
# ● location_id: Clave foránea referida al identicador único de una
# localización asociada al proyecto. Tipo entero.
# ● company_id: Clave foránea referida al identicador único de una empresa
# asociada al proyecto.Tipo entero.
# teams.csv
# ● team_id:Identicador único para cada equipo. Tipo entero.
# ● name: Nombre del equipo.Tipo String.
# ● description: Descripción del equipo: Descripción del equipo. Tipo cadena.
# ● project_id: Clave foránea que hace referencia al identicador único de un
# proyecto. Tipo entero.
# works_in_team.csv
# ● person_id: Clave foránea que hace referencia al identicador único de una
# persona. Tipo entero.
# ● team_id: Clave foránea que hace referencia al identicador único de un
# equipo. Tipo entero.
# ● rol: Rol de la persona dentro del equipo. Tipo String.
# favourite_pokemon.json
# ● person_id: Clave foránea que hace referencia al identicador único de una
# persona. Tipo entero.
# ● pokemon_id Clave foránea que hace referencia al identicador único de un
# pokemon. Tipo entero.
# ● dateCaptured: fecha en la que el pokemon se capturó. Tipo String.



def buscar_personas_por_empresa(empresa):

    print(f"Buscando personas en la empresa {empresa}...")

def buscar_personas_por_rol(rol):
    print(f"Buscando personas con el rol {rol} en diferentes empresas...")

def buscar_empresas_comunes(persona1, persona2):
    print(f"Buscando empresas comunes entre {persona1} y {persona2}...")

def buscar_personas_por_equipo(equipo):
    print(f"Buscando personas en el equipo {equipo}...")

def mostrar_todos_los_equipos():
    print("Mostrando todos los equipos con el número de personas que los componen...")

def mostrar_equipos_por_proyectos():
    print("Mostrando equipos con el número total de proyectos asociados...")

def buscar_skills_por_persona(persona, proficiency):
    print(f"Buscando skills de {persona} con proficiency {proficiency}...")

def buscar_personas_con_skills_similares():
    print("Buscando personas con skills similares...")

def buscar_proyecto_pokemon_variedad():
    print("Buscando proyecto con mayor variedad de pokemons favoritos en el equipo...")

def buscar_equipos_por_ubicacion(ubicacion):
    print(f"Buscando equipos en la ubicación {ubicacion}...")

if __name__ == "__main__":
    main_menu()
