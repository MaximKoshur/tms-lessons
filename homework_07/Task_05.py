import json
with open("file_04.json","r") as f:
    data = json.load(f)
    print(data['surname'],data['name'],data['age'])