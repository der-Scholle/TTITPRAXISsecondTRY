class DemoClass:

    def __init__(self, prop1="Значение по умолчанию 1", prop2="Значение по умолчанию 2"):
        self.property1 = prop1
        self.property2 = prop2
        print(f"Создан объект со свойствами: {self.property1}, {self.property2}")

    def __del__(self):
        print(f"Удаление объекта со свойствами: {self.property1}, {self.property2}")

if __name__ == "__main__":
    print("Создание объекта с параметрами по умолчанию:")
    obj1 = DemoClass()

    print("\nСоздание объекта с заданными параметрами:")
    obj2 = DemoClass("Кастомное значение 1", "Кастомное значение 2")

    print("\nУдаление объектов:")
    del obj1
    del obj2