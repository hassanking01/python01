class Plant:
    def __init__(self, name: str , height: int , age: int):
        self.name = name
        self.height = height
        self.age = age
    def age_grow(self):
        self.age += 1
    def grow(self):
        self.height += 1
    def print_plan(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")    
if __name__ == "__main__":
    i = 1
    print(f"=== Day {i} ===")
    p1 = Plant("Rose" , 25 , 30)
    p1.print_plan()
    old_height = p1.height
    while i < 7:
        p1.age_grow()
        p1.grow()
        i += 1
    print(f"=== Day {i} ===")
    p1.print_plan()
    print(f"Growth this week: +{p1.height - old_height}cm")
        