class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        return self.rate * self.days

if __name__ == "__main__":

    worker = Worker("Чёрный", "Мальчик", 1500, 20)

    print(f"Работник: {worker.name} {worker.surname}")
    print(f"Ставка за день: {worker.rate} руб.")
    print(f"Отработано дней: {worker.days}")
    print(f"Зарплата: {worker.get_salary()} руб.")