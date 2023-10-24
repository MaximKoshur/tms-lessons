import json
data = {'name': 'Maxim','surname': 'Koshur','age': '19'}
with open('file_03.json',"w") as f:
    json.dump(data,f)