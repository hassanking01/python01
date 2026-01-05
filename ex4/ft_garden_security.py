class SecurePlant:
    def __init__(self , name : str):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name}")

    def set_height(self , height : int):
        if height < 0 :
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else :
            print(f"Height updated: {height}cm [OK]")
            self.__height = height

    def set_age(self, age: int):
        if age < 0 :
            print(f"Invalid operation attempted: height {age}cm [REJECTED]")
            print("Security: Negative age rejected")
        else :
            print(f"Height updated: {age}cm [OK]")
            self.__age = age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age
   
if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Plant")
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-5)
    print()
    print(f"Current plant: {p1.name} ({p1.get_height()}cm, {p1.get_age()} days)")
