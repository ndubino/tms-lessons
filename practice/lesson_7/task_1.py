students_list = [
    ('Ivan', 'Ivanov', 2003),
    ('Petr', 'Petrov', 2005),
    ('Sidr', 'Sidorov', 2004)
]

sorted_list = sorted(students_list, key=lambda student: students_list[1])
