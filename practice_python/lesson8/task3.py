import json

data = {'name': 'Nikita',
        'surname': 'Dubino',
        'is_teacher': False}

with open('file_03.json', 'w') as file:
    json.dump(data, file)
