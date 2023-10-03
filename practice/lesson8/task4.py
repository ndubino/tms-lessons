import json

name = int()
surname = int()
age = int(input())


person = {'name': name, 'surname': surname, 'age': age}

with open('file_04.json', 'w') as file:
    json.dump(person, file)