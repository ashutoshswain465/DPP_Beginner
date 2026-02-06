import random

with open("random_person_name/names.txt", "r") as file:
    names = file.readlines()
    random_name = random.choice(names)
    print(f"Randomly selected name: {random_name}")
