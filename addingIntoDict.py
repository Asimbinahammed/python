students=[
    {
        'Name':'Asim',
        'age':25

    },
    {
        'Name':'Aswin',
        'age':28

    },
    {
        'Name':'Amjith',
        'age':30

    }
]
print(students)
print(students(['Name']['Amjith']))
def addingNew(name,age):
    new_students={}
    new_students["name"]=name
    new_students["age"]=age
    students.append(new_students)
    return students
print(addingNew('anju',24))


array_of_dicts = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

name_to_find = 'Bob'

for person in array_of_dicts:
    if person['name'] == name_to_find:
        age_of_bob = person['age']
        break  # Once found, you can stop searching

print(f"The age of {name_to_find} is: {age_of_bob}")
