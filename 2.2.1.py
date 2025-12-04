class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def set_surname(self, new_surname):
        self.surname = new_surname

    def set_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def set_group_number(self, new_group_number):
        self.group_number = new_group_number

    def display_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")

def find_student(students, surname, birth_date):
    for student in students:
        if student.surname == surname and student.birth_date == birth_date:
            return student
    return None

students = [
    Student("Кипелов", "01.01.2000", "ГР-101", [4, 5, 3, 4, 5]),
    Student("Линдеманн", "15.05.2001", "ГР-102", [3, 4, 4, 3, 5]),
    Student("Осборн", "20.11.1999", "ГР-101", [5, 5, 5, 5, 5])
]

students[0].set_surname("Кипелов-Осборн")
students[1].set_group_number("ГР-103")

search_surname = input("Введите фамилию студента: ")
search_birth_date = input("Введите дату рождения студента (в формате ДД.ММ.ГГГГ): ")

found_student = find_student(students, search_surname, search_birth_date)
if found_student:
    print("\nНайден студент:")
    found_student.display_info()
else:
    print("\nСтудент не найден.")