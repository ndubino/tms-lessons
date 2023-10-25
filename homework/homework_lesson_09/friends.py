from person import Person


my_friends = [
    Person('Ivan Ivanov', 20, 'M'),
    Person('Anna Ivanova', 25, 'F'),
    Person('Sergey Petrov', 30, 'M'),
    Person('Elena Sidorova', 28, 'F')
]

def get_oldest_person(lst):
    oldest = None
    for person in lst:
        if oldest is None or person.age > oldest.age:
            oldest = person
    return oldest


def get_male_person(lst):
    return [person for person in lst if person.gender == 'M']


print('My friends are: ')
for friend in my_friends:
    friend.print_person_info()

print()
print('The oldest friend is: ')
oldest_friend = get_oldest_person(my_friends)
oldest_friend.print_person_info()

print()
print('My male friends are: ')
male_friends = get_male_person(my_friends)
for friend in male_friends:
    friend.print_person_info()