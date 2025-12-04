import sqlite3

# Подключение к базе
conn = sqlite3.connect("drinks.db")
cur = conn.cursor()

# --------- Создание таблиц ---------

cur.execute("""
CREATE TABLE IF NOT EXISTS alcohol (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    strength INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS cocktails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    strength REAL,
    price INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS cocktail_items (
    cocktail_id INTEGER,
    ingredient TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS stock (
    name TEXT PRIMARY KEY,
    amount INTEGER
)
""")

conn.commit()


# --------- 1. Добавление алкоголя ---------
def add_alcohol():
    print("\n=== Добавление алкоголя ===")
    name = input("Название: ")
    strength = int(input("Крепость: "))
    amount = int(input("Количество: "))

    cur.execute("INSERT INTO alcohol (name, strength) VALUES (?, ?)", (name, strength))
    cur.execute("INSERT OR REPLACE INTO stock (name, amount) VALUES (?, ?)", (name, amount))

    conn.commit()
    print("Алкоголь добавлен!\n")


# --------- 2. Добавление коктейля ---------
def add_cocktail():
    print("\n=== Создание коктейля ===")
    name = input("Название коктейля: ")

    n = int(input("Количество ингредиентов: "))
    items = []

    for i in range(n):
        ing = input(f"Ингредиент {i+1}: ")
        items.append(ing)

    price = int(input("Цена: "))

    # вычисление крепости
    cur.execute("SELECT name, strength FROM alcohol")
    alcohol_dict = {row[0]: row[1] for row in cur.fetchall()}

    alcohol_strengths = [alcohol_dict[i] for i in items if i in alcohol_dict]
    strength = sum(alcohol_strengths) / len(alcohol_strengths) if alcohol_strengths else 0

    cur.execute("INSERT INTO cocktails (name, strength, price) VALUES (?, ?, ?)",
                (name, strength, price))
    cocktail_id = cur.lastrowid

    for ing in items:
        cur.execute("INSERT INTO cocktail_items (cocktail_id, ingredient) VALUES (?, ?)",
                    (cocktail_id, ing))

    conn.commit()
    print("Коктейль создан!\n")


# --------- 3. Продажа ---------
def sell():
    print("\n=== Продажа ===")
    name = input("Название: ")

    # Алкоголь
    cur.execute("SELECT amount FROM stock WHERE name = ?", (name,))
    row = cur.fetchone()

    if row is not None:
        if row[0] > 0:
            cur.execute("UPDATE stock SET amount = amount - 1 WHERE name = ?", (name,))
            conn.commit()
            print("Алкоголь продан!\n")
        else:
            print("Нет на складе.\n")
        return

    # Коктейль
    cur.execute("SELECT id FROM cocktails WHERE name = ?", (name,))
    cocktail = cur.fetchone()

    if not cocktail:
        print("Напиток не найден.\n")
        return

    cocktail_id = cocktail[0]

    cur.execute("SELECT ingredient FROM cocktail_items WHERE cocktail_id = ?", (cocktail_id,))
    ingredients = [i[0] for i in cur.fetchall()]

    # Проверка склада
    for ing in ingredients:
        cur.execute("SELECT amount FROM stock WHERE name = ?", (ing,))
        r = cur.fetchone()
        if not r or r[0] <= 0:
            print("Недостаточно ингредиентов.\n")
            return

    # Списываем ингредиенты
    for ing in ingredients:
        cur.execute("UPDATE stock SET amount = amount - 1 WHERE name = ?", (ing,))
    conn.commit()

    print("Коктейль продан!\n")


# --------- 4. Пополнение запаса ---------
def restock():
    print("\n=== Пополнение склада ===")
    name = input("Название: ")
    amount = int(input("Количество: "))

    cur.execute("INSERT OR IGNORE INTO stock (name, amount) VALUES (?, 0)", (name,))
    cur.execute("UPDATE stock SET amount = amount + ? WHERE name = ?", (amount, name))

    conn.commit()
    print("Запасы обновлены.\n")


# --------- Студенческое меню ---------
while True:
    print("""
1 - Добавить алкоголь
2 - Добавить коктейль
3 - Продать напиток/коктейль
4 - Пополнить склад
5 - Выход
""")

    choice = input("Выберите действие: ")
    if choice == "1":
        add_alcohol()
    elif choice == "2":
        add_cocktail()
    elif choice == "3":
        sell()
    elif choice == "4":
        restock()
    elif choice == "5":
        break
    else:
        print("Ошибка ввода.")