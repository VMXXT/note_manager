from datetime import datetime # импортируем библиотеку для работы с датами

# Создаем словарь для хранения информации о заметке
note = {}

# Запрашиваем у пользователя информацию
note["username"] = input("Введите имя пользователя: ")

# Создаем список заголовков заметки
note["titles"] = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)

note["content"] = input("Введите описание заметки: \n")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

# Форматируем дату создания заметки и дату дэдлайна
temp_created_date = datetime.today() # присваиваем переменной сегодняшнюю дату
note["created_date"] = datetime.strftime(temp_created_date, "%d.%m") # форматируем, убираем год

#создадим цикл для проверки верного ввода даты дэдлайна
while True:
    temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")

    try:
        note["issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m") # убираем год
        break  # Выход из цикла, если дата введена правильно

    except ValueError:
    # Если возникает ошибка, значит дата введена неправильно
        print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")

#Вывод данных
# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
