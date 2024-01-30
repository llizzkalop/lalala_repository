from random import randint
class Building:

    total = 0
    def __init__(self):
        Building.total += 30
values = []
values_sets = randint(0,40)
while len(values) < values_sets:
    new_values = Building()
    values.append(new_values)
print(Building.total)