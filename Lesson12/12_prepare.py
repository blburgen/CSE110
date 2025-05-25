people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 110
youngest_person = ""


for person in people:
    name = person.split()
    if int(name[1]) < youngest_age:
        youngest_age = int(name[1])
        youngest_person = name[0]
        
print(f"The youngest person is {youngest_person} at age {youngest_age}.")
    