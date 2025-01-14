from mysql.models.locations.LocationsLoader import LocationsLoader # type: ignore
from mysql.models.Skills.SkillLoader import SkillsLoader # type: ignore # type: ignore
from mysql.models.has_skill.Has_skillLoader import HasSkillLoader # type: ignore
from mysql.models.pokemons.PokemonLoader import PokemonLoader # type: ignore
from mysql.DatabaseConector import DatabaseConector # type: ignore

db = DatabaseConector()

locations_loader = LocationsLoader(db)
skills_loader = SkillsLoader(db)
has_skill_loader = HasSkillLoader(db)
pokemon_loader = PokemonLoader(db)

locations_loader.create_table()
skills_loader.create_table()
has_skill_loader.create_table()
pokemon_loader.create_table()

locations_loader.load_and_insert_locations("data/locations.json")
skills_loader.load_and_insert_skills("data/skills.json")
has_skill_loader.load_and_insert_has_skill("data/has_skill.json")
pokemon_loader.load_and_insert_pokemon("data/pokemon.json")
