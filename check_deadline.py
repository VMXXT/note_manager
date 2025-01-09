from datetime import datetime # импортируем библиотеку для работы с датами

# Создаем словарь для хранения информации о заметке и записываем имя пользователя
note = {"username": input("Введите имя пользователя: "), "titles": []}

# Запрашиваем у пользователя информацию
# создаем цикл для множественного ввода заголовков
while True:
    # Запрашиваем у пользователя ввод заголовка заметки
    title = input("Введите заголовок заметки (или 'стоп' или Enter для завершения кода): ")

    # Проверяем команду завершения ввода
    if title.lower() == "стоп" or title == "":
        break

    # Добавляем только новые значения в список заголовков
    if title not in note["titles"]: # если такого заголовка нет, добавляем
        note["titles"].append(title)
    elif title in note["titles"]: # если заголовок есть, просим ввести другой
        print("Этот заголовок уже был добавлен. Введите другой.")


note["content"] = input("Введите описание заметки: \n")
# Создаем список со статусами заметки и записываем в словарь 1 по индексу
statuses = ["Выполнено" , "В процессе" , "Отложено"]
note["status"] = statuses[1]

# Форматируем дату создания заметки и дату дедлайн
temp_created_date = datetime.today() # присваиваем переменной сегодняшнюю дату
note["created_date"] = datetime.strftime(temp_created_date, "%d.%m") # форматируем, убираем год

# Создаем цикл для проверки верного ввода даты дедлайн
while True:
    temp_issue_date = input("Дата дедлайн в формате дд.мм.гггг - ")

    try:
        issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y") # дата до форматирования в строку
        # преобразуем дату в строку для записи в словарь
        note["issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m") # убираем год
        break  # Выход из цикла, если дата введена правильно

    except ValueError:
    # Если возникает ошибка, значит дата введена неправильно
        print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")


# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")


# Цикл для обновления статуса заметки
while True:
    status_new = input("\nВыберите новый статус заметки "
                       "(1. Выполнено, 2. В процессе, 3. Отложено или введите свой статус): ")
    # Проверка на пустую строку
    if status_new == "":
        print("Вы ввели некорректное значение")
        continue  # Возврат к началу цикла для нового ввода

    # Конвертация ввода в число
    try:
        status_new = int(status_new)
    except ValueError:
        note["status"] = status_new
        break  # Выход из цикла после корректного пользовательского ввода

    # Если пользователь ввел число, проверяем
    if status_new == 1:
        note["status"] = statuses[0]
        break
    elif status_new == 2:
        note["status"] = statuses[1]
        break
    elif status_new == 3:
        note["status"] = statuses[2]
        break
    else:
        print("Вы ввели некорректное значение")

# Выводим новый статус заметки
print(f"\nСтатус заметки успешно обновлён на: {note['status']}")

# Проверка дедлайна
current_date = datetime.today() # присваиваем текущую дату
# используем объект timedelta, вычитаем текущую дату из даты дедлайна
days_difference = (issue_date - current_date).days # присваиваем разницу в днях
# задаем цикл для проверки истек ли дедлайн
if days_difference < 0:
    print(f"\nВнимание! Дедлайн истёк {-days_difference} дней назад.")
elif days_difference == 0:
    print("\nДедлайн сегодня!")
else:
    print(f"\nДо дедлайна осталось {days_difference} дней.")




