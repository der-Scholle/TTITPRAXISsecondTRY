import psutil
import sqlite3
from datetime import datetime

conn = sqlite3.connect('system_monitor.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS monitoring_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    cpu_percent REAL NOT NULL,
    memory_percent REAL NOT NULL,
    disk_percent REAL NOT NULL
)
''')
conn.commit()


def collect_system_data():
    """Сбор данных о системе"""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk


def save_to_db(cpu, memory, disk):
    """Сохранение данных в базу данных"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
    INSERT INTO monitoring_data (timestamp, cpu_percent, memory_percent, disk_percent)
    VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu, memory, disk))
    conn.commit()


def show_current_stats():
    """Отображение текущей статистики"""
    cpu, memory, disk = collect_system_data()
    print("\nТекущие показатели системы:")
    print(f"Загрузка CPU: {cpu}%")
    print(f"Использование памяти: {memory}%")
    print(f"Загрузка диска: {disk}%")
    return cpu, memory, disk


def show_historical_data():
    """Отображение исторических данных"""
    print("\nИсторические данные:")
    print("1. Последние 10 записей")
    print("2. За конкретную дату")
    print("3. Все данные")
    print("0. Назад")

    choice = input("Выберите вариант: ")

    if choice == '1':
        cursor.execute('SELECT * FROM monitoring_data ORDER BY timestamp DESC LIMIT 10')
    elif choice == '2':
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        cursor.execute('SELECT * FROM monitoring_data WHERE timestamp LIKE ? ORDER BY timestamp', (f'{date}%',))
    elif choice == '3':
        cursor.execute('SELECT * FROM monitoring_data ORDER BY timestamp')
    elif choice == '0':
        return

    data = cursor.fetchall()

    if not data:
        print("Данные не найдены!")
        return

    print("\nДата и время           | CPU (%) | Память (%) | Диск (%)")
    print("-----------------------------------------------")
    for row in data:
        print(f"{row[1]} | {row[2]:>6.1f} | {row[3]:>9.1f} | {row[4]:>7.1f}")

while True:
    print("\n=== Системный монитор ===")
    print("1. Текущее состояние системы")
    print("2. Сохранить текущие данные")
    print("3. Просмотреть исторические данные")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        show_current_stats()

    elif choice == '2':
        cpu, memory, disk = show_current_stats()
        save_to_db(cpu, memory, disk)
        print("Данные сохранены!")

    elif choice == '3':
        show_historical_data()

    elif choice == '0':
        break

conn.close()