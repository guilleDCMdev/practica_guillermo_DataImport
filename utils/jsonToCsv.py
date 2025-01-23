#conversor de json a csv
import csv
import json
import os

def jsonToCsv(json_file:str, csv_file:str):
    with open(json_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    with open(csv_file, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data[next(iter(data))].keys())
        for key in data:
            csv_writer.writerow(data[key].values())
            
# def main():
#     jsonToCsv('data/locations.json', 'data/locations.csv')
#     jsonToCsv('data/skills.json', 'data/skills.csv')
#     jsonToCsv('data/has_skill.json', 'data/has_skill.csv')
#     jsonToCsv('data/pokemon.json', 'data/pokemon.csv')