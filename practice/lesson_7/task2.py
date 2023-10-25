students_list = [
    ('Ivan', 'Ivanov', 2003),
    ('Petr', 'Petrov', 2005),
    ('Sidr', 'Sidorov', 2004)
]

def get_surname(student: tuple) -> str:
    return student[2]


sorted_list = sorted(students_list, key=get_surname)

print(sorted_list)

