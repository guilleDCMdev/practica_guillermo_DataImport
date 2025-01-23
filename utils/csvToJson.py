#conversor de csv a json
import csv
import json
import os

def csvToJson(csv_file:str, json_file:str):
    data = {}
    with open(csv_file, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            key = rows['id']
            data[key] = rows
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))
        
# def main():
#     csvToJson('data/locations.csv', 'data/locations.json')
#     csvToJson('data/skills.csv', 'data/skills.json')
#     csvToJson('data/has_skill.csv', 'data/has_skill.json')
#     csvToJson('data/pokemon.csv', 'data/pokemon.json')