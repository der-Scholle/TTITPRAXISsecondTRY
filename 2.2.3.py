class NumberContainer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display_numbers(self):
        print(f"Первое число: {self.num1}")
        print(f"Второе число: {self.num2}")

    def set_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def calculate_sum(self):
        return self.num1 + self.num2

    def find_max(self):
        return max(self.num1, self.num2)

numbers = NumberContainer(10, 20)

print("Исходные числа:")
numbers.display_numbers()

numbers.set_numbers(15, 25)
print("\nПосле изменения:")
numbers.display_numbers()

print(f"\nСумма чисел: {numbers.calculate_sum()}")

print(f"Наибольшее число: {numbers.find_max()}")