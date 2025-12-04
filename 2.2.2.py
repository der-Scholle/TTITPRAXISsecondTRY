class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.number = number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.number}")
        print(f"Время отправления: {self.departure_time}")

def find_train(trains, number):
    for train in trains:
        if train.number == number:
            return train
    return None

trains = [
    Train("Москва", "123A", "08:30"),
    Train("Санкт-Петербург", "456B", "12:45"),
    Train("Казань", "789C", "15:20")
]

search_number = input("Введите номер поезда: ")

found_train = find_train(trains, search_number)
if found_train:
    print("\nИнформация о поезде:")
    found_train.display_info()
else:
    print("\nПоезд с таким номером не найден.")