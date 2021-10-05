import json
import os
db_path = os.path.join("database", "users_db.json")
# d = json.loads(db_path)

with open(db_path, 'r') as j:
    contents = json.loads(j.read())
    # print(contents)
username = "abdo.am169@gmail.com"
if "abdo.am169@gmail.com" in contents.keys() :
    print(contents["abdo.am169@gmail.com"]["password"])


    print("True")
print(contents.keys())