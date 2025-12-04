class Calculation:
    def __init__(self, calculation_line=""):
        self.__calculation_line = calculation_line

    def set_calculation_line(self, new_value):
        """Устанавливает новое значение для calculation_line"""
        self.__calculation_line = new_value

    def set_last_symbol_calculation_line(self, symbol):
        """Добавляет символ в конец строки"""
        self.__calculation_line += str(symbol)

    def get_calculation_line(self):
        """Возвращает текущее значение строки"""
        return self.__calculation_line

    def get_last_symbol(self):
        """Возвращает последний символ строки"""
        if self.__calculation_line:
            return self.__calculation_line[-1]
        return None

    def delete_last_symbol(self):
        """Удаляет последний символ из строки"""
        if self.__calculation_line:
            self.__calculation_line = self.__calculation_line[:-1]

if __name__ == "__main__":
    calc = Calculation("123")

    print("Текущая строка:", calc.get_calculation_line())

    calc.set_last_symbol_calculation_line("+")
    print("После добавления '+':", calc.get_calculation_line())

    print("Последний символ:", calc.get_last_symbol())

    calc.delete_last_symbol()
    print("После удаления последнего символа:", calc.get_calculation_line())

    calc.set_calculation_line("456")
    print("Новая строка:", calc.get_calculation_line())