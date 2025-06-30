# Sorts a list of dictionaries by the 'age' key
def sort_by_age(data):
    return sorted(data, key=lambda x: x['age'])

# Sample usage
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]

sorted_people = sort_by_age(people)
print(sorted_people)
