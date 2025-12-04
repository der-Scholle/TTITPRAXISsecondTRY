class Counter:
    def __init__(self, value=0):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def increment(self):
        self.__value += 1

    def decrement(self):
        self.__value -= 1

counter1 = Counter()
print("Счетчик 1 (по умолчанию):", counter1.value)

counter1.increment()
counter1.increment()
print("После двух увеличений:", counter1.value)

counter1.decrement()
print("После одного уменьшения:", counter1.value)

counter2 = Counter(5)
print("\nСчетчик 2 (начальное значение 5):", counter2.value)

counter2.decrement()
counter2.decrement()
counter2.decrement()
print("После трех уменьшений:", counter2.value)

counter2.increment()
print("После одного увеличения:", counter2.value)