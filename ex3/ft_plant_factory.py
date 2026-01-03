class Plant:
    def __init__(self, name: str , height: int , age: int):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = []
    plants_data = [["Rose" , 25 , 30],
                   ["Oak" ,200 , 365],
                   ["Cactus", 5, 90],
                   ["Sunflower" , 80 , 45],
                   ["Fern" , 15 , 120]
                   ]
    i = 0;
    for data in plants_data:
        p1 = Plant(data[0] , data[1] , data[2])
        plants.append(p1)
        i += 1;
    for plant in plants:
        print("Created:" , f"{plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created:", i)