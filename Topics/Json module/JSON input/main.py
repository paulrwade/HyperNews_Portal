import json


json_string = input()

data = json.loads(json_string)

print(type(data))
print(data)