import json

# Open the existing JSON file and load its contents
with open('DummyData.json', 'r', encoding='utf-8') as file:
    datas = json.load(file)

    for data in datas:
        del data['name']['en']
        del data['name']['hi']

with open('NewJson.json', 'w', encoding='utf-8') as file:
    json.dump(datas, file, indent=4)
