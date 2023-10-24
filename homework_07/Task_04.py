import json
name,surname,age = input(),input(),input()
data = {"name":name,"surname":surname,"age":age}
with open('file_04.json',"w") as f:
    json.dump(data,f)