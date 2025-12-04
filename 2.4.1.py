import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    middle_name TEXT,
    group_name TEXT,
    grade1 INTEGER,
    grade2 INTEGER,
    grade3 INTEGER,
    grade4 INTEGER
)
''')
conn.commit()

while True:
    print("\n1. Добавить студента")
    print("2. Показать всех студентов")
    print("3. Найти студента")
    print("4. Изменить данные студента")
    print("5. Удалить студента")
    print("6. Средний балл группы")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        first = input("Имя: ")
        last = input("Фамилия: ")
        middle = input("Отчество: ")
        group = input("Группа: ")
        grades = [
            int(input("Оценка 1: ")),
            int(input("Оценка 2: ")),
            int(input("Оценка 3: ")),
            int(input("Оценка 4: "))
        ]

        cursor.execute('''
        INSERT INTO students 
        (first_name, last_name, middle_name, group_name, grade1, grade2, grade3, grade4)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first, last, middle, group, *grades))
        conn.commit()
        print("Студент добавлен!")

    elif choice == '2':
        cursor.execute('SELECT id, first_name, last_name, group_name FROM students')
        print("\nСписок всех студентов:")
        for row in cursor.fetchall():
            print(f"{row[0]}. {row[2]} {row[1]} ({row[3]})")

    elif choice == '3':
        last = input("\nВведите фамилию: ")
        cursor.execute('''
        SELECT *, (grade1 + grade2 + grade3 + grade4) / 4.0 
        FROM students 
        WHERE last_name LIKE ?
        ''', (f'%{last}%',))

        found = cursor.fetchall()
        if not found:
            print("Студент не найден!")
            continue

        for student in found:
            print(f"\n{student[2]} {student[1]} {student[3]}")
            print(f"Группа: {student[4]}")
            print(f"Оценки: {student[5:9]}")
            print(f"Средний балл: {student[9]:.2f}")

    elif choice == '4':
        cursor.execute('SELECT id, first_name, last_name FROM students')
        print("\nСписок студентов:")
        for row in cursor.fetchall():
            print(f"{row[0]}. {row[2]} {row[1]}")

        try:
            student_id = int(input("\nВведите ID студента: "))
            cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
            student = cursor.fetchone()

            if not student:
                print("Студент не найден!")
                continue

            first = input(f"Имя ({student[1]}): ") or student[1]
            last = input(f"Фамилия ({student[2]}): ") or student[2]
            middle = input(f"Отчество ({student[3]}): ") or student[3]
            group = input(f"Группа ({student[4]}): ") or student[4]
            grades = [
                int(input(f"Оценка 1 ({student[5]}): ") or student[5]),
                int(input(f"Оценка 2 ({student[6]}): ") or student[6]),
                int(input(f"Оценка 3 ({student[7]}): ") or student[7]),
                int(input(f"Оценка 4 ({student[8]}): ") or student[8])
            ]

            cursor.execute('''
            UPDATE students SET
            first_name = ?,
            last_name = ?,
            middle_name = ?,
            group_name = ?,
            grade1 = ?,
            grade2 = ?,
            grade3 = ?,
            grade4 = ?
            WHERE id = ?
            ''', (first, last, middle, group, *grades, student_id))
            conn.commit()
            print("Данные обновлены!")
        except:
            print("Ошибка ввода!")

    elif choice == '5':
        cursor.execute('SELECT id, first_name, last_name FROM students')
        print("\nСписок студентов:")
        for row in cursor.fetchall():
            print(f"{row[0]}. {row[2]} {row[1]}")

        try:
            student_id = int(input("\nВведите ID студента: "))
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()
            print("Студент удален!")
        except:
            print("Ошибка ввода!")

    elif choice == '6':
        group = input("\nВведите название группы: ")
        cursor.execute('''
        SELECT AVG((grade1 + grade2 + grade3 + grade4) / 4.0)
        FROM students 
        WHERE group_name = ?
        ''', (group,))

        avg = cursor.fetchone()[0]
        if avg:
            print(f"Средний балл группы {group}: {avg:.2f}")
        else:
            print("Группа не найдена или нет студентов!")

    elif choice == '0':
        break

    else:
        print("Неверный ввод!")

conn.close()