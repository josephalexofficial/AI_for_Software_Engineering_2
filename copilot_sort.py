# Copilot suggested function based on comment prompt
def sort_people_by_age(people):
    people.sort(key=lambda person: person['age'])
    return people

# Example data
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]

print(sort_people_by_age(people))
