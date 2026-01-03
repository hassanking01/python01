class Plant:
    def __init__(self, name: str , height: int , age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_data = [["Rose" , 25 , 30],
                   ["Oak" ,200 , 365],
                   ["Cactus", 5, 90],
                   ["Sunflower" , 80 , 45],
                   ["Fern" , 15 , 120]
                   ]
    i = 0;
    for name, height, age in plants_data:
        p1 = Plant(name , height , age)
        print("Created:" , p1.get_info())
        i += 1;
    print("\nTotal plants created:", i)