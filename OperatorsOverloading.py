class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

h1 = Building(25, 'Shopping mall')
h2 = Building(25, 'Shopping mall')
h3 = Building(35, 'High-rise')
print(f'h1 == h2: {h1 == h2}')
print(f'h1 == h3: {h1 == h3}')